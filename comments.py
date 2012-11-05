from database import lensComments, userLikeHistory
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
			userNickname = getNickname(user.id), 
			count = 0)
	else:		
		commentObject.comment = comment
		commentObject.reviewLink =reviewLink
		commentObject.reviewDisplay = reviewDisplay
	commentObject.put()
	memcache.delete('commentsFor' + lensID)


def likeComment(lensID, userID, localUser):
	objectKey = lensID + 'commentBy' + userID
	if getLikeHistory(objectKey,localUser) == False:
		commentObject = getUserComment(lensID, userID)
		if commentObject is not None:
			commentObject.count += 1
			commentObject.put()
			likeObject = userLikeHistory(userID = localUser.id, objectID = objectKey).put()
			memcache.delete('commentsFor' + lensID)
			memcache.delete(objectKey)

def getLikeHistory(objectKey, localUser):
	historyStatus = False
	likeHistory = memcache.get(objectKey)	
	if likeHistory is None:
		likeHistory = userLikeHistory.all().filter('objectID = ', objectKey)
		memcache.set(objectKey, likeHistory)
	for item in likeHistory:
		if item.userID == localUser.id:
			historyStatus = True
	return historyStatus

def getUserComment(lensID, userID):
	comments = getComments(lensID)
	userComment = None
	for comment in comments:
		if comment.userID == userID:
			userComment = comment
	return userComment

def getThreeColumnComments(lensID):
	comments = getComments(lensID)
	threeColumns = [[],[],[]]
	i = 0
	for comment in comments:
		if comment.comment != 'blank_comment':
			comment.userNickname = getNickname(comment.userID)			
			threeColumns[i].append(comment)
			if i == 2:
				i = 0
			else:
				i += 1

	return threeColumns

class userComment():
	def __init__(self, lensID, localUser):
		self.displayAlt = 'visible'
		self.display = 'none'
		if localUser.exists:
			userComment = getUserComment(lensID, localUser.id)
			if userComment is not None:
				if userComment.comment != 'blank_comment':
					self.comment = userComment.comment
					self.link = userComment.reviewLink
					self.display = 'visible'
					self.displayAlt = 'none'
		
			
			

