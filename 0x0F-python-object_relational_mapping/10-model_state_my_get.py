#!/usr/bin/python3
"""prints the State object with the name passed as argument from the database hbtn_0e_6_usa"""
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    element = session.query(State).filter(State.name == (argv[4],))
    try:
        print(element[0].id)
    except IndexError:
        print("Not found")
