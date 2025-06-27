#!/usr/bin/python3
""" List all State object"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    db_url = f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id.asc()):
        print(f"{state.id}: {state.name}")

    session.close()

