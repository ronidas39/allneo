from logging import Logger
from neo4j.work.simple import Session
from AllNeo_Code.Helper.logger import NeoLogger as NL
from AllNeo_Code.Base.setUp import Connections
from AllNeo_Code.Feature.Count import Count


class baseTest:

    def __init__(self):
        self.con = Connections('bolt://localhost:7687','ChichKa','neo4j')
        self.testSession = self.con.getSession()

class testLogger(baseTest):

    def testLogger():
        Logger = NL.getLogger("Whatever")
        Logger.warning("Test Warning")
        Logger.error("Test Error")
        Logger.exception("Test Exception")
        Logger.debug("Test Debug")
        Logger.info("Test Infos")

class testDB(baseTest):
    def testConnection(self):        
        ret_Var = False
        try:
            if(self.testSession):
                print("CONNECTION SUCCESSFUL!")
                ret_Var = True

        except:
            Logger.exception("EXCEPTION OCCURED.")
        

        #obj = con.getSession()
        """
        con.getNodeCount("Roni") # n : Node, Label, Node outBound, inbound, No of properties, 
        con.getNodeCount("Roni","-d")
        con.getLabelCount()
        con.getLableCount("-d")
        con.getNodeCountByLabel("Student")
        con.getNodeCountByLabel("Student","-d")
        con.getAllroperties()
        con.getAllroperties("-d")
        con.getPropertiesByNode("Node")
        con.getPropertiesByNode("Node","-d")
        """

        #1. Count
        #2. Count With Properties
    
    def testAllCount(self):
        countAll = Count.getAllNodeCount(self.testSession)
        print(countAll)

    
testObj = testDB()

#testObj.testLogger()
testObj.testConnection()
testObj.testAllCount()
