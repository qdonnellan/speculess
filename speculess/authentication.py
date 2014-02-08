from google.appengine.api import users

def loginRequired(wrapped_function):
        #Decorator for ensuring user authentication for protected code       
        google_user = users.get_current_user()     
        if user:
            wrapped_function(user)
        else:
            self.redirect("/?errors=You must be logged in to view that content")