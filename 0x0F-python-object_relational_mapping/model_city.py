#!/usr/bin/python3
""" a module that contains class definition of City """

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from model_state import Base


class City(Base):
    """ a City class that inherit from Base class"""
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
