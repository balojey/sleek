import enum
import os
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings, SettingsConfigDict
from yarl import URL

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "0.0.0.0"
    port: int = 8080
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False
    debug: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database
    db_host: str = os.getenv("SLEEK_DB_HOST", "localhost")   #"localhost"
    db_port: int = os.getenv("SLEEK_DB_PORT", 5432)
    db_user: str = os.getenv("SLEEK_DB_USER", "sleek")   #"sleek"
    db_pass: str = os.getenv("SLEEK_DB_PASS", "sleek")   #"sleek"
    db_base: str = os.getenv("SLEEK_DB_BASE", "sleek")  #"sleek"
    db_echo: bool = False

    # Variables for google auth
    google_auth_client_id: str = os.getenv("SLEEK_GOOGLE_AUTH_CLIENT_ID", "")
    google_auth_client_secret: str = os.getenv("SLEEK_GOOGLE_AUTH_CLIENT_SECRET", "")

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql+psycopg2",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_base}",
            # query={'ssl':'require'},
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SLEEK_",
        env_file_encoding="utf-8",
    )


settings = Settings()