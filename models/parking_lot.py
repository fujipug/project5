from google.appengine.ext import ndb

class ParkingLot(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.StringProperty()
	is_full = ndb.BooleanProperty(default=False)
	date = ndb.DateTimeProperty()
