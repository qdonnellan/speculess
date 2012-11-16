from database import lensUses
from userBag import getBagInstance
from google.appengine.api import memcache
import operator

def newUse(lensID, use):
	useObject = getSpecificUse(lensID, use)	
	if useObject is not None:
		useObject.count += 1
	else:
		useObject = lensUses(lensUse = use, count = 1, lensID = lensID)
	useObject.put()
	memcache.set(lensID + '|' + use, useObject)
	memcache.delete('uses' + lensID)

def getUserUses(userID, lensID):
	userBag = getBagInstance(userID, lensID)
	lensUses = userBag.lensUses
	if lensUses:
		allUses = lensUses.split('|')
	useList = []
	for use in allUses:
		if use:
			useList.append(use)
	return useList

def setUserUses(userID, lensID, newUses):
	#newUses is a list with 3 elements		
	useString = '%s|%s|%s' % (newUses[0:3])
	userBag = getBagInstance(userID, lensID)
	userBag.lensUses = useString
	userBag.put()
	getBagInstance(userID, lensID, update = True)

def getLensUses(lenID, update = False):
	allInstances = userLensBag.all().filter('lensID =', lensID)
	usesList = []
	for bagInstance in allInstances:
		if bagInstance.lensUses:
			thisInstancesUses = bagInstance.lensUses.split('|')
			for use in thisInstancesUses:
				usesList.append(use)
	return usesList

def getAllUses(lensID = None):
	if lensID is not None:
		allUses = memcache.get('uses' + lensID)
		if allUses is None:
			allUses = lensUses.all().filter('lensID = ', lensID)
			memcache.set('uses' + lensID, allUses)

	else:
		allUses = memcache.get('absolutelyAllUses')
		if allUses is None:
			allUses = lensUses.all()
			memcache.set('absolutelyAllUses', allUses)
	return allUses

def getSpecificUse(lensID, use):
	specificUse = memcache.get(lensID + '|' + use )
	if specificUse is None:
		specificUse = lensUses.all().filter('lensID = ', lensID).filter('lensUse = ', use).get()
		memcache.set(lensID + '|' + use, specificUse)
	return specificUse


class createUseClass():
	def __init__(self, useObject, totalUses):
		self.count = useObject.count
		percentUsed = 1.*useObject.count/totalUses *100
		percentUsedString = '%s' % int(percentUsed)
		self.percent = percentUsedString
		self.useName = useObject.lensUse


