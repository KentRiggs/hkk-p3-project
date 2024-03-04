import sqlite3
from contextlib import contextmanager

DATABASE_NAME = 'game.db'

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    try:
        yield conn
    finally:
        conn.close()