import webapp2

from base_handler import BaseHandler
from posts import PostHandler
from lots import LotHandler
from models import ParkingLot

class MainHandler(BaseHandler):
    def get(self):
        template_values = {}
        url = "/posts"
        template_values = {
            'url':url
        }

        self.render("./templates/main.html", template_values)

        # add stuff to datastore here -- or use localhost:8000
        # -- make sure to comment after adding
        # lots = [
        #     ParkingLot(
        #         name = "P66",
        #         description = "Skydome",
        #         ),
        #     ParkingLot(
        #         name = "P62",
        #         description = "South Commuter"
        #     ),
        #     ParkingLot(
        #         name = "P42",
        #         description = "South of Forestry"
        #     )
        # ]
        # for lot in lots:
        #     lot.put()

# main application routing
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
