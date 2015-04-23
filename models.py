import os 
import webapp2
from google.appengine.ext import ndb

parking_names = ["South Comuter"]

class Comment(ndb.Model):
	c_id = ndb.StringProperty()
	text = ndb.StringProperty()
	parking_lot_id = ndb.StringProperty()

class Parking_lot(ndb.Model):
	p_id = ndb.StringProperty()
	name = ndb.StringProperty()
	is_full = ndb.BooleanProperty()
	comments = ndb.KeyProperty(Comment, repeated=True)
	date = ndb.DateTimeProperty()

class Account(ndb.Model):
	email = ndb.StringProperty()
	parking_lots = ndb.KeyProperty(Parking_lot, repeated=True)
	comments = ndb.KeyProperty(Comment, repeated=True)






