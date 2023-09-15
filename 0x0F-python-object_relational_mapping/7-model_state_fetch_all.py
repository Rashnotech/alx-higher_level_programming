#!/usr/bin/python3
""" a module that list all State object from the database """

from model_state import Base, State
from sqlalchemy import sqlalchemy
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
            format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
