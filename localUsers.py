from database import appUsers
from google.appengine.api import memcache
from google.appengine.api import users

#userStuff

def userCacheKey(userID):
	return 'localUser' + userID

def newUser(googleUserObject, success=False):
	if googleUserObject is not None:
		userID = googleUserObject.user_id()
		existingUser = checkForUser(userID)
		if existingUser is None:
			newUserObject = appUsers(userID = userID, nickname = googleUserObject.nickname())
			newUserObject.put()
			success = True
			getAllUsers(refresh = True)
		else:
			success = 'ExistingUserPresent'
	return success

def getAllUsers(refresh = False):
	allUsers = memcache.get('allUsers')
	if allUsers is None or refresh:
		allUsers = []
		users = appUsers.all()
		for user in users:
			allUsers.append(user.userID)
		memcache.set('allUsers', allUsers)
	return allUsers

def changeUserNickname(userID, newNickname):
	currentNicknamesList = memcache.get('currentNicknamesList')
	if newNickname not in currentNicknamesList:
		existingUser = checkForUser(userID)
		if existingUser is not None:
			oldNickname = existingUser.nickname
			existingUser.nickname = newNickname
			existingUser.put() #commit new nickname to db
			memcache.set(userCacheKey(userID), existingUser) #commit new nickname to cache
			currentNicknamesList = [x for x in currentNicknamesList if x != oldNickname] #remove ald nick from list
			currentNicknamesList.append(newNickname)
			memcache.set('currentNicknamesList', currentNicknamesList)

def checkForUser(userID, forceRefresh = False):
	cacheKey = userCacheKey(userID)
	userObject = memcache.get(cacheKey)
	if userObject is None or forceRefresh:
		userObject = appUsers.all().filter('userID = ', userID).get()
		if userObject is not None:
			memcache.set(cacheKey, userObject)
	return userObject

def getNickname(userID):
	nickname = 'Unknown'
	userObject = checkForUser(userID)
	if userObject is not None:
		nickname = userObject.nickname
	return nickname

class localUser():
	def __init__(self, existingUser=None):
		googleUser = users.get_current_user()		
		if googleUser:
			existingUser = checkForUser(googleUser.user_id())
		if existingUser is None:
			self.exists = False
			self.displayUser = 'None' #don't display user specific html when user not present
			self.displayAlt = 'visible' #display alternate html when no user present
		else:
			self.exists = True
			self.displayUser = 'visible' 
			self.displayAlt = 'None'
			self.nickname = existingUser.nickname
			self.id = googleUser.user_id()
			self.logoutUrl = users.create_logout_url("/")


