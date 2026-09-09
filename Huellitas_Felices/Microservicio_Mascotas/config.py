import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "huellitas_felices")
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
    