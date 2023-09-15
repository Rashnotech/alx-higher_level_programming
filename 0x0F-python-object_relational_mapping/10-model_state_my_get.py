#!/usr/bin/python3
""" a script that prints the State object """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbase = sys.argv[3]
    search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            user, passwd, dbase), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == search).first()
    if state is None:
        print('Not found')
    else:
        print(state.id)
