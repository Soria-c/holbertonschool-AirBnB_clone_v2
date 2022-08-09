#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base 
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel, Base):
    """class definition of a City"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    #state_id = ""
    #name = ""
