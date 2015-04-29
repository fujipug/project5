import jinja2
import webapp2
from google.appengine.api import users
from models import Account
import os


# setup jinja2 templating -- webapp template deprecated
jinja_environment = jinja2.Environment(
   extensions=['jinja2.ext.autoescape'],
   loader=jinja2.FileSystemLoader(
       # can add a string to this dirname for organization
       os.path.dirname(__file__)),
   autoescape=True)


class BaseHandler(webapp2.RequestHandler):

    def __init__(self, request=None, response=None):
        super(BaseHandler, self).__init__(request, response)
        self.user = users.get_current_user()
        if self.user:
            self.url = users.create_logout_url('/')
            self.url_linktext = "Sign out"
        else:
            self.url = users.create_login_url(self.request.uri)
            self.url_linktext = "Sign In"
    def get_account(self):
        user = users.get_current_user()
        if user:
            url = users.create_logout_url('/')
            url_linktext = "Sign out"

            # check if user in db
            qry = Account.query()
            acc = []
            for x in qry:
                if x.email == user.email():
                    acc = x
                    break
            # if user not in db then add it
            if not acc:
                acc = Account(email = user.email())
                acc.put()
            return acc

    def render(self, template_name, template_values):
        template = jinja_environment.get_template(template_name)
        self.response.out.write(template.render(template_values))
