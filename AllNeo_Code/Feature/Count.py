from AllNeo_Code.Base.setUp import Connections

class Count:

    def getAllNodeCount(session):
        query_1 = "match(n) return count(n) as Count"
        result = session.run(query_1)
        counter = [{"Count":data["Count"]}for data in result]
        #print(counter)
        return counter

    