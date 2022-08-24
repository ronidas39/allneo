from neo4j import  GraphDatabase
from neo4j.work.simple import Session

class Connection:
    #variables:
    URI = ''
    UID = ''
    PWD = ''

    def __init__(self, uri,pwd,user = 'neo4j'):
        self.__URI = uri
        self.__USER = user
        self.__PWD = pwd
        # print('Connections:',self.URI ,' ' ,self.UID ,' ', self.PWD)
        
        try:
            self.__driver = GraphDatabase.driver(uri= self.__URI, auth=(self.__USER,self.__PWD)) 
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()    
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response    