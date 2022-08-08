#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base 
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """class definition of a City"""
     __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    #state_id = ""
    #name = ""
