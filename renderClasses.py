from comments import getUserComment, getAllUserComments
from lensList import lensList
from sortComments import sortComments
from userBag import getUserBagList
from likeObjects import getUserRating, userLikedObject, getObjectLikes
from localUsers import getNickname
from lensStats import getLensStats, getTotalLensInstances
from lensOps import getLens
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
		comment.buttonStyle = 'btn-inverse'
		comment.buttonTooltip = 'Is this impression useful? Click to recommend'
	return comment


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
	def __init__(self,lensID, localUser, sortMethod = 'rating'):
		comments = sortComments(lensID, sortMethod = sortMethod, numToGet = 10)
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
		tabDict = {'have':'', 'wish':'', 'impressions':'', 'personal':''}
		if activeTab in tabDict:
			tabDict[activeTab] = 'active'
		elif activeTab == '' or activeTab not in tabDict:
			tabDict['personal'] = 'active'

		self.haveLI = tabDict['have']
		self.wishLI = tabDict['wish']
		self.impressionsLI = tabDict['impressions']
		self.personalLI = tabDict['personal']

		self.have = 'in ' + tabDict['have']
		self.wish = 'in ' + tabDict['wish']
		self.impressions = 'in ' +  tabDict['impressions']
		self.personal = 'in ' +  tabDict['personal']	

class userImpressions():
	def __init__(self,localUser,commentUserID=None):
		if commentUserID is None:
			commentUserID = localUser.id
		userComments = getAllUserComments(commentUserID)	
		impressions = []	
		for comment in userComments:
			impressions.append(impression(comment, localUser))
		self.impressions = impressions

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


