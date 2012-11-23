import os
import jinja2
import webapp2
from localUsers import localUser
from renderClasses import makeAlerts

template_dir=os.path.join(os.path.dirname(__file__),"templates")
jinja_environment=jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
        
    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):    
    	alert = makeAlerts(error = self.request.get('error'), success = self.request.get('success'))	
        self.write(self.render_str(template, localUser = localUser(), alert = alert, **kw)) 

               





        
            
