from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2

from base_handler import BaseHandler
from models import ParkingLot

class LotHandler(BaseHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = "Sign out"
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = "Sign In"

        lot_id = self.request.get('id')
        print(lot_id)
        lot_key = ndb.Key(urlsafe=lot_id)
        lot = lot_key.get()
        template_values ={
            'user': user,
            'url': url,
            'url_linktext':url_linktext,
            'lot': lot
        }
        self.render("./templates/lots.html", template_values)

# encapsulating lots in app
app = webapp2.WSGIApplication([
    ('/lots', LotHandler)
], debug=True)
