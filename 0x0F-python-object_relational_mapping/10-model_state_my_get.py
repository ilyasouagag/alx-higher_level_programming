#!/usr/bin/python3
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
    alert = 0
    for element in session.query(State).order_by(State.id):
        if element.name == argv[4]:
            print(element.id)
            alert = 1
    if alert == 0:
        print("Not found")
