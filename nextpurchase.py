import pandas as pd
import dash 
import dash_html_components as html 
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
import flask
import numpy as np
import joblib
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple

# Bootstrap/CSS
external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP]

app = dash.Dash(
    __name__, 
    requests_pathname_prefix='/prediction/',
    external_stylesheets=external_stylesheets
)

# app2 = dash.Dash(
#     __name__,
#     server=server,
#     url_base_pathname='/prediction/'
# )
rfm = pd.read_csv('module-3/Project Akhir/Datasets/rfm__.csv')
navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("About Olist", href="http://localhost:8050/about-olist/")),
        dbc.NavItem(dbc.NavLink("Predict Next Purchase", active=True, href="http://localhost:8050/prediction/")),
        dbc.NavItem(dbc.NavLink("Data Visualization",  href="http://localhost:8050/data-visualization/")),
        dbc.NavItem(dbc.NavLink("Data Analytics", href="http://localhost:8050/data-analytics/"))
    ],
        pills=True,
        style={
            'font-size': '20px',
            'padding-left': '100px'
        }
)

row = html.Div(
    [
        dbc.Row(
            dbc.Col(
                html.Div("A single, half-width column"),
                width={"size": 6, "offset": 3},
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Div("The last of three columns"),
                    width={"size": 3, "order": "last", "offset": 1},
                ),
                dbc.Col(
                    html.Div("The first of three columns"),
                    width={"size": 3, "order": 1, "offset": 2},
                ),
                dbc.Col(
                    html.Div("The second of three columns"),
                    width={"size": 3, "order": 12},
                ),
            ]
        ),
    ]
)

style = {'padding': '1.5em'}
app.layout = html.Div(
    [   
        html.H1("Olist Dashboard", style={'text-align': 'center', 'padding': '20px', 'font-size': '30px'}),
        html.Hr(),
        html.Div(),
        navbar,
        html.Hr(),
        html.Div(style={'padding-top': '10px'}),
        html.Div(children=[
            dcc.Markdown("""
                Predict Next Purchase based on:
                Difference Day of Purchase,
                Recency,
                Frequency,
                Monetary,
                Segment
            """, style={'font-size': '20px', 'padding': '1.5em'}),
            
            html.Div([
                dcc.Markdown("Difference Day of Purchase"),
                dcc.Slider(
                    id='diffday',
                    min=0,
                    max=360,
                    step=1,
                    value=30,
                    tooltip=dict(always_visible=True)
                    # marks={n:str(n) for n in range(0, 361, 1)}
                )
            
            ], style={'font-size': '15px', 'padding': '1.5em'}),
            html.Div([
                dcc.Markdown("Recency Value"),
                dcc.Slider(
                    id='recency',
                    min=0,
                    max=360,
                    step=1,
                    value=30,
                    updatemode='drag',
                    tooltip=dict(always_visible=True, placement='bottomLeft')
                    # marks={n:str(n) for n in range(0, 361, 1)}
                )
            ], style={'font-size': '15px', 'padding': '1.5em'}),
            html.Div([
                dcc.Markdown("Frequency Value"),
                dcc.Slider(
                    id='frequency',
                    min=1,
                    max=25,
                    step=1,
                    value=1,
                    updatemode='drag',
                    marks={n: str(n) for n in range(1, 26, 1)}
                )
            ], style={'font-size': '15px', 'padding': '1.5em'}),
            html.Div([
                dcc.Markdown("Monetary Value (R$)"),
                dcc.Input(
                    id='monetary',
                    placeholder='Enter Monetary Value',
                    type='number',
                    value='200'
                ) 

            ], style={'font-size': '15px', 'padding': '1.5em'}),
            html.Div([
                dcc.Markdown("Segment Customer"),
                dcc.RadioItems(
                    id='segment',
                    options=[
                        {'label': 'High-Tier Customer', 'value': 'high'},
                        {'label': 'Middle-Tier Customer', 'value': 'middle'},
                        {'label': 'Low-Tier Customer', 'value': 'low'}
                    ],
                    value='high'
                )  
            ], style={'font-size': '15px', 'padding': '1.5em'}),
            html.Div(
                html.P("Customer Class Prediction:",
                style={'font-size': '20px', 'padding': '2em'})
            ),
            html.Div(
                children=[
                    html.Div(id='output', style={'fontWeight': 'bold', 'font-size': '20px', 'padding': '2em'})
                    
                ]
            )
        ]
        )

        # row_new
        # [navbar], style={'backgroundColor':'black'}
    ]
    )

# if __name__ == '__main__':
#     app.run_server(debug=True)


# layout = html.Div([
#     dcc.Markdown("""
#         ### Predict
#         Use the controls below to update your predicted offer, based on city,
#         beds, baths, number of offers, and list price.
#     """),
# html.Div(id='prediction-content', style={'fontWeight': 'bold'}),
# html.Div([
#         dcc.Markdown('###### Area'),
#         dcc.Dropdown(
#             id='area',
#             options=[{'label': city, 'value': city} for city in cities],
#             value=cities[10]
#         ),
#     ], style=style),
# html.Div([
#         dcc.Markdown('###### Bedrooms'),
#         dcc.Slider(
#             id='bedrooms',
#             min=1,
#             max=7,
#             step=1,
#             value=3,
#             marks={n: str(n) for n in range(1, 7, 1)}
#         ),
#     ], style=style),
# html.Div([
#         dcc.Markdown('###### Baths'),
#         dcc.Slider(
#             id='baths',
#             min=1,
#             max=9,
#             step=1,
#             value=2,
#             marks={n: str(n) for n in range(1, 9, 1)}
#         ),
#     ], style=style),
# html.Div([
#         dcc.Markdown('###### Number of Offers'),
#         dcc.Slider(
#             id='offers',
#             min=2,
#             max=15,
#             step=1,
#             value=3,
#             marks={n: str(n) for n in range(2, 15, 1)}
#         ),
#     ], style=style),
# html.Div([
#         dcc.Markdown('###### Listing Price'),
#         dcc.Slider(
#             id='list_price',
#             min=1000000,
#             max=3000000,
#             step=100000,
#             value=1500000,
#             marks={n: f'{n/1000:.0f}k' for n in range(1000000, 3000000, 100000)}
#         ),
#     ], style=style),
# ])

@app.callback(
    Output('output', 'children'),
    [Input('diffday', 'value'),
     Input('recency', 'value'),
     Input('frequency', 'value'),
     Input('monetary', 'value'),
     Input('segment', 'value')
    ]
     )
def predict(diffday, recency, frequency, monetary, segment):
    rfm_quintiles = rfm[['recency', 'monetary']].quantile([0.2, 0.4, 0.6, 0.8])
    x1 = int(diffday)
    x2 = int(recency)
    x3 = int(frequency)
    x4 = int(monetary)

    def recency_score(x):
        q1 = rfm_quintiles.loc[0.2, 'recency']
        q2 = rfm_quintiles.loc[0.4, 'recency']
        q3 = rfm_quintiles.loc[0.6, 'recency']
        q4 = rfm_quintiles.loc[0.8, 'recency']
        
        if x <= q1:
            return 5
        elif q1 < x <= q2:
            return 4
        elif q2 < x <= q3:
            return 3
        elif q4 < x <= q4:
            return 2
        else:
            return 1
    r_score = recency_score(int(recency))

    def frequency_score(x):
        q = np.quantile(rfm.frequency.unique(), [0.2, 0.4, 0.6, 0.8])
        if x <= q[0]:
            return 1
        elif q[0] < x <= q[1]:
            return 2
        elif q[1] < x <= q[2]:
            return 3
        elif q[2] < x <= q[3]:
            return 4
        else:
            return 5
    f_score = frequency_score(int(frequency))

    def monetary_score(x, col):
        q1 = rfm_quintiles.loc[0.2, col]
        q2 = rfm_quintiles.loc[0.4, col]
        q3 = rfm_quintiles.loc[0.6, col]
        q4 = rfm_quintiles.loc[0.8, col]
        
        if x <= q1:
            return 1
        elif q1 < x <= q2:
            return 2
        elif q2 < x <= q3:
            return 3
        elif q4 < x <= q4:
            return 4
        else:
            return 5

    m_score = monetary_score(int(monetary), 'monetary')

    rfm_total_score = r_score + f_score + m_score

    high_tier = 0
    medium_tier = 0
    low_tier = 0

    if segment == 'high':
        high_tier = 1
    elif segment == 'medium':
        medium_tier = 1
    else:
        low_tier = 1


    pipeline = joblib.load('module-3/Project Akhir/olistModelRF')
    y_pred = pipeline.predict([[diffday, recency, frequency, monetary, r_score, f_score, m_score, rfm_total_score, high_tier, medium_tier, low_tier]])

    return y_pred
    # return 'You have selected "{} {} {} {} {} {}"'.format(diffday, recency, frequency, monetary, segment, result)
    # return str(diffday[0])
    # return '20'

#     pipeline = joblib.load('module-3/Project Akhir/olistModelRF')
#     y_pred_log = pipeline.predict(df)
#     y_pred = y_pred_log[0]
#     percent_over = ((y_pred - list_price) / list_price) * 100
#     per_offer = percent_over / offers
#     results = f'The predicted winning bid is ${y_pred:,.0f} which is {percent_over:.2f}% over the asking price or \
#                 {per_offer:.2f}% per offer.'
#     return results