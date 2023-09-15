#!/usr/bin/python3
""" a script that lists all State objects """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, dbase), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query.filter(State.name.like
                                  ('%a%')).order_by('id').all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
