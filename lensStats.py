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

class lensStats():
	def __init__(self, lensID):
		currentStats = getLensStats(lensID)
		self.have = currentStats['haveIt']
		self.want = currentStats['wantIt']
		self.dont = currentStats['doNotWant']
		self.total = currentStats['total']
		if self.total != 0:
			self.havePercent = int(100.*self.have/self.total)
			self.wantPercent = int(100.*self.want/self.total)
			self.dontPercent = int(100.*self.dont/self.total)
		else:
			self.havePercent = 0
			self.wantPercent = 0
			self.dontPercent = 0

		


