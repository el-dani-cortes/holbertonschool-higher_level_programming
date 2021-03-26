#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(180), nullable=False)
    state = relationship("City")
