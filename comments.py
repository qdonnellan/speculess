import database

def getComments(lensID):
	comments = database.getComments(lensID)
	return comments

def getThreeColumnComments(lensID):
	comments = getComments(lensID)
	threeColumns = [[],[],[]]
	i = 0
	for comment in comments:
		threeColumns[i].append(comment)
		if i == 2:
			i = 0
		else:
			i += 1

	return threeColumns
