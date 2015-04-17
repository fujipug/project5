from google.appengine.ext.webapp import template
from google.appengine.api import users

import webapp2

class LotHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = "Sign out"
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = "Sign In"
        template_values ={
            'user': user,
            'url': url,
            'url_linktext':url_linktext
        }

        self.response.out.write(template.render("./templates/lots.html", template_values))

app = webapp2.WSGIApplication([
    ('/lots', LotHandler)
], debug=True)
