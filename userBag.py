from database import userLensBag
from google.appengine.ext import db
from google.appengine.api import memcache
import logging

def userBagCacheKey(userID, lensID):
	return userID + lensID + 'bagInstance'

def changeUserBag(userID, newBagStatus, lensID):
	if newBagStatus in ['wantIt', 'haveIt', 'doNotWant', 'clearStatus']:
		bagInstance = getBagInstance(userID, lensID)
		if bagInstance is not None:
			bagInstance.bagStatus = newBagStatus
		else:
			bagInstance = userLensBag(
				userID = userID, 
				bagStatus = newBagStatus,
				lensID = lensID)
		cacheKey = userBagCacheKey(userID, lensID)
		memcache.set(cacheKey, bagInstance)			

def getBagInstance(userID, lensID):
	cacheKey = userBagCacheKey(userID, lensID)
	bagInstance = memcache.get(cacheKey)
	if bagInstance is None:
		bagInstance = userLensBag.all().filter('userID = ', userID).filter('lensID = ', lensID).get()
		logging.info(str(bagInstance))
		memcache.set(cacheKey, bagInstance)
	if bagInstance is not None:
		if bagInstance.bagStatus == 'clearStatus':
			bagInstance = None
	return bagInstance

class lensStatus():
	def __init__(self, userID, lensID):
		bagInstance = getBagInstance(userID, lensID)
		if bagInstance is None:
			self.statusLinks = 'visible'
			self.changeStatusLink = 'none'
		else:
			self.statusLinks = 'none'
			statusDict = {'wantIt': 'want', 'haveIt': 'have', 'doNotWant': 'do not want'}
			self.status = statusDict[bagInstance.bagStatus].upper()
			self.changeStatusLink = 'visible'
			bootstrapColorDict = {'wantIt': 'info', 'haveIt': 'success', 'doNotWant': 'danger'}
			self.bootstrapColor = bootstrapColorDict[bagInstance.bagStatus]
			bootstrapIconDict = {'wantIt': 'heart', 'haveIt': 'check', 'doNotWant': 'ban-circle'}
			self.icon = bootstrapIconDict[bagInstance.bagStatus]

