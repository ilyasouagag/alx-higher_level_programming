#!/usr/bin/python3
"""adds the State object “Louisiana” to the
database hbtn_0e_6_usa"""
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
    object = State(name="louisiana")
    session.add(object)
    element = session.query(State).filter_by(name='Louisiana').first()
    print(element.id)
    session.commit()
