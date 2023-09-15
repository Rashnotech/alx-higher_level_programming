#!/usr/bin/python3
""" a module that contains the class definition of a state """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    __tablename__ = 'states'

