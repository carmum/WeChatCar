# coding: utf-8

import sae

from myapp import app

application = sae.create_wsgi_app(app)
