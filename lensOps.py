from lensList import lensList

# All operations on the lens list are stored here

def getLens(lensID):
    lensFound = None
    for lens in lensList:
        if str(lens.id) == str(lensID):
            lensFound = lens
    return lensFound



