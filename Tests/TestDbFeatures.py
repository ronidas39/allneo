import baseTest
from AllNeo_Code.Feature.Count import Count
from logging import Logger

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
