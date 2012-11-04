import webapp2
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import users
from handlers import MainHandler
from lensList import lensList
from lensOps import getLens
import comments
import database
import logging
import lensUses
import userBag
import localUsers

class MainPage(MainHandler):
    def get(self):        
        self.render('front.html', lenses=lensList, homeActive = 'active')

class lensInfo(MainHandler):    
    def get(self, lensID): 
        lens = getLens(lensID, lensList)
        bigUses, smallUses = lensUses.getRefinedUseList(lensID)
        allUses = lensUses.getAllUses(lensID)        
        listAllUses = []
        for use in allUses:
            listAllUses.append("%s" % str(use.lensUse))
        if lens is not None:       
            self.render('lensPage.html', 
                lens = lens, 
                bigUses = bigUses, 
                smallUses = smallUses,
                listAllUses = listAllUses,
                columnComments = comments.getThreeColumnComments(lensID),
                lensStatus = userBag.lensStatus(userID='testUser', lensID = lensID))
        else:
            self.redirect('/')

    def post(self, lensID):
        if 'userUse' in self.request.POST:
            userInput = self.request.get('newUse')
            database.newUse(lensID=lensID, use = userInput)
            self.redirect('/lens/%s' % lensID)
        elif 'userImpression' in self.request.POST:
            impression = self.request.get('newImpression')            
            comments.newComment(lensID=lensID, comment=impression, user = localUsers.localUser())
            self.redirect('/lens/%s' % lensID)

class lensBag(MainHandler):
    def get(self, userID = 'testUser'):
        changeBag = self.request.get('changeBag')
        if changeBag is not None:
            if '|' in changeBag:
                newBagStatus, lensID = changeBag.split('|')
                userBag.changeUserBag(userID, newBagStatus, lensID)
                self.redirect('/lens/%s' % lensID)

class userProfile(MainHandler):
    def get(self):
        localUser = localUsers.localUser()
        if localUser.exists:
            self.render('profile.html')
        else:
            self.redirect('/authenticate?error=you must be logged in for that')

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
    ('/profile', userProfile),
    ('/myBag', lensBag),
    ('.*', MainPage),
    ],debug=True)