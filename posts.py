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

        # get all recent comments (<16m), update the db
        comments = Comment.query(
            Comment.date > datetime.utcnow() - timedelta(minutes=16))

        for c in comments:
            lot = c.lot[0].get()
            if c.atype == 0: # parking services
                lot.cop = True
            if c.atype == 1: # full -- priority 
                lot.is_full = True
            lot.put()
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
