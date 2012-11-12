import webapp2
from google.appengine.api import memcache
from google.appengine.ext import db
from google.appengine.api import users
from handlers import MainHandler
from lensOps import getLens
from lensList import lensList
from sorter import sortLenses
import likeObjects
import comments
import database
import userBag
import localUsers
import renderClasses
import logging

class MainPage(MainHandler):
    def get(self):
        lenses = renderClasses.appendStats(lensList)
        sortMethod = self.request.get('sortMethod')
        activePill = renderClasses.activePill(sortMethod)        
        self.render('front.html', lenses=sortLenses(lenses, sortMethod), activePill = activePill, homeActive = 'active')

class lensInfo(MainHandler):    
    def get(self, lensID):
        localUser = localUsers.localUser() 
        lens = getLens(lensID)  
        lensStats = renderClasses.lensStats(lensID) 
        sortMethod = self.request.get('sortMethod')           
        if lens is not None:       
            self.render('lensPage.html', 
                lens = lens,
                lensStats = renderClasses.lensStats(lensID),  
                userComment = renderClasses.userComment(lensID, localUser),               
                comments = renderClasses.threeColumns(lensID, localUser, sortMethod=sortMethod),
                activePill = renderClasses.activePill(sortMethod),
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
        redirectUrl = self.request.get('redirect')
        localUser = localUsers.localUser()
        if lensID is not None and userID is not None:
            if localUser.exists:
                likeObjects.likePress(lensID, userID, localUser)
        if redirectUrl is None or redirectUrl == '':
            self.redirect('/lens/%s' % lensID)
        else:
            self.redirect(redirectUrl)

class userProfile(MainHandler):
    def get(self, userID = None):
        activeTab = self.request.get('activeTab')
        activeTabClass = renderClasses.activeTab(activeTab)
        localUser = localUsers.localUser()
        if userID is None:            
            if localUser.exists:
                self.render('profile.html', 
                    userBag = renderClasses.userBag(localUser.id), 
                    profileActive = 'active', 
                    thisUser = localUser,
                    impressions = renderClasses.twoColumnImpressions(localUser),
                    activeTab = activeTabClass,
                    displaySecure = 'visible',
                    displaySecureAlt = 'none')
            else:
                self.redirect('/authenticate?error=you must be logged in for that')
        else:
            sameUser = False
            if localUser.exists:
                if userID == localUser.id:
                    sameUser = True
            if sameUser:
                self.redirect('/profile?activeTab=%s' % activeTab)
            else:
                thisUser = localUsers.localUser(userID = userID)
                self.render('profile.html', 
                        userBag = renderClasses.userBag(thisUser.id), 
                        impressions = renderClasses.twoColumnImpressions(localUser, commentUserID = thisUser.id),
                        activeTab = activeTabClass,
                        displaySecure = 'none',
                        thisUser = thisUser,
                        displaySecureAlt = 'visible')

    def post(self):
        if 'userImpression' in self.request.POST:
            impression = self.request.get('newImpression')
            reviewLink = self.request.get('reviewLink') 
            lensID = self.request.get('lensID')        
            comments.newComment(lensID=lensID, comment=impression, user = localUsers.localUser(), reviewLink=reviewLink)
            self.redirect('/profile?activeTab=impressions')

        if 'userInformation' in self.request.POST:
            userAbout = self.request.get('userAbout')
            userNickname = self.request.get('userNickname')
            userWebsite = self.request.get('userWebsite')
            userImage= self.request.get('userImage')
            user = localUsers.localUser()
            error = localUsers.changeUserInformation(user.id, userNickname, userAbout, userWebsite, userImage)
            if error is None:
                self.redirect('/profile')
            else:
                self.redirect('/profile?error=%s' % error)


class aboutPage(MainHandler):
    def get(self):
        self.render('about.html', aboutActive = 'active')

class userAuth(MainHandler):
    def get(self):
        error = self.request.get('error')
        newAccountSetup = self.request.get('setup')
        if newAccountSetup == 'True':            
            creationAttempt = localUsers.newUser(users.get_current_user())
            if creationAttempt == True:
                self.redirect('/?success=you have successfully created an account')
            elif creationAttempt == 'ExistingUserPresent':
                self.redirect('/?success=you are now logged in')
            else:
                self.redirect('/authenticate?error=something went wrong')

        else:
            self.render('signUpPage.html', loginUrl = users.create_login_url('/authenticate?setup=True'))


        
app = webapp2.WSGIApplication([
    ('/lens/(\w+)', lensInfo),
    ('/authenticate', userAuth),
    ('/like/lens/(\w+)/(\w+)', likeLens),
    ('/profile', userProfile),
    ('/profile/(\w+)', userProfile),
    ('/myBag', lensBag),
    ('/about', aboutPage),
    ('.*', MainPage),
    ],debug=True)