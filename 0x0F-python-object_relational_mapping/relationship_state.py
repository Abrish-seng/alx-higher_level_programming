#!/usr/bin/python3
"""Defines State class"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State class with attributes id and name"""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
