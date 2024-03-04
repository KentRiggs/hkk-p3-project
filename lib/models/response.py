from .database import get_db_connection



class Response:
    def __init__(self, id=None, npc_id=None, question_id=None, text=None):
        self.id = id
        self.npc_id = npc_id
        self.question_id = question_id
        self.text = text

    @staticmethod
    def create_table():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY,
            npc_id INTEGER,
            question_id INTEGER,
            text TEXT NOT NULL,
            FOREIGN KEY (npc_id) REFERENCES npcs (id),
            FOREIGN KEY (question_id) REFERENCES questions (id)
        );
        """)
            conn.commit()