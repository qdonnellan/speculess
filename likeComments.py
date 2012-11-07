from database import userLikeHistory, lensComments
from comments import getUserComment
from google.appengine.api import memcache
import logging


def likeComment(lensID, userID, localUser):
	objectKey = lensID + 'commentBy' + userID
	commentObject = getUserComment(lensID, userID)
	if commentObject is not None:
		likeHistory = getLikeHistory(objectKey,localUser)
		if likeHistory is None:
			commentObject.count += 1				
			likeObject = userLikeHistory(userID = localUser.id, objectID = objectKey)
			likeObject.put()			
		else:
			likeHistory.delete()
			commentObject.count += -1

		memcache.delete('likeHistoryFor' + userID)
		commentObject.put()		
		memcache.delete('commentsFor' + lensID)
		memcache.delete(objectKey)	

def getLikeHistory(objectKey, localUser):
	likeHistory = memcache.get('likeHistoryFor' + objectKey)	
	if likeHistory is None:
		likeHistory = userLikeHistory.all().filter('objectID = ', objectKey).filter('userID = ', localUser.id).get()
		memcache.set('likeHistoryFor' + objectKey, likeHistory)
	return likeHistory	

def getUserLikes(userID):
	likes = memcache.get('likeHistoryFor' + userID)
	if likes is None:
		comments = lensComments.all().filter('userID = ', userID).run()
		likes = 0
		for comment in comments:
			likes += comment.count
		memcache.set('likeHistoryFor' + userID, likes)
	return likes
