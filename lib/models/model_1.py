# lib/cli.py
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

def initialize_database():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            wins INTEGER DEFAULT 0
        );
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY,
            question_text TEXT
        );
        """)
        conn.commit()

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

class Question:
    def __init__(self, id=None, question_text=None):
        self.id = id
        self.question_text = question_text

if __name__ == "__main__":
    initialize_database()
    user_id, created = User.create_user("John Doe")
    user = User.find_user_by_name("John Doe")
    if user:
        print(f"{user.name} has {user.wins} wins.")
        User.update_user_wins(user.name, 3)
        User.delete_user(user.name)
    else:
        print("User not found.")