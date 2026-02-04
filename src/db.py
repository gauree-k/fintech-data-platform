import psycopg
from contextlib import contextmanager
from .config import PGConfig

@contextmanager
def get_conn():
    conn = psycopg.connect(PGConfig().dsn)
    try:
        yield conn
    finally:
        conn.close()
