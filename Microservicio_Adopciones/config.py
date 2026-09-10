import os  # Permite trabajar con variables del sistema
from dotenv import load_dotenv  # Carga las variables del archivo .env

load_dotenv()  # Carga las configuraciones guardadas en .env


class Config:

    # Datos para conectarse a la base de datos
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "huellitas_felices")

    # Configuración del servidor
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
    SERVER_PORT = int(os.getenv("SERVER_PORT", 8001))
