#!/usr/bin/python3
"""generate query to database
"""

from sqlalchemy import create_engine
from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    # initialize a session to communicate with database
    session = Session()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))

    session.close()
