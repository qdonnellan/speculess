from database import lensComments
from google.appengine.api import memcache

def getComments(lensID):
	commentObject = memcache.get('commentsFor' + lensID)
	if commentObject is None:
		commentObject = lensComments.all().filter('lensID = ', lensID)
		memcache.set('commentsFor' + lensID, commentObject)
	return commentObject

def newComment(lensID, comment, userID):
	commentObject = lensComments(
		lensID = lensID, 
		comment = comment,
		userID = userID, 
		count = 1 )
	commentObject.put()
	memcache.delete('commentsFor' + lensID)

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
