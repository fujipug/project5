from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2

from base_handler import BaseHandler
from models import ParkingLot, Comment

class LotHandler(BaseHandler):
    def get(self):

        # pull the id parameter from the query string
        # this holds the urlsafe key for a specific parking lot
        lot_id = self.request.get('id')
        lot_key = ndb.Key(urlsafe=lot_id)
        # get account
        acc = self.get_account()
        # check if lot is in favorites
        if lot_key not in acc.parking_lots:
                acc.parking_lots.append(lot_key)
                acc.put()
        # get comments on lot
        comments = Comment.query(Comment.lot == lot_key).order(-Comment.date)
        # get the parking lot associated with this key, then pass to template
        lot = lot_key.get()
        template_values ={
            'user': self.user,
            'url': self.url,
            'url_linktext':self.url_linktext,
            'lot': lot,
            'lot_id': lot_id,
            'comments': comments,
        }
        self.render("./templates/lots.html", template_values)

# encapsulating lots in app
app = webapp2.WSGIApplication([
    ('/lots', LotHandler)
], debug=True)
