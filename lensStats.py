from database import userLensBag
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
	totalInstances = 0
	haveInstances = 0
	wantInstances = 0
	dontInstances = 0
	for lens in bagInstances:
		if lens.bagStatus != 'clearStatus':
			totalInstances += 1
		if lens.bagStatus == 'wantIt':
			wantInstances += 1
		if lens.bagStatus == 'haveIt':
			haveInstances +=1
		if lens.bagStatus == 'doNotWant':
			dontInstances += 1
	lensStats = {'wantIt': wantInstances, 'haveIt': haveInstances, 'doNotWant': dontInstances, 'total':totalInstances}
	return lensStats



		


