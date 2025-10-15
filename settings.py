import tempfile
from urllib.parse import quote_plus

DEBUG = False
LOG = False
LOG_FILE = 'app.log'
TEMP_PATH = tempfile.gettempdir()
DB_NAME = 'pep8checker'
DEBUG = False
SECRET_KEY = '0199dd51-4ee1-7d68-98f3-7dcbbaaccfb3'
USER = "user"
PASSWORD = quote_plus("password")
HOST = "127.0.0.1"

POSTGRES_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:5432/{DB_NAME}?gssencmode=disable"
