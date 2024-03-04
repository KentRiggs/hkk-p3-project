from .user import User
from .npcs import NPC
from .response import Response


def initialize_database():
    User.create_table()
    NPC.create_table()
    Response.create_table()
    
if __name__ == "__main__":
    initialize_database()