from google.appengine.ext import db
from google.appengine.api import memcache
import logging

class lensUses(db.Model): 
	lensID = db.StringProperty(required = True)
	lensUse = db.StringProperty(required = True)
	count = db.IntegerProperty(required = True, default = 1)

class lensComments(db.Model):
	lensID = db.StringProperty(required = True)
	comment = db.TextProperty(required = True)
	userID = db.StringProperty(required = True)
	count = db.IntegerProperty(required = True)

class userLensBag(db.Model):
	userID = db.StringProperty(required = True)
	bagStatus = db.StringProperty(required = True)
	lensID = db.StringProperty(required = True)

def newUse(lensID, use):
	useObject = getSpecificUse(lensID, use)	
	if useObject is not None:
		logging.info('this use object is not NONE')
		useObject.count += 1
	else:
		useObject = lensUses(lensUse = use, count = 1, lensID = lensID)
	useObject.put()
	memcache.set(lensID + '|' + use, useObject)
	memcache.delete('uses' + lensID)

def getAllUses(lensID):
	allUses = memcache.get('uses' + lensID)
	if allUses is None:
		allUses = lensUses.all().filter('lensID = ', lensID)
		memcache.set('uses' + lensID, allUses)
	return allUses

def getSpecificUse(lensID, use):
	specificUse = memcache.get(lensID + '|' + use )
	if specificUse is None:
		specificUse = lensUses.all().filter('lensID = ', lensID).filter('lensUse = ', use).get()
		memcache.set(lensID + '|' + use, specificUse)
	return specificUse

def getComments(lensID):
	commentObject = memcache.get('commentsFor' + lensID)
	if commentObject is None:
		commentObject = lensComments.all().filter('lensID = ', lensID)
		memcache.set('commentsFor' + lensID, commentObject)
	return commentObject

def newComment(lensID, comment, userID):
	commentObject = lensComments(
		lensID = lensID, 
		comment = comment,
		userID = userID, 
		count = 1 )
	commentObject.put()
	memcache.delete('commentsFor' + lensID)





