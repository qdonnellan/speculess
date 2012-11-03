import database
import operator

def getUseStats(lensID):
	lensUses = database.getAllUses(lensID)
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
	#For uses with greater than 60% usage, the rendering of the progress bars is weird
	#(specifically, there isn't room for the text)
	#so we have unique progress bars for >60% uses
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


