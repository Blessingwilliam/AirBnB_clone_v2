#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    if models.storage_t != 'db':
        @property
          def cities(self):
        """Getter attribute cities that returns the list of City objects from storage linked to the current State"""
        from models import storage
        from models.city import City
        if storage_t != "db":
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]
        return self.cities

