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
            # models.ParkingLot(
            #     name = "P13",
            #     description = "Cline Library"
            # ),
            # models.ParkingLot(
            #     name = "P13B",
            #     description = "Ponderosa"
            # ),
            # models.ParkingLot(
            #     name = "P46",
            #     description = "Forestry/Nursing"
            # ),
            # models.ParkingLot(
            #     name = "P62",
            #     description = "South Commuter"
            # ),
            # models.ParkingLot(
            #     name = "P62A",
            #     description = "South Commuter"
            # ),
            # models.ParkingLot(
            #     name = "P62B",
            #     description = "South Commuter"
            # ),
            # models.ParkingLot(
            #     name = "P64",
            #     description = "Facility Services",
            # ),
            # models.ParkingLot(
            #     name = "P65",
            #     description = "Skydome Side Lot"
            # ),
            # models.ParkingLot(
            #     name = "P66",
            #     description = "Skydome"
            # ),
            # models.ParkingLot(
            #     name = "P69A",
            #     description = "Greenhouse Complex"
            # ),
            # models.ParkingLot(
            #     name = "P96A",
            #     description = "Knoles Parking Garage",
            # ),
            # models.ParkingLot(
            #     name = "P96B",
            #     description = "San Francisco Parking Garage",
            # ),
        ]
        # for lot in lots:
        #     lot.put()
        # comment = models.Comment(text="testing a comment for p64")
        # comment_key = comment.put()
        # lot = models.ParkingLot(
        #     name="P64",
        #     description="Facility Services",
        #     comments=[comment_key]
        #     )
        # lot.put()


# main application routing
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
