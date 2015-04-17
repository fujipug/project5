import os 
import webapp2
from google.appengine.ext import ndb

parking_names = ["South Comuter"]

class ParkingLotInfo(ndb.Model):
	name = ndb.StringProperty(parking_names)
	p_id = ndb.StringProperty()
	full = ndb.BooleanProperty()
	comments = ndb.StringProperty()
	datetime = DateTimeProperty()

