from dao.DAO import DAO
from domain.User import User 
import sqlite3
class UserDAO():
    def __init__(self): 
        self.connect(self)
        cursor = self.conn.cursor()


    def create(self, user):
        self.cursor.execute("INSERT INTO user (name,email, address VALUES(?,?,?))")
        self.conn.commit
        user.id=self.cursor.lastrowid
        print(user)
       

    
    def read(self, id):
        pass


    
    def readAll(self):
        pass


   
    def update(self, obj):
        pass


    
    def delete(self, id):
        pass  

    def connect(self,db="lms.db"):
        self.connect =sqlite3.connect(db)
        return self.conn
    
    def close(self):
        if self.conn: # if self.conn != null this is short hand pythonic style 
            self.conn
