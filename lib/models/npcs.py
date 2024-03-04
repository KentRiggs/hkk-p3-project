from .database import get_db_connection



class NPC:
    def __init__(self, id=None, name=None, ascii_art=None, is_killer=False):
        self.id = id
        self.name = name
        self.ascii_art = ascii_art
        self.is_killer = is_killer


    @staticmethod
    def create_table():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS npcs (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            ascii_art TEXT NOT NULL,
            is_killer BOOLEAN NOT NULL DEFAULT FALSE
        );
        """)
            conn.commit()
