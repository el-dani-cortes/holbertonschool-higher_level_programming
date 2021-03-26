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
    s1 = State(name="California")
    s1.city = [City(name="San Francisco")]
    session = Session(engine)
    session.add(s1)
    session.commit()
    session.close()
