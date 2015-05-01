import webapp2
import cgi
import models
import json
from json import JSONEncoder
from google.appengine.api import users
from google.appengine.ext import ndb

from base_handler import BaseHandler
from models import ParkingLot, Comment

from datetime import datetime, timedelta

from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2

from base_handler import BaseHandler
from models import ParkingLot, Comment


class GaeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat() if hasattr(obj, 'isoformat') else obj
        elif isinstance(obj, ndb.Key):
            return obj.get().name
        elif isinstance(obj, ndb.Model):
            return obj.to_dict()
        elif isinstance(obj, users.User):
            return obj.email()
        else:
            return json.JSONEncoder.default(self, obj)

def serialize(obj):
    return json.dumps(obj, cls=GaeEncoder)

class CommentFormHandler(BaseHandler):
    def get(self):       
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write("[")
        # pull the id parameter from the query string
        # this holds the urlsafe key for a specific parking lot
        lot_id = self.request.get('lot_id')
        lot_key = ndb.Key(urlsafe=lot_id)
        # get account
        acc = self.get_account()
        # check if lot is in favorites
        if lot_key not in acc.parking_lots:
                acc.parking_lots.append(lot_key)
                acc.put()
        # get comments on lot
        comments = Comment.query(
            Comment.lot_key == lot_key,
            # filter out any comments older than a day
            Comment.date > datetime.utcnow() - timedelta(days=1)
            ).order(-Comment.date)

        for c in comments:
            seconds_passed = (datetime.now() - c.date).total_seconds()
            passed = ""
            end = ""
            # recent is no older than 15 minutes (ie < 16 minutes)
            if seconds_passed < 60 * 16:
                c.recent = True
            # compute seconds when under a minute has passed
            if seconds_passed < 60:
                passed = str(int(seconds_passed))
                end = " seconds ago"
            # compute minutes when under an hour has passed
            elif seconds_passed < 3600:
                passed = str(int(seconds_passed / 60))
                end = " minutes ago"
                if seconds_passed < 120:
                    end = " minute ago"
            # compute hours when under a day has passed
            elif seconds_passed < 3600 * 24:
                passed = str(int(seconds_passed) / 3600)
                end = " hours ago"
                if seconds_passed < 7200:
                    end = " hour ago"
            else:
                passed = str(int(seconds_passed) / (3600*24))
                end = " days ago"
                if seconds_passed < 3600 * 48:
                    end = " day ago"
            c.time = passed + end
            self.response.out.write(serialize(c) + ",")
        self.response.out.write("{}")
        self.response.out.write("]")

    def post(self):
        lot_id = self.request.get('lot_id')
        lot_key = ndb.Key(urlsafe=lot_id)
        lot = lot_key.get()
        comment = models.Comment(
            text=self.request.get('comment'),
            atype=int(self.request.get('atype')),
            lot_key=lot_key,
            author=self.user
            )
        comment_key = comment.put()
        self.redirect("/lots?id=" + lot_key.urlsafe())


# encapsulating posts into an app
app = webapp2.WSGIApplication([
    ('/comment_forms', CommentFormHandler)
], debug=True)
