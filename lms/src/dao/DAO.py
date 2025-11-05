"""DAO Interface
   Data access object: CRUD
"""

from abc import ABC, abstractmethod

import sqlite3

class DAO(ABC):
    @abstractmethod
    def create(self, obj):
        pass

    @abstractmethod
    def read(self, id):
        pass


    @abstractmethod
    def readAll(self):
        pass


    @abstractmethod
    def update(self, obj):
        pass


    @abstractmethod
    def delete(self, id):
        pass    