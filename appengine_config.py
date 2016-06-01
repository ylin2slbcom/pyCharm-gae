# coding=utf-8
"""
`appengine_config.py` is automatically loaded when Google App Engine starts a new instance of your application.
This runs before any WSGI applications specified in app.yaml are loaded.
This file ensures that the python lib directory is added to the path. Without it, the flask module will not be found.
"""

from google.appengine.ext import vendor
# Add any libraries installed in the "lib" folder.
import os
vendor.add(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib'))

# from dlstorage import appengine_helper
# Add the correct packages path if running on Production (this is set by Google when running on GAE in the cloud)
# if appengine_helper.is_running_in_production():
#     vendor.add('venv/lib/python2.7/site-packages')