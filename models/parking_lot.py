from google.appengine.ext import ndb
from comment import Comment

class ParkingLot(ndb.Model):
	name = ndb.StringProperty()
	description = ndb.StringProperty()
	is_full = ndb.BooleanProperty(default=False)
	comments = ndb.KeyProperty(Comment, repeated=True)
	date = ndb.DateTimeProperty()
