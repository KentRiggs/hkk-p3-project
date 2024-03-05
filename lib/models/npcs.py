from .database import get_db_connection
import sqlite3



class NPC:
    def __init__(self, id=None, name=None, ascii_art=None, is_killer=False):
        self.id = id
        self.name = name
        self.ascii_art = ascii_art
        self.is_killer = is_killer
        self.responses = []

    def add_response(self, response):
        self.responses.append(response)

    def create_npc(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO npcs (name, ascii_art, is_killer) VALUES (?, ?, ?)",
                               (self.name, self.ascii_art, self.is_killer))
                conn.commit()
                print(f"NPC '{self.name}' created successfully.")
                return True
            except sqlite3.IntegrityError:
                print(f"Failed to create NPC '{self.name}'. Name already exists.")
                return False
       
    @staticmethod
    def delete_npc(npc_name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM npcs WHERE name = ?", (npc_name,))
            if cursor.rowcount > 0:
                print(f"NPC '{npc_name}' deleted successfully.")
                return True
            else:
                print(f"NPC '{npc_name}' not found.")
                return False

    @staticmethod
    def get_npc_by_name(name):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM npcs WHERE name = ?", (name,))
            npc_row = cursor.fetchone()
            if npc_row:
                return NPC(*npc_row)
            else:
                return None
            

    @staticmethod
    def list_all_npcs():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM npcs")
            npcs = cursor.fetchall()
            npc_objects = []
            for npc in npcs:
                npc_objects.append(NPC(*npc))
            return npc_objects
        
    @staticmethod
    def update_ascii_art(npc_name, new_ascii_art):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE npcs SET ascii_art = ? WHERE name = ?", (new_ascii_art, npc_name))
                conn.commit()
                print(f"ASCII art for NPC '{npc_name}' updated successfully.")
            except sqlite3.Error as e:
                print(f"Failed to update ASCII art for NPC '{npc_name}': {e}")


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
