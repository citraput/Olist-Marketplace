import pandas as pd
import dash 
import dash_html_components as html 
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

# server = flask.Flask(__name__)

# Bootstrap/CSS
external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__, 
    requests_pathname_prefix='/about-olist/',
    external_stylesheets=external_stylesheets
)

# app2 = dash.Dash(
#     __name__,
#     server=server,
#     url_base_pathname='/prediction/'
# )

navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("About Olist", active=True, href="http://localhost:8050/about-olist/")),
        dbc.NavItem(dbc.NavLink("Predict Next Purchase", href="http://localhost:8050/prediction/")),
        dbc.NavItem(dbc.NavLink("Data Visualization", href="http://localhost:8050/data-visualization/")),
        dbc.NavItem(dbc.NavLink("Data Analytics", href="http://localhost:8050/data-analytics/"))
    ],
        pills=True,
        style={
            'font-size': '20px',
            'padding-left': '100px'
        }
)
olist = './module-3/Project Akhir/olist.png' # replace with your own image
olist_exp = 'module-3/Project Akhir/olist_exp.png'
encoded_olist = base64.b64encode(open(olist, 'rb').read())
encoded_olist_exp = base64.b64encode(open(olist_exp, 'rb').read())

# app.layout = html.Div([
#     html.Img(src='data:image/png;base64,{}'.format(encoded_image))
# ])

row_new = dbc.Row(
    [
        dbc.Col(
            html.Div(
                children=[
                    html.H1("Olist Marketplace", style={'font-size': '50px', 'margin-left': '200px'}),
                    html.Hr(style={"width": "50%"}),
                    html.Img(src='data:image/png;base64,{}'.format(encoded_olist.decode()), style={'width': '150px', 'margin-left': '350px', 'margin-top': '10px', 'margin-bottom': '30px'}),
                    html.P("The Olist is a large online marketplaces, formed by thousands of stores throughout Brazil.", style={'padding-left': '200px', 'font-size': '23px'}), 
                    html.Ul(
                        children=[
                        html.Li("Industry: Marketplace"),
                        html.Li("Founded: 2015"),
                        html.Li("Headquarter: Curitiba, Latin America"),
                        
                        html.Li(children=[
                            "Website: ",
                            dcc.Link("Olist.com", href='www.olist.com')
                        ]
                        ),
                        
                        html.Li("Founder: Tiago Dalvi"),
                        ],
                        style={'margin-left': '200px', 'font-size': '20px', 'padding-bottom': '50px'}
                    )
                ],
                style={'background-color': '#EEEEEE'}
            ),

            width=6
        ),
        dbc.Col(
            html.Div(
                children=[
                # html.P("Test"),
                # html.H1("Olist Marketplace", style={'font-size': '50px', 'margin-left': '200px'}), 
                html.Img(src='data:image/png;base64,{}'.format(encoded_olist_exp.decode()), style={'width': '80%', 'margin-left': '10px', 'margin-top': '10px', 'margin-bottom': '30px'}),
                ]
            ),
            width=6
            ),
    ]
)


# app.layout = html.Div()

# app.layout = html.Div(children=[
#     html.Div(className='row',
#             children=[
#                 html.Div(className='four columns div-user-controls'),
#                 html.Div(className='eight columns div-for-charts bg-grey')

#             ])
# ])

# app.layout = html.Div(children=[
#     html.Div(className='row',
#             children=[
#                 html.Div(className='four columns div-user-controls'),
#                 html.Div(className='eight columns div-for-charts bg-grey')

#             ])
# ])

# app.layout = html.Div([
#     html.H1("Olist Dashboards", style={"text-align": "center"})
# ])

app.layout = html.Div(
    [   
        html.H1("Olist Dashboard", style={'text-align': 'center', 'padding': '20px', 'font-size': '30px'}),
        html.Hr(),
        html.Div(),
        navbar,
        html.Hr(),
        html.Div(style={'padding-top': '10px'}),
        row_new
        # [navbar], style={'backgroundColor':'black'}
    ]
    )

# if __name__ == '__main__':
#     app.run_server(debug=True)

