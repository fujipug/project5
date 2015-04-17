import webapp2
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        url = "/posts"
        template_values = {
            'url':url
        }

        self.response.out.write(template.render("./templates/main.html", template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
