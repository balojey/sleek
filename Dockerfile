FROM python:3.12.7-bookworm as prod
RUN apt-get update && apt-get install -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*


RUN pip install poetry==1.4.2
RUN pip install setuptools
RUN pip install typing-extensions

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Installing requirements
RUN poetry install --only main
# Removing gcc
RUN apt-get purge -y \
  gcc \
  && rm -rf /var/lib/apt/lists/*

# Copying actuall application
COPY . /app/src/
RUN poetry install --only main

CMD ["/usr/local/bin/python", "sleek/main.py"]

FROM prod as dev

RUN poetry install