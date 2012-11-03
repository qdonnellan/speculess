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

class appUsers(db.Model):
	userID = db.StringProperty(required = True)
	nickname =db.StringProperty(required = True)





