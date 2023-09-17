#!/usr/bin/python3
""" a module that contains the class definition of a state """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    """ This class defines stateObject """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
