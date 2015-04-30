import webapp2
import cgi
import models
from google.appengine.api import users
from google.appengine.ext import ndb

from base_handler import BaseHandler
from models import comment

class CommentFormHandler(BaseHandler):
    '''
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
        lot_id = self.request.get('id')
        lot_key = ndb.Key(urlsafe=lot_id)
        lot = lot_key.get()
        template_values ={
            'user': user,
            'url': url,
            'url_linktext':url_linktext,
            'lot_id': lot_id,
        }

        self.render("./templates/comment_forms.html", template_values)
    '''
    def post(self):
        lot_id = self.request.get('lot_id')
        lot_key = ndb.Key(urlsafe=lot_id)
        lot = lot_key.get()
        comment = models.Comment(
            text=self.request.get('comment'),
            atype=int(self.request.get('atype')),
            lot=[lot_key],
            author=self.user
            )
        comment_key = comment.put()
        self.redirect("/lots?id=" + lot.key.urlsafe())


# encapsulating posts into an app
app = webapp2.WSGIApplication([
    ('/comment_forms', CommentFormHandler)
], debug=True)
