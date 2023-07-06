from neo4j import  GraphDatabase
from neo4j.work.simple import Session

class Connections:
    #variables:
    URI = ''
    UID = ''
    PWD = ''
    #session = Session()

    def __init__(self, uri,pwd,uid = 'neo4j'):
        self.URI = uri
        self.UID = uid
        self.PWD = pwd
        
        
        driver = GraphDatabase.driver(uri= self.URI, auth=(self.UID,self.PWD)) 
        session = driver.session()
        self.session = session  
        

    def getSession(self):
        print(f'{self.URI} -- {self.UID} -- {self.PWD}')
        print(f'{self.session}')
        return self.session
        
    def getCount(self,input):
        query_1 = """
        match(n) return n.name as Name
        """
        result = self.session.run(query_1)
        hanuid = [{"name":dada["Name"]}for dada in result]

        print(hanuid)
