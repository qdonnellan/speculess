from database import lensUses, userLensBag
from userBag import getBagInstance
from google.appengine.api import memcache
import operator
import logging

def getUserUses(userID, lensID):
	userBag = getBagInstance(userID, lensID)
	useList = []
	if userBag:
		lensUses = userBag.lensUses
		if lensUses:
			allUses = lensUses.split('|')		
		for use in allUses:
			if use:
				useList.append(use)
	return useList

def setUserUses(userID, lensID, newUses):
	#newUses is a list
	useString = ''
	for use in newUses:
		useString += use + '|'
	bagInstance = getBagInstance(userID, lensID)
	if bagInstance is None:
		bagInstance = userLensBag(
				userID = userID, 
				bagStatus = 'clearStatus',
				lensID = lensID,
				lensUses = useString)
		bagInstance.put()
	else:
		bagInstance.lensUses = useString
		bagInstance.put()
	
	getBagInstance(userID, lensID, update = True)
	getLensUses(lensID, update = True)

def getLensUses(lensID, update = False):
	thisLensUses =  memcache.get('lensUsesFor' + lensID)
	if thisLensUses is None or update:
		allInstances = userLensBag.all().filter('lensID =', lensID)
		usesList = []
		for bagInstance in allInstances:
			if bagInstance.lensUses:
				thisInstancesUses = bagInstance.lensUses.split('|')
				for use in thisInstancesUses:
					if use is not None and use != '':
						usesList.append(use)
		thisLensUses = allUses(usesList).allUses
		memcache.set('lensUsesFor' + lensID,thisLensUses)
	return thisLensUses

class allUses():
	def __init__(self,useList):
		useMap = {}
		for use in useList:
			if use in useMap:
				useMap[use].count+=1
			else:
				useMap[use] = lensUse(use)
		self.allUses = useMap.values()

		

class lensUse():
	def __init__(self,useName):
		self.lensUse = useName
		self.count = 1




