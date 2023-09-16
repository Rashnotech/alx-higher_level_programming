#!/usr/bin/python3
""" a module that contains class definition of City """

from model_state import Base
from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy import relationship


class City(Base):
    """ a City class that inherit from Base class"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
    State = relationship('states', back_populates='cities')
