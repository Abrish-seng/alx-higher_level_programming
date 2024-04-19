#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Database connection setup
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object for California
    california = State(name="California")

    # Create a new City object for San Francisco
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City objects to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
