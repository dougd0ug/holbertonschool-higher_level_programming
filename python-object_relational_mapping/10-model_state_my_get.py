#!/usr/bin/python3
"""
Module that contains
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, dbname, search_name = argv[1], argv[2], argv[3], argv[4]
    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == search_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
