import webapp2
from google.appengine.api import users

from base_handler import BaseHandler
from models import ParkingLot

class PostHandler(BaseHandler):
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
            # order by description, if descriptions match, then order by name
            'parking_lots': ParkingLot.query().order(ParkingLot.description, ParkingLot.name)
        }

        self.render("./templates/posts.html", template_values)

# encapsulating posts into an app
app = webapp2.WSGIApplication([
    ('/posts', PostHandler)
], debug=True)
