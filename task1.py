# Task1
# enter a dictionary and print its values with no repeat its letters
def addToDict():
    Dict = dict()
    n = input("Enter number of keys : ")
    n = int(n)
    while n > 0:
        key = input("key : ")
        val = input("value : ")
        Dict.update({key: val})
        n -= 1
    return Dict


def getUniqueStr(value):
    uniqueStr = set()
    value = str(value)
    for i in value:
        uniqueStr.add(i)
    return uniqueStr


def getUniqueness():
    uniqueList = []
    for i in addToDict().values():
        uniqueList.append(getUniqueStr(i))
    return uniqueList


print(getUniqueness())
