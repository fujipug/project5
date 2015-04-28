import webapp2

from base_handler import BaseHandler
from posts import PostHandler
from lots import LotHandler

class MainHandler(BaseHandler):
    def get(self):
        template_values = {}
        url = "/posts"
        template_values = {
            'url':url
        }

        self.render("./templates/main.html", template_values)

# main application routing
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
