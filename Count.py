import DbConnect
from DbConnect import Connection
import pandas as pd

class NodeCount:

    def __init__(self,uri,uname,pwd):
        self.self = self
        self.uri = uri
        self.uname = uname
        self.pwd = pwd
        
        # print('NodeCount:',uri,' ',uname,' ',pwd)
        self.conn = Connection(self.uri,self.pwd,self.uname)

    def getNodeCount(self,n):
        query_1 = "match("+n+") return count(n) as Count"
        result = self.conn.query(query_1)
        dat = [{"Count":val["Count"]} for val in result]
        print(dat)

        query_2 = "match("+n+") return n.id as id, n.name as name"
        result = self.conn.query(query_2)
        Val2 = [{"ID":dat["id"],"Name":dat["name"]} for dat in result]
        print(pd.DataFrame(Val2))

    def getLabelCount(self,n):
        query = "match("+n+") return count(distinct(labels(n))) as UnqLblCnt"
        result = self.conn.query(query)
        LblCnt = [{"UniqueLabelCount":dat["UnqLblCnt"]} for dat in result]
        print(LblCnt)
