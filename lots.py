from datetime import datetime, timedelta

from google.appengine.api import users
from google.appengine.ext import ndb
import webapp2

from base_handler import BaseHandler
from models import ParkingLot, Comment

class LotHandler(BaseHandler):
    def get(self):

        # pull the id parameter from the query string
        # this holds the urlsafe key for a specific parking lot
        lot_id = self.request.get('id')
        lot_key = ndb.Key(urlsafe=lot_id)

        # get account
        acc = self.get_account()

        # check if lot is in favorites
        if lot_key not in acc.parking_lots:
                acc.parking_lots.append(lot_key)
                acc.put()

        # get comments on lot
        comments = Comment.query(
            Comment.lot == lot_key,
            # filter out any comments older than a day
            Comment.date > datetime.utcnow() - timedelta(days=1)
            ).order(-Comment.date)

        # these flags used for updating cop or is_full -- if we encounter just
        # one record that satisfies the time constraint (<16m)
        # then the lot is full or has a cop
        updated_full = False
        updated_cop = False
        lot = lot_key.get()
        for c in comments:
            seconds_passed = (datetime.now() - c.date).total_seconds()
            passed = ""
            end = ""
            # recent is no older than 15 minutes (ie < 16 minutes)
            if seconds_passed < 60 * 16:
                c.recent = True
                # full if the comment is a parking lot full type comment
                if c.atype == 1:
                    updated_full = True
                elif c.atype == 2:
                    updated_cop = True
            else:
                c.recent = False
            c.put()

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
            #print(diff)
        if updated_full == False:
            lot.is_full = False
        else:
            lot.is_full = True
        if updated_cop == False:
            lot.cop = False
        else:
            lot.cop = True
        lot.put()


        # get the parking lot associated with this key, then pass to template
        lot = lot_key.get()
        template_values ={
            'user': self.user,
            'url': self.url,
            'url_linktext':self.url_linktext,
            'lot': lot,
            'lot_id': lot_id,
            'comments': comments,
        }
        self.render("./templates/lots.html", template_values)

# encapsulating lots in app
app = webapp2.WSGIApplication([
    ('/lots', LotHandler)
], debug=True)
