#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, relationship


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    State.city = relationship("City")
    session = Session(engine)
    query = session.query(State).all()
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.city:
            print("    {}: {}".format(city.id, city.name))
    session.close()
