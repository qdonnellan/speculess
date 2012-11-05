from lensList import lensList
from lensStats import lensStats

# All operations on the lens list are stored here

def getLens(lensID):
    lensFound = None
    for lens in lensList:
        if str(lens.id) == str(lensID):
            lensFound = lens
    return lensFound

def appendStats(lensList):
 	newList = []
 	for lens in lensList:
 		lens.stats = lensStats(lens.id)
 		newList.append(lens)
 	return newList

