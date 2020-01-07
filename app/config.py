from dotenv import load_dotenv
import os

load_dotenv()

SECREY_KEY = os.environ.get("SECRET_KEY", "adw244fg")
DEBUG = os.environ.get("DEBUG", True)
HOST = os.environ.get("HOST", "127.0.0.1")
PORT = os.environ.get("PORT", 4000)

oracle_config = {
    "PROTOCOL": os.environ.get("DB_PROTOCOL", "oracle"),
    "USER": os.environ.get("DB_USER", "root"),
    "PASS": os.environ.get("DB_PASS", "1234"),
    "HOST": os.environ.get("DB_HOST", "localhost"),
    "DB": os.environ.get("DB_NAME", "ORCL"),
}

SQLALCHEMY_DATABASE_URI = "%s://%s:%s@%s/%s" % (
    oracle_config["PROTOCOL"],
    oracle_config["USER"],
    oracle_config["PASS"],
    oracle_config["HOST"],
    oracle_config["DB"],
)
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
