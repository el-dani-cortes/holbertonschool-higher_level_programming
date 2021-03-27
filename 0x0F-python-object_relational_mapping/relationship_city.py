#!/usr/bin/python3
"""
This module defines a City class that
inherits from Base class from module SQLAlchemy.
"""
from sqlalchemy import ForeignKey, Column, Integer, String
from relationship_state import Base


class City(Base):
    """
    Represents an instance of City class for SQLAlchemy module
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
