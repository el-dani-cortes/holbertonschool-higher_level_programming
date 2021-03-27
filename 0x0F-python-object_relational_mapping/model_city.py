#!/usr/bin/python3
"""
Class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """
    Class definition for the SQLAlchemy module
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(180), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
