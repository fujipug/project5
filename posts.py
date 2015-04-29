import webapp2
from google.appengine.api import users

from base_handler import BaseHandler
from models import ParkingLot

class PostHandler(BaseHandler):
    def get(self):
        template_values = {}
        favorite_lots = []
        acc = self.get_account()
        for x in acc.parking_lots:
            favorite_lots.append(x.get())

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
