from google.appengine.ext import db

class lensUses(db.Model): 
	lensID = db.StringProperty(required = True)
	lensUse = db.StringProperty(required = True)
	count = db.IntegerProperty(required = True, default = 1)

class lensComments(db.Model):
	lensID = db.StringProperty(required = True)
	comment = db.TextProperty(required = True)
	userID = db.StringProperty(required = True)
	userNickname = db.StringProperty(required = False)
	reviewLink = db.StringProperty(required=False)
	reviewDisplay = db.TextProperty(required = False)
	count = db.IntegerProperty(required = True)

class userLensBag(db.Model):
	userID = db.StringProperty(required = True)
	bagStatus = db.StringProperty(required = True)
	lensID = db.StringProperty(required = True)

class appUsers(db.Model):
	userID = db.StringProperty(required = True)
	nickname =db.StringProperty(required = True)

class userLikeHistory(db.Model):
	userID = db.StringProperty(required = True)
	objectID = db.StringProperty(required = True)





