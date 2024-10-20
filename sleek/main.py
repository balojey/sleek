from fasthtml.common import *
from fasthtml.oauth import GoogleAppClient, redir_url
from datetime import datetime

from sqlmodel import create_engine

from sleek.settings import settings
from sleek.db.models.room import Room


db = database('data/counts.db')
counts = db.t.counts
if counts not in db.t: counts.create(dict(name=str, count=int), pk='name')
Count = counts.dataclass()
print(settings.google_auth_client_id)

############################ AUTH BEGINS ######################

# Auth client setup for GitHub
client = GoogleAppClient(settings.google_auth_client_id, 
                         settings.google_auth_client_secret)
auth_callback_path = "/auth_redirect"

def before(req, session):
    # if not logged in, we send them to our login page
    # logged in means:
    # - 'user_id' in the session object, 
    # - 'auth' in the request object
    auth = req.scope['auth'] = session.get('user_id', None)
    if not auth: return RedirectResponse('/login', status_code=303)
    counts.xtra(name=auth)
bware = Beforeware(before, skip=['/login', auth_callback_path])

app = FastHTML(debug=settings.debug, before=bware)

# User asks us to Login
@app.get('/login')
def login(request):
    redir = redir_url(request,auth_callback_path)
    login_link = client.login_link(redir)
    # we tell user to login at github
    return P(A('Login with GitHub', href=login_link))    

# User comes back to us with an auth code from Github
@app.get(auth_callback_path)
def auth_redirect(code:str, request, session):
    redir = redir_url(request, auth_callback_path)
    user_info = client.retr_info(code, redir)
    user_id = user_info[client.id_key] # get their ID
    session['user_id'] = user_id # save ID in the session
    # create a db entry for the user
    if user_id not in counts: counts.insert(name=user_id, count=0)
    return RedirectResponse('/', status_code=303)

@app.get('/logout')
def logout(session):
    session.pop('user_id', None)
    return RedirectResponse('/login', status_code=303)

############################ AUTH ENDS ######################

@app.get('/')
def home(auth):
    return Div(
        P("Count demo"),
        P(f"Count: ", Span(counts[auth].count, id='count')),
        Button('Increment', hx_get='/increment', hx_target='#count'),
        P(A('Logout', href='/logout'))
    )

@app.get('/increment')
def increment(auth):
    c = counts[auth]
    c.count += 1
    return counts.upsert(c).count


serve(port=settings.port)
