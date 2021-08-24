from AllNeo_Code.Base.setUp import Connections


class baseTest:

    def __init__(self):
        self.con = Connections('bolt://localhost:7687','ChichKa','neo4j')
        self.testSession = self.con.getSession()