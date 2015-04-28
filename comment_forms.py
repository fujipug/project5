import webapp2
import cgi
import models
from google.appengine.api import users

from base_handler import BaseHandler
from models import comment

class CommentFormHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}
        # check if user is logged in or not and reroute appropriately
        if user:
            url = users.create_logout_url('/')
            url_linktext = "Sign out"
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = "Sign In"
        template_values ={
            'user': user,
            'url': url,
            'url_linktext':url_linktext,
            #'parking_lots': ParkingLot.query()
        }

        self.render("./templates/comment_forms.html", template_values)

    def post(self): 
        comment = models.Comment(
            text=self.request.get('comment'),
            atype=int(self.request.get('atype')),
            )
        comment_key = comment.put()

        self.redirect("/")
        

# encapsulating posts into an app
app = webapp2.WSGIApplication([
    ('/comment_forms', CommentFormHandler)
], debug=True)
