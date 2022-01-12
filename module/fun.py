from pymongo import *

class fun:
    def __init__(self):
        # Initialize the connection on the data base.
        self.conn = MongoClient('mongodb+srv://basdatnr:basdatnr@cluster0.45x5b.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
        self.db = self.conn.dbzalora01       # Data Base name:  TestDB
        self.cursor = self.db.Products # Collection name: collection
        
    def create(self, query={}):
        # Insert a new register.
        self.cursor.insert_many(query)
        
    def read(self, query={}):
        # Read all the register.
        for value in self.cursor.find(query):
            print(value)
        
    def update(self, query_1={}, query_2={}):
        
        # Change the first item on the list.
        self.cursor.update_one(query_1, query_2)
    
    def delete(self, query={}):
        self.cursor.delete_one(query)