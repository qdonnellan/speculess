import database

def getComments(lensID):
	comments = database.getComments(lensID)
	return comments
