#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    #name = ""
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter attribute cities that 
            returns the list of City instances
            with state_id equals to the current State.id """
            return list(filter(
                    lambda x: x.state_id == self.id ,storage.all(
                    City).values()))
