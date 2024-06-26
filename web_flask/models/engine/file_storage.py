#!/usr/bin/python3
"""This module defines the DBStorage class"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class DBStorage:
    """DB storage class"""

    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        classes = [User, State, City, Place, Review, Amenity]
        objects = {}
        if cls is None:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(cls.__name__, obj.id)
                    objects[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                objects[key] = obj
        return objects

    def new(self, obj):
        """Adds the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the current database session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute (self.__session)"""
        self.__session.remove()

