import webapp2
from google.appengine.api import memcache
from google.appengine.ext import db
from handlers import MainHandler
from lensList import lensList
from lensOps import getLens
import comments
import database
import logging
import lensUseStats
import userBag


class MainPage(MainHandler):
    def get(self):        
        self.render('front.html', lenses=lensList, homeActive = 'active')

class lensInfo(MainHandler):    
    def get(self, lensID): 
        lens = getLens(lensID, lensList)
        bigUses, smallUses = lensUseStats.getRefinedUseList(lensID)
        allUses = database.getAllUses(lensID)        
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
            database.newComment(lensID=lensID, comment=impression, userID='randomUser')
            self.redirect('/lens/%s' % lensID)

class lensBag(MainHandler):
    def get(self, userID = 'testUser'):
        changeBag = self.request.get('changeBag')
        if changeBag is not None:
            if '|' in changeBag:
                newBagStatus, lensID = changeBag.split('|')
                userBag.changeUserBag(userID, newBagStatus, lensID)
                self.redirect('/lens/%s' % lensID)

        
app = webapp2.WSGIApplication([
    ('/lens/(\w+)', lensInfo),
    ('/myBag', lensBag),
    ('.*', MainPage),
    ],debug=True)