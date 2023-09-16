#!/usr/bin/python3
""" a module that adds state object to database """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        user, passwd, dbase), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
    session.close()
