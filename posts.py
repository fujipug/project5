from datetime import datetime, timedelta

import webapp2
from google.appengine.api import users

from base_handler import BaseHandler
from models import ParkingLot
from models import Comment

class PostHandler(BaseHandler):
    def get(self):
        template_values = {}
        favorite_lots = []
        acc = self.get_account()
        if acc:
            for x in acc.parking_lots:
                favorite_lots.append(x.get())

        # reset all cop and is_full properties to False
        lots = ParkingLot.query()
        for lot in lots:
            lot.cop = False
            lot.is_full = False
            lot.put()

        # get all recent comments (<16m), update cop and is_full
        comments = Comment.query(
            Comment.date > datetime.utcnow() - timedelta(minutes=16))

        for c in comments:
            l = c.lot_key.get()
            print(l.is_full)
            if c.atype == 1: # full -- priority
                l.is_full = True
            if c.atype == 2: # cop present
                l.cop = True
            l.put()

        template_values ={
            'user': self.user,
            'url': self.url,
            'url_linktext':self.url_linktext,
            # order by description, if descriptions match, then order by name
            'parking_lots': ParkingLot.query().order(ParkingLot.description, ParkingLot.name),
            'favorite_lots': favorite_lots
        }

        self.render("./templates/posts.html", template_values)

# encapsulating posts into an app
app = webapp2.WSGIApplication([
    ('/posts', PostHandler)
], debug=True)
