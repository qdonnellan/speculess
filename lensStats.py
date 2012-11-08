from database import userLensBag
from localUsers import getAllUsers
from google.appengine.api import memcache

def getLensStats(lensID, update = False):
	cacheKey = 'currentLensStats' + lensID
	currentStats = memcache.get(cacheKey)
	if currentStats is None or update == True:
		allInstances = userLensBag.all().filter('lensID =', lensID)
		currentStats = makeStatCalculation(allInstances)
		memcache.set(cacheKey, currentStats)
	return currentStats

def makeStatCalculation(bagInstances):
	haveInstances = 0
	wantInstances = 0
	dontInstances = 0
	for lens in bagInstances:		
		if lens.bagStatus == 'wantIt':
			wantInstances += 1
		if lens.bagStatus == 'haveIt':
			haveInstances +=1
		if lens.bagStatus == 'doNotWant':
			dontInstances += 1
	lensStats = {'wantIt': wantInstances, 'haveIt': haveInstances, 'doNotWant': dontInstances}
	return lensStats

def getTotalLensInstances(refresh = False):
	totalInstances = memcache.get('totalLensInstances')
	if totalInstances is None or refresh:
		totalInstances = 0
		allBagObjects = userLensBag.all()
		listAllBags = []
		for bagObject in allBagObjects:
			listAllBags.append(bagObject.userID)		
		for userID in getAllUsers():
			if userID in listAllBags:
				totalInstances += 1
		memcache.set('totalLensInstances', totalInstances)
	return totalInstances




		


