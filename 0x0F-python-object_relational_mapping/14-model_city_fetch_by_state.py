#!/usr/bin/python3
"""prints contents of a database joined to another
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, asc
from model_state import State, Base
from model_city import City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    result = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id))

    for row in result:
        print(row.state.name + ': (' + str(row.id) + ') ' + row.name)
