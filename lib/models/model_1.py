from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from contextlib import contextmanager


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False) 
    wins = Column(Integer, default=0)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question_text = Column(String)


def create_user(name, session):
    existing_user = session.query(User).filter_by(name=name).first()
    if existing_user:
        return existing_user, False 
    else:
        new_user = User(name=name)
        session.add(new_user)
        session.commit()
        print(f"User '{name}' created successfully.")
        return new_user, True  

def delete_user(name, session):
    user = session.query(User).filter_by(name=name).first()
    if user:
        session.delete(user)
        session.commit()
        return True
    print(f"User '{name}' not found.")
    return False

def update_user_wins(name, session, additional_wins=1):
    user = session.query(User).filter_by(name=name).first()
    if user:
        user.wins += additional_wins
        session.commit()
        return True
    print(f"User '{name}' not found.")
    return False

def find_user_by_name(name, session):
    return session.query(User).filter_by(name=name).first()


def list_all_users(session):
    users = session.query(User).all()
    for user in users:
        print(f"User: {user.name}, Wins: {user.wins}")


engine = create_engine('sqlite:///game.db', echo=False)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

if __name__ == "__main__":
    with session_scope() as session:
        user = find_user_by_name("some_username", session)
        if user:
            print(f"{user.name} has {user.wins} wins.")
        else:
            print("User not found.")

    with session_scope() as session:
        success = delete_user("some_username", session)
        if not success:
         print("User not found or could not be deleted.")