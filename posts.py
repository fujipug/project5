#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.api import users

class PostHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('Hey there non criminals')
        user = users.get_current_user()
        template_values = {}
        if user:
            url = users.create_logout_url('/')
            url_linktext = "Logout"
            greeting = "See you soon"
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = "Logout"
            greeting = "Youre back!"
        template_values ={
            'greetings': greeting,
            'user': user,
            'url': url,
            'url_linktext':url_linktext
        }

        self.response.out.write(template.render("posts.html", template_values))


app = webapp2.WSGIApplication([
    ('/', PostHandler)
], debug=True)
