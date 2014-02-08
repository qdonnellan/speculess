from lensList import lensList

def getLens(lensID):
    lensFound = None
    for lens in lensList:
        if str(lens.id) == str(lensID):
            lensFound = lens
    return lensFound





