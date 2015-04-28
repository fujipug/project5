import jinja2
import webapp2

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

    def render(self, template_name, template_values):
        template = jinja_environment.get_template(template_name)
        self.response.out.write(template.render(template_values))
