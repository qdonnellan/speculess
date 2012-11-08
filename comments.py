from database import lensComments
from localUsers import getNickname
from google.appengine.api import memcache


def getComments(lensID):
	commentObject = memcache.get('commentsFor' + lensID)
	if commentObject is None:
		commentObject = lensComments.all().filter('lensID = ', lensID)
		memcache.set('commentsFor' + lensID, commentObject)
	return commentObject

def newComment(lensID, comment, user, reviewLink = None):
	if reviewLink is None or reviewLink == '':
		reviewDisplay = 'none'
	else:
		reviewDisplay = 'visible'

	if comment is None or comment == '':
		comment = 'blank_comment'

	commentObject = lensComments.all().filter('lensID =', lensID).filter('userID = ', user.id).get()
	if commentObject is None:
		commentObject = lensComments(
			lensID = lensID,
			comment = comment,
			reviewLink = reviewLink,
			reviewDisplay = reviewDisplay,
			userID = user.id,
			count = 0)
		commentObject.put()
	else:
		if comment == 'blank_comment':
			commentObject.delete()			
		else:		
			commentObject.comment = comment
			commentObject.reviewLink =reviewLink
			commentObject.reviewDisplay = reviewDisplay
			commentObject.put()	
	memcache.delete('commentsFor' + lensID)

def getUserComment(lensID, userID):
	comments = getComments(lensID)
	userComment = None
	for comment in comments:
		if comment.userID == userID:
			userComment = comment
	return userComment


		
			
			

