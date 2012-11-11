from database import appUsers
from google.appengine.api import memcache
from google.appengine.api import users
import logging

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

def changeUserInformation(userID, newNickname = None, newAbout = None, newWebsite = None, imgsrc = None):
	existingUser = checkForUser(userID)
	error = None
	if existingUser is not None:
		oldNickname = existingUser.nickname		
		if newNickname is not None and newNickname != oldNickname:
			currentNicknamesList = getNicknames()
			if newNickname not in currentNicknamesList:				
				existingUser.nickname = newNickname				
				currentNicknamesList = [x for x in currentNicknamesList if x != oldNickname] #remove ald nick from list
				currentNicknamesList.append(newNickname)
				memcache.set('currentNicknamesList', currentNicknamesList)
			else:
				error = 'username already exists'
		if newAbout is not None:
			existingUser.about = newAbout
		if newWebsite is not None:
			existingUser.website = newWebsite
		if imgsrc is not None:
			existingUser.imgsrc = imgsrc

		if error is None:
			existingUser.put()
			memcache.set(userCacheKey(userID), existingUser) #commit new user to cache
	return error

def getNicknames(newName = None):
	currentNicknamesList = memcache.get('currentNicknamesList')
	if currentNicknamesList is None:
		currentNicknamesList = []
		allUsers = appUsers.all()
		for user in allUsers:
			currentNicknamesList.append(user.nickname)
		memcache.set('currentNicknamesList', currentNicknamesList)
	return currentNicknamesList

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
	def __init__(self, existingUser=None, userID = None):				
		if userID is not None:
			existingUser = checkForUser(userID)
		else:
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
			self.website = existingUser.website	
			if self.website is None:
				self.website = ''	
			self.about = existingUser.about
			if self.about is None:
				self.about = ''
			self.nickname = existingUser.nickname
			self.id = existingUser.userID
			self.rating = existingUser.rating
			self.logoutUrl = users.create_logout_url("/")
			self.imgsrc = existingUser.imgsrc


