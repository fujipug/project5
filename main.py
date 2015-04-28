import webapp2

from base_handler import BaseHandler
from posts import PostHandler
from lots import LotHandler
import models

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
        lots = [
            models.ParkingLot(
                name = "P66",
                description = "Skydome",
                ),
            models.ParkingLot(
                name = "P96A",
                description = "Knoes Parking Garage",
                ),
            models.ParkingLot(
                name = "P96B",
                description = "San Fransisco Parking Garage",
                ),
            models.ParkingLot(
                name = "P62",
                description = "South Commuter"
            ),
            models.ParkingLot(
                name = "P42",
                description = "South of Forestry"
            )
        ]
        for lot in lots:
            lot.put()
        comment = models.Comment(text="testing a comment for p64")
        comment_key = comment.put()
        lot = models.ParkingLot(
            name="P64",
            description="By Faculty Services",
            comments=[comment_key]
            )
        lot.put()


# main application routing
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
