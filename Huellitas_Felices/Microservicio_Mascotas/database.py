from contextlib import contextmanager
import pymysql
from config import Config

def _get_connection():
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        db=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
    )

@contextmanager
def get_cursor(commit: bool = False):
    """
    Context manager: abre conexión y cursor, y garantiza el cierre
    aunque ocurra una excepción (evita repetir try/finally en cada función).
    'commit=True' se usa solo en operaciones de escritura (INSERT/UPDATE/DELETE).
    """
    conn = _get_connection()
    try:
        with conn.cursor() as cursor:
            yield cursor
            if commit:
                conn.commit()
    finally:
        conn.close()
