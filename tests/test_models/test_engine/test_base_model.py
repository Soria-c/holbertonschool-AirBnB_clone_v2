#!/usr/bin/python3
"""Module that describe the BDStorage test class"""
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class TestDBStorage(unittest.TestCase):
    """Class for test the BaseModel Class method and atributes"""

    def setUp(self):
        """All variables that we need"""
        self.storage = DBStorage()

    
