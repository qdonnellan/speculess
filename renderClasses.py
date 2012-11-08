from comments import getUserComment, getComments
from likeObjects import getUserRating, userLikedObject, getObjectLikes
from localUsers import getNickname
from lensStats import getLensStats


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
	def __init__(self,lensID, localUser):
		comments = getComments(lensID)
		self.columns = [[],[],[]]
		i = 0
		for comment in comments:
			if comment.comment != 'blank_comment':
				comment.userNickname = getNickname(comment.userID)
				comment.userRating = getUserRating(comment.userID)	
				if comment.reviewLink is None or comment.reviewLink == '':
					comment.reviewDisplay = 'none'
				else:
					comment.reviewDisplay = 'visible'			
				objectKey = 'likesFor' + lensID + comment.userID
				comment.count = getObjectLikes(objectKey)
				if userLikedObject(localUser, objectKey):
					comment.buttonStyle = 'btn-primary'
					comment.buttonTooltip = 'You liked this comment, click again to unlike'					
				else:
					comment.buttonStyle = 'btn-inverse'
					comment.buttonTooltip = 'Like this impression if you feel it is useful'			
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
		self.total = currentStats['total']
		if self.total != 0:
			self.havePercent = int(100.*self.have/self.total)
			self.wantPercent = int(100.*self.want/self.total)
			self.dontPercent = int(100.*self.dont/self.total)
		else:
			self.havePercent = 0
			self.wantPercent = 0
			self.dontPercent = 0

