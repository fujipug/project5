from google.appengine.ext import ndb

class Comment(ndb.Model):
    text = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)
