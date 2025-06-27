#!/usr/bin/python3
"""
Module that contains
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    search_name = argv[4]
    db_url = f"mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}"

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
