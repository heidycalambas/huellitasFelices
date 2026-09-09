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

    conn = _get_connection()

    try:

        with conn.cursor() as cursor:

            yield cursor

            if commit:
                conn.commit()

    finally:

        conn.close()