#!/usr/bin/python3
""" a module that print the first State object from the database """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user, passwd, dbase), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    state = session.query(State).order_by('id').first()
    if state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(state.id, state.name))
