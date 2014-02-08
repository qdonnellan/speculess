from comments import getComments
from likeObjects import getObjectLikes
from google.appengine.api import memcache
import operator
import logging
import random

def sortComments(lensID, sortMethod = None, forceRefresh = False, numToGet = 12):
	comments = getComments(lensID)
	commentList = []	

	if sortMethod == 'random':
		for comment in comments:
			commentList.append(comment)
		comments = random.sample(commentList,min(numToGet, len(commentList)))

	elif sortMethod == 'latest':
		comments = sorted(comments, key=operator.attrgetter('created'), reverse=True)

	else:		
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

def sortLenses(lensList, sortMethod=None):
	#only works on lensList with appended stats
	tempTuple = []
	

	if sortMethod == 'age':
		logging.info('sort method is age')
		for lens in lensList:
			tempTuple.append([lens.born, lens])
		tempTuple = sorted(tempTuple, key=operator.itemgetter(0), reverse = True)

		lensList = []
		for lens in tempTuple:
			lensList.append(lens[1])

	else: #sortMethod == 'have': is the default sort
		for lens in lensList:
			tempTuple.append([lens.stats.have, lens.stats.want, lens.stats.dont, lens])

		#sort first by wants, then by haves to force want as the secondary key
		tempTuple = sorted(tempTuple, key=operator.itemgetter(2), reverse = False)
		tempTuple = sorted(tempTuple, key=operator.itemgetter(1), reverse = True)		
		tempTuple = sorted(tempTuple, key=operator.itemgetter(0), reverse = True)

		lensList = []
		for lens in tempTuple:
			lensList.append(lens[3])
	return lensList

def sortUses(allUsesObject):
	tempTuple = []
	for use in allUsesObject:
		tempTuple.append([use.count, use])
	tempTuple = sorted(tempTuple, key=operator.itemgetter(0), reverse = True)

	useList = []
	for use in tempTuple:
		useList.append(use[1])
	return useList


