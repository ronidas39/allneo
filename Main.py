from Count import NodeCount

UserName = input("Enter Username:")
PassWord = input("Enter Password:")

def CallCount():
    nc = NodeCount('bolt://localhost:7687',UserName,PassWord)

    #Node Count
    print("-------------Value Match---------------")
    nc.getNodeCount("n:Person{name:'Martin Sheen'}")

    print("------------Pattern Match--------------")
    nc.getNodeCount("n")

    #Label Count
    print("------Label Count by Value Match-------")
    nc.getLabelCount("n")

CallCount()    