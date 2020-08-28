from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

from flask_app import flask_app
from aboutolist import app as app1
from nextpurchase import app as app2
from dataviz import app as app3
from analytics import app as app4
import joblib
# from app1 import app as app1
# from app2 import app as app2

app1.enable_dev_tools(debug=True, dev_tools_props_check=False)
app2.enable_dev_tools(debug=True, dev_tools_props_check=False)
app3.enable_dev_tools(debug=True, dev_tools_props_check=False)
app4.enable_dev_tools(debug=True, dev_tools_props_check=False)

application = DispatcherMiddleware(flask_app, {
    '/about-olist': app1.server,
    '/prediction': app2.server,
    '/data-visualization': app3.server,
    '/data-analytics': app4.server

})

if __name__ == '__main__':
    model = joblib.load('module-3/Project Akhir/olistModelRF')
    run_simple('localhost', 8050, application)