from comments import getComments
from likeObjects import getObjectLikes
from google.appengine.api import memcache
import operator

def sortComments(lensID, sortMethod = None, forceRefresh = False, numToGet = None):
	comments = getComments(lensID)
	commentList = []
	if sortMethod == 'rating' or forceRefresh:		
		for comment in comments:
			objectKey = 'likesFor' + lensID + comment.userID
			commentList.append([getObjectLikes(objectKey),comment])
		commentList = sorted(commentList, key=operator.itemgetter(0), reverse=True)

	comments = []
	for item in commentList:
		comments.append(item[1])

	if numToGet is not None:
		comments = comments[0:numToGet]	
	return comments