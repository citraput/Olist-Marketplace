# from werkzeug.wsgi import DispatcherMiddleware

# from flask_app import flask_app
# from app1 import app as app1
# # from app2 import app as app2

# application = DispatcherMiddleware(flask_app, {
#     '/app1': app1.server,
#     # '/app2': app2.server,
# })

from werkzeug.wsgi import DispatcherMiddleware

from flask_app import flask_app
from aboutolist import app as app1
from nextpurchase import app as app2
from dataviz import app as app3
from analytics import app as app4
# from app1 import app as app1
# from app2 import app as app2

application = DispatcherMiddleware(flask_app, {
    '/about-olist': app1.server,
    '/prediction': app2.server,
    '/data-visualization': app3.server,
    '/data-analytics': app4.server
})