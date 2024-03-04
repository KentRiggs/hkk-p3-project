from .database import get_db_connection
import sqlite3


class User:
    def __init__(self, id=None, name=None, wins=0):
        self.id = id
        self.name = name
        self.wins = wins
    
    @staticmethod
    def create_user(name):
     with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()
            print(f"User '{name}' created successfully.")
            return cursor.lastrowid, True
        except sqlite3.IntegrityError:
            return None, False
    
    @staticmethod
    def find_user_by_name(name):
     with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        user_row = cursor.fetchone()
        if user_row:
            return User(*user_row)
        else:
            return None
        
    @staticmethod
    def update_user_wins(name, additional_wins=1):
     with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET wins = wins + ? WHERE name = ?", (additional_wins, name))
        if cursor.rowcount == 0:
            print(f"User '{name}' not found.")
            return False
        conn.commit()
        return True
     
    @staticmethod
    def delete_user(name):
     with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE name = ?", (name,))
        if cursor.rowcount == 0:
            print(f"User '{name}' not found.")
            return False
        conn.commit()
        return True
     
    @staticmethod
    def list_all_users():
     with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print(f"User: {user[1]}, Wins: {user[2]}")

    @staticmethod
    def create_table():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                wins INTEGER DEFAULT 0
            );
            """)
            conn.commit()