from database import lensUses
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

def getUseStats(lensID):
	lensUses = getAllUses(lensID)
	totalUses = 0
	for use in lensUses:
		totalUses += use.count
	sortedUses = sorted(lensUses, key=operator.attrgetter('count'), reverse = True)
	topUses = sortedUses[0:min(10,len(sortedUses))]
	topUseList = []
	for use in topUses:
		topUseList.append(createUseClass(use, totalUses))
	return topUseList

def getRefinedUseList(lensID):
	useList = getUseStats(lensID)
	bigPercent = []
	smallPercent = []
	for use in useList:
		if int(use.percent) > 60:
			bigPercent.append(use)
		else:
			smallPercent.append(use)
	return bigPercent, smallPercent

class createUseClass():
	def __init__(self, useObject, totalUses):
		self.count = useObject.count
		percentUsed = 1.*useObject.count/totalUses *100
		percentUsedString = '%s' % int(percentUsed)
		self.percent = percentUsedString
		self.useName = useObject.lensUse


