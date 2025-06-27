#!/usr/bin/python3
"""
Module containing function displaying objects from a database.
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    Lists first State object from a database.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    state = session.query(State).filter(State.name == search_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
