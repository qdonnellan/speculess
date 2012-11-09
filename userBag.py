from database import userLensBag
from lensStats import getLensStats, getTotalLensInstances
from lensOps import getLens
from google.appengine.ext import db
from google.appengine.api import memcache

def userBagCacheKey(userID, lensID=None):
	if lensID is not None:
		return userID + lensID + 'bagInstance'
	else:
		return 'userBag' + userID

def changeUserBag(userID, newBagStatus, lensID):
	if newBagStatus in ['wantIt', 'haveIt', 'doNotWant', 'clearStatus']:
		bagInstance = getBagInstance(userID, lensID)
		if newBagStatus != 'clearStatus':
			if bagInstance is not None:
				bagInstance.bagStatus = newBagStatus
			else:
				bagInstance = userLensBag(
					userID = userID, 
					bagStatus = newBagStatus,
					lensID = lensID)
			bagInstance.put()
			cacheKey = userBagCacheKey(userID, lensID)	#get the individual lens bag key	
			memcache.set(cacheKey, bagInstance)	
		elif newBagStatus == 'clearStatus':
			if bagInstance is not None:
				bagInstance.delete()
		updateUserBag(userID)
		getBagInstance(userID, lensID, update = True)
		getLensStats(lensID, update = True)
		getTotalLensInstances(refresh = True)

def updateUserBag(userID, fetch = False):
	userBag = userLensBag.all().filter('userID = ', userID)
	cachedBag = []
	for lens in userBag:
		cachedBag.append(lens)		
	cacheKey = userBagCacheKey(userID)
	memcache.set(cacheKey, cachedBag)
	if fetch:
		return cachedBag



def getUserBagList(userID):
	cacheKey = userBagCacheKey(userID)
	userBag = memcache.get(cacheKey)
	if userBag is None:
		userBag = updateUserBag(userID, fetch=True)
	return userBag


def getBagInstance(userID, lensID, update = False):
	cacheKey = userBagCacheKey(userID, lensID)
	bagInstance = memcache.get(cacheKey)
	if bagInstance is None or update:
		bagInstance = userLensBag.all().filter('userID = ', userID).filter('lensID = ', lensID).get()
		memcache.set(cacheKey, bagInstance)
	if bagInstance is not None:
		if bagInstance.bagStatus == 'clearStatus':
			bagInstance = None
	return bagInstance

class lensStatus():
	def __init__(self, user, lensID):
		if user.exists:
			bagInstance = getBagInstance(user.id, lensID)
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



