from google.appengine.ext import ndb
from parking_lot import ParkingLot
from comment import Comment


class Account(ndb.Model):
    email = ndb.StringProperty()
    parking_lots = ndb.KeyProperty(ParkingLot, repeated=True)
    comments = ndb.KeyProperty(Comment, repeated=True)
