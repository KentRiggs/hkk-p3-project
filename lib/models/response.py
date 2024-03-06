from .database import get_db_connection
import sqlite3



class Response:
    def __init__(self, id=None, name=None, responses=None, is_suspicious=False):
        self.id = id
        self.name = name
        self.responses = responses if responses else []
        self.is_suspicious = is_suspicious

    def create_response(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO responses (name, response_1, response_2, response_3, is_suspicious) VALUES (?, ?, ?, ?, ?)",
                               (self.name, self.responses[0], self.responses[1], self.responses[2], self.is_suspicious))
                conn.commit()
                print("Response created successfully.")
                return True
            except sqlite3.IntegrityError:
                print("Failed to create response.")
                return False
    @staticmethod
    def delete_response(response_name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM responses WHERE name = ?", (response_name, ))
            if cursor.rowcount > 0:
                conn.commit()
                print("Response deleted successfully.")
                return True
            else:
                print("Response not found.")
                return False
            
    @staticmethod
    def list_all_responses():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM responses")
            responses = cursor.fetchall()
            return responses 
        
    @staticmethod
    def get_suspicious_responses():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM responses WHERE is_suspicious = ?", (True,))
            suspicious_responses = cursor.fetchall()
            return suspicious_responses
        
    @staticmethod
    def get_innocent_responses():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM responses WHERE is_suspicious = ?", (False,))
            innocent_responses = cursor.fetchall()
            return innocent_responses

    @staticmethod
    def create_table():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS responses (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    response_1 TEXT NOT NULL,
                    response_2 TEXT NOT NULL,
                    response_3 TEXT NOT NULL,
                    is_suspicious BOOLEAN NOT NULL
                );
            """)
            conn.commit()