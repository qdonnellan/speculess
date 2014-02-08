from database import likes
from localUsers import checkForUser
from google.appengine.api import memcache
import logging

def likePress(lensID, ownerID, localUser):
	likeKey = 'likesFor' + lensID + ownerID
	if userLikedObject(localUser, likeKey):
		logging.info('user already liked this')
		undoLike(likeKey, localUser, ownerID)
	else:		
		doLike(likeKey,localUser, ownerID)

def doLike(likeKey, localUser, ownerID):
	newLike = likes(objectID = likeKey, userID = localUser.id).put()
	updateUserRating(ownerID, 1)
	memcache.delete('likesFor' + likeKey)
	memcache.delete('likeHistoryFor' + localUser.id)

def undoLike(likeKey, localUser, ownerID):
	oldLike = likes.all().filter('objectID = ', likeKey).filter('userID =',localUser.id).get()
	oldLike.delete()
	updateUserRating(ownerID, -1)
	memcache.delete('likesFor' + likeKey)
	memcache.delete('likeHistoryFor' + localUser.id)

def getObjectLikes(likeKey):
	totalLikes = memcache.get('likesFor' + likeKey)
	if totalLikes is None:
		likeQuery = likes.all().filter('objectID = ', likeKey)
		totalLikes = 0
		for like in likeQuery:
			totalLikes += 1
		memcache.set('likesFor' + likeKey, totalLikes)
	return totalLikes

def getUserLikeHistory(localUser):
	if localUser.exists:
		likeHistory = memcache.get('likeHistoryFor' + localUser.id)
		if likeHistory is None:
			allLikes = likes.all().filter('userID =', localUser.id)
			likeHistory = []
			for like in allLikes:
				likeHistory.append(like)
			memcache.set('likeHistoryFor' + localUser.id, likeHistory)
	else:
		likeHistory = []
	return likeHistory

def userLikedObject(localUser,objectID):
	likeHistory = getUserLikeHistory(localUser)
	ping = False
	for like in likeHistory:
		if like.objectID == objectID:
			ping = True
	return ping

def updateUserRating(userID, increment):
	user = checkForUser(userID)
	if user:
		if user.rating:
			user.rating += increment
		else:
			user.rating = increment
		user.put()
		checkForUser(userID, forceRefresh = True)

def getUserRating(userID):
	user = checkForUser(userID)
	if user:
		if user.rating is None:
			rating = 0
		else:
			rating = user.rating
	else:
		rating = 0
	return rating

