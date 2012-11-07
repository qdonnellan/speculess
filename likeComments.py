from database import userLikeHistory, lensComments
from comments import getUserComment
from google.appengine.api import memcache
import logging


def likeComment(lensID, userID, localUser):
	objectKey = lensID + 'commentBy' + userID
	commentObject = getUserComment(lensID, userID)
	if commentObject is not None:
		likeHistory = getLikeHistory(objectKey,localUser)
		if  likeHistory == False:		
			if commentObject is not None:
				commentObject.count += 1				
				likeObject = userLikeHistory(userID = localUser.id, objectID = objectKey).put()
				incrementUserLikes(userID, 1)
		else:
			likeHistory.delete()
			commentObject.count += -1
			incrementUserLikes(userID, -1)
		commentObject.put()		
		memcache.delete('commentsFor' + lensID)
		memcache.delete(objectKey)
	
	

def getLikeHistory(objectKey, localUser):
	historyStatus = False
	likeHistory = memcache.get(objectKey)	
	if likeHistory is None:
		likeHistory = userLikeHistory.all().filter('objectID = ', objectKey)
		memcache.set(objectKey, likeHistory)
	if localUser.exists:
		for item in likeHistory:
			if item.userID == localUser.id:
				historyStatus = item
	return historyStatus

def getUserLikes(userID):
	likes = memcache.get('likeHistoryFor' + userID)
	if likes is None:
		comments = lensComments.all().filter('userID = ', userID).run()
		likes = 0
		for comment in comments:
			likes += comment.count
		memcache.set('likeHistoryFor' + userID, likes)
	return likes

def incrementUserLikes(userID, increment):
	likes = getUserLikes(userID)
	likes += increment
	memcache.set('likeHistoryFor' + userID, likes)