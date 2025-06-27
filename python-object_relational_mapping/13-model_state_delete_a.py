#!/usr/bin/python3
"""
module
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, dbname = argv[1], argv[2], argv[3]
    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in state_to_delete:
        session.delete(state)

    session.commit()
    session.close()
