import webapp2
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import users
from handlers import MainHandler
from lensOps import getLens, appendStats
from lensList import lensList
import likeObjects
import comments
import database
import logging
import userBag
import localUsers
import renderClasses

class MainPage(MainHandler):
    def get(self):        
        self.render('front.html', lenses=appendStats(lensList), homeActive = 'active')

class lensInfo(MainHandler):    
    def get(self, lensID):
        localUser = localUsers.localUser() 
        lens = getLens(lensID)                
        if lens is not None:       
            self.render('lensPage.html', 
                lens = lens,
                lensStats = renderClasses.lensStats(lensID),  
                userComment = renderClasses.userComment(lensID, localUser),               
                comments = renderClasses.threeColumns(lensID, localUser),
                lensStatus = userBag.lensStatus(localUser, lensID = lensID))
        else:
            self.redirect('/')

    def post(self, lensID):
        if 'userUse' in self.request.POST:
            userInput = self.request.get('newUse')
            database.newUse(lensID=lensID, use = userInput)
            self.redirect('/lens/%s' % lensID)
        elif 'userImpression' in self.request.POST:
            impression = self.request.get('newImpression')
            reviewLink = self.request.get('reviewLink')         
            comments.newComment(lensID=lensID, comment=impression, user = localUsers.localUser(), reviewLink=reviewLink)
            self.redirect('/lens/%s' % lensID)

class lensBag(MainHandler):
    def get(self):
        localUser = localUsers.localUser()
        changeBag = self.request.get('changeBag')
        if changeBag is not None:
            if '|' in changeBag:
                newBagStatus, lensID = changeBag.split('|')
                userBag.changeUserBag(localUser.id, newBagStatus, lensID)
                self.redirect('/lens/%s' % lensID)

class likeLens(MainHandler):
    def get(self, lensID=None, userID = None):
        localUser = localUsers.localUser()
        if lensID is not None and userID is not None:
            if localUser.exists:
                likeObjects.likePress(lensID, userID, localUser)
        self.redirect('/lens/%s' % lensID)

class userProfile(MainHandler):
    def get(self):
        localUser = localUsers.localUser()
        if localUser.exists:
            self.render('profile.html', userBag = userBag.userBag(localUser.id))
        else:
            self.redirect('/authenticate?error=you must be logged in for that')

class aboutPage(MainHandler):
    def get(self):
        self.render('about.html', aboutActive = 'active')

class userAuth(MainHandler):
    def get(self):
        newAccountSetup = self.request.get('setup')
        if newAccountSetup == 'True':            
            creationAttempt = localUsers.newUser(users.get_current_user())
            if creationAttempt == True:
                self.redirect('/?creation=success')
            elif creationAttempt == 'ExistingUserPresent':
                self.redirect('/?error=you are now logged in!')
            else:
                self.redirect('/authenticate?error=something went wrong')

        else:
            self.render('signUpPage.html', loginUrl = users.create_login_url('/authenticate?setup=True'))


        
app = webapp2.WSGIApplication([
    ('/lens/(\w+)', lensInfo),
    ('/authenticate', userAuth),
    ('/like/lens/(\w+)/(\w+)', likeLens),
    ('/profile', userProfile),
    ('/myBag', lensBag),
    ('/about', aboutPage),
    ('.*', MainPage),
    ],debug=True)