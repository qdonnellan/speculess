from comments import getUserComment, getAllUserComments
from lensList import lensList
from sorter import sortComments, sortUses
from userBag import getUserBagList
from likeObjects import getUserRating, userLikedObject, getObjectLikes
from localUsers import getNickname
from lensStats import getLensStats, getTotalLensInstances
from lensOps import getLens
from lensUses import getLensUses, getUserUses
import logging

def appendStats(lensList):
 	newList = []
 	for lens in lensList:
 		lens.stats = lensStats(lens.id)
 		newList.append(lens)
 	return newList

def formatComment(comment, localUser):
	comment.userNickname = getNickname(comment.userID)
	comment.userRating = getUserRating(comment.userID)	
	if comment.reviewLink is None or comment.reviewLink == '':
		comment.reviewDisplay = 'none'
	else:
		comment.reviewDisplay = 'visible'			
	objectKey = 'likesFor' + comment.lensID + comment.userID
	comment.count = getObjectLikes(objectKey)
	if userLikedObject(localUser, objectKey):
		comment.buttonStyle = 'btn-primary'
		comment.buttonTooltip = 'You found this impression useful. Click again to undo'					
	else:
		comment.buttonStyle = 'btn'
		comment.buttonTooltip = 'Is this impression useful? Click to recommend'
	if comment.created is not None:
		comment.time = comment.created.strftime('%d %h %Y')
	else:
		comment.time = '0'
	return comment

class userUses():
	def __init__(self,lensID, localUser):
		if localUser.exists:
			uses = getUserUses(localUser.id, lensID)
			threeUses = ['','','']
			i = 0
			for use in uses:
				if i < 3 and use != '' and use is not None:
					threeUses[i] = use
				i += 1
			self.first = threeUses[0]
			self.second = threeUses[1]
			self.third = threeUses[1]


class userComment():
	def __init__(self, lensID, localUser):
		self.displayAlt = 'visible'
		self.display = 'none'
		if localUser.exists:
			userComment = getUserComment(lensID, localUser.id)
			if userComment is not None:
				if userComment.comment != 'blank_comment':
					self.comment = userComment.comment
					self.link = userComment.reviewLink
					self.display = 'visible'
					self.displayAlt = 'none'

class threeColumns():
	def __init__(self,lensID, localUser, sortMethod = None):
		comments = sortComments(lensID, sortMethod = sortMethod, numToGet = 12)
		self.columns = [[],[],[]]
		i = 0
		for comment in comments:
			if comment.comment != 'blank_comment':
				comment = formatComment(comment, localUser)		
				self.columns[i].append(comment)
				if i == 2:
					i = 0
				else:
					i += 1

class lensStats():
	def __init__(self, lensID):
		currentStats = getLensStats(lensID)
		self.have = currentStats['haveIt']
		self.want = currentStats['wantIt']
		self.dont = currentStats['doNotWant']
		self.total = getTotalLensInstances()		
		if self.total != 0:
			self.havePercent = int(100.*self.have/self.total)
			self.wantPercent = int(100.*self.want/self.total)
			self.dontPercent = int(100.*self.dont/self.total)
		else:
			self.havePercent = 0
			self.wantPercent = 0
			self.dontPercent = 0

class activeTab():
	def __init__(self,activeTab):
		tabDict = {'have':'', 'wish':'', 'impressions':'', 'personal':'', 'default':'', 'uses':''}
		if activeTab in tabDict:
			tabDict[activeTab] = 'active'
		elif activeTab == '' or activeTab not in tabDict:
			tabDict['default'] = 'active'

		self.haveLI = tabDict['have']
		self.wishLI = tabDict['wish']
		self.impressionsLI = tabDict['impressions']
		self.personalLI = tabDict['personal']
		self.defaultLI = tabDict['default']
		self.usesLI = tabDict['uses']

		self.have = 'in ' + tabDict['have']
		self.wish = 'in ' + tabDict['wish']
		self.default = 'in ' + tabDict['default']
		self.uses = 'in ' + tabDict['uses']
		self.impressions = 'in ' +  tabDict['impressions']
		self.personal = 'in ' +  tabDict['personal']	

class activePill():
	def __init__(self,activePill):
		if activePill == 'latest':
			self.latest = 'active'
		elif activePill == 'random':
			self.random = 'active'
		elif activePill == 'age':
			self.age = 'active'
		else: #defaul active pill is rated
			self.rated = 'active'

class userImpressions():
	def __init__(self,localUser,commentUserID=None):
		if commentUserID is None:
			commentUserID = localUser.id
		userComments = getAllUserComments(commentUserID)	
		impressions = []	
		for comment in userComments:
			impressions.append(impression(comment, localUser))
		self.impressions = impressions

class twoColumnImpressions():
	def __init__(self,localUser, commentUserID=None):
		allImpressions = userImpressions(localUser, commentUserID)
		self.columns = [[],[]]
		i=0
		for impression in allImpressions.impressions:
			self.columns[i].append(impression)
			if i == 1:
				i = 0
			else:
				i += 1

class impression():
	def __init__(self, comment, localUser):
		self.comment = formatComment(comment, localUser)
		lens = getLens(comment.lensID)
		lens.stats = lensStats(lens.id)
		self.lens = lens

class userBag():
	def __init__(self, userID):
		lensList = getUserBagList(userID)
		haveList = []
		wantList = []
		for lens in lensList:
			if lens.bagStatus == 'haveIt':
				haveList.append(getLens(lens.lensID))
			elif lens.bagStatus == 'wantIt':
				wantList.append(getLens(lens.lensID))
		self.want = appendStats(wantList)
		self.have = appendStats(haveList)

class makeAlerts():
    def __init__(self, error = None, success = None):
        self.errorMsg = error
        self.successMsg = success
        if error is not None and error != '':
            self.errorDisplay = 'visible'
        else:
            self.errorDisplay = 'none'

        if success is not None and success != '':
            self.successDisplay = 'visible'
        else:
            self.successDisplay = 'none'

class lensUses():
	def __init__(self, lensID):
		allUses = getLensUses(lensID)
		self.uses = sortUses(allUses)
		
		self.source = ""
		for use in allUses:
			self.source += '"%s",' % use.lensUse
		self.source = '[%s " "]' % self.source
		




