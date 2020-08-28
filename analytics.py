import pandas as pd
import numpy as np
import dash 
import plotly.figure_factory as ff
import dash_html_components as html 
import dash_core_components as dcc
import plotly.express as px
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import base64
import flask
from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
import os, ssl
from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
# init_notebook_mode(connected=True)
import plotly.graph_objs as go
import dash_table_experiments as dt
from operator import attrgetter
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)): 
    ssl._create_default_https_context = ssl._create_unverified_context
# from sqlalchemy import create_engine

# Bootstrap/CSS
external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP, 'https://codepen.io/amyoshino/pen/jzXypZ.css']

# Mapbox Token
mapbox_access_token = 'pk.eyJ1IjoiY2l0cmFkaWFuaSIsImEiOiJja2U1bXViaTgwNnowMnJwZDdpOHc0ZnVrIn0.oAJE0jW7TOTxCcIdz0q8GA'

app = dash.Dash(
    __name__, 
    requests_pathname_prefix='/data-analytics/',
    external_stylesheets=external_stylesheets
)

# app2 = dash.Dash(
#     __name__,
#     server=server,
#     url_base_pathname='/prediction/'
# )

navbar = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("About Olist", href="http://localhost:8050/about-olist/")),
        dbc.NavItem(dbc.NavLink("Predict Next Purchase", href="http://localhost:8050/prediction/")),
        dbc.NavItem(dbc.NavLink("Data Visualization", href="http://localhost:8050/data-visualization/")),
        dbc.NavItem(dbc.NavLink("Data Analytics", active=True, href="http://localhost:8050/data-analytics/"))
    ],
        pills=True,
        style={
            'font-size': '20px',
            'padding-left': '400px',
            'text-align': 'center'
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

# olist = './module-3/Project Akhir/olist.png' # replace with your own image
# olist_exp = 'module-3/Project Akhir/olist_exp.png'
# encoded_olist = base64.b64encode(open(olist, 'rb').read())
# encoded_olist_exp = base64.b64encode(open(olist_exp, 'rb').read())

# app.layout = html.Div([
#     html.Img(src='data:image/png;base64,{}'.format(encoded_image))
# ])

# row_new = dbc.Row(
#     [
#         dbc.Col(
#             html.Div(
#                 children=[
#                     html.H1("Olist Marketplace", style={'font-size': '50px', 'margin-left': '200px'}),
#                     html.Hr(style={"width": "50%"}),
#                     html.Img(src='data:image/png;base64,{}'.format(encoded_olist.decode()), style={'width': '150px', 'margin-left': '350px', 'margin-top': '10px', 'margin-bottom': '30px'}),
#                     html.P("The Olist is a large online marketplaces, formed by thousands of stores throughout Brazil.", style={'padding-left': '200px', 'font-size': '23px'}), 
#                     html.Ul(
#                         children=[
#                         html.Li("Industry: Marketplace"),
#                         html.Li("Founded: 2015"),
#                         html.Li("Headquarter: Curitiba, Latin America"),
                        
#                         html.Li(children=[
#                             "Website: ",
#                             dcc.Link("Olist.com", href='www.olist.com')
#                         ]
#                         ),
                        
#                         html.Li("Founder: Tiago Dalvi"),
#                         ],
#                         style={'margin-left': '200px', 'font-size': '20px', 'padding-bottom': '50px'}
#                     )
#                 ],
#                 style={'background-color': '#EEEEEE'}
#             ),

#             width=6
#         ),
#         dbc.Col(
#             html.Div(
#                 children=[
#                 # html.P("Test"),
#                 # html.H1("Olist Marketplace", style={'font-size': '50px', 'margin-left': '200px'}), 
#                 html.Img(src='data:image/png;base64,{}'.format(encoded_olist_exp.decode()), style={'width': '80%', 'margin-left': '10px', 'margin-top': '10px', 'margin-bottom': '30px'}),
#                 ]
#             ),
#             width=6
#             ),
#     ]
# )


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

# app.layout = html.Div(
#     [   
#         html.H1("Olist Dashboard", style={'text-align': 'center', 'padding': '20px', 'font-size': '30px'}),
#         html.Hr(),
#         html.Div(),
#         navbar,
#         html.Hr(),
#         html.Div(style={'padding-top': '10px'}),
#         html.P("Citra"),
#         row
#         # row_new
#         # [navbar], style={'backgroundColor':'black'}
#     ]
#     )

# if __name__ == '__main__':
#     app.run_server(debug=True)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
def label_state(x):
    if x == 'AC':
        return 'Acre'
    elif x == 'AL':
        return 'Alagoas'
    elif x == 'AP':
        return 'Amapa'
    elif x == 'AM':
        return 'Amazonas'
    elif x == 'BA':
        return 'Bahia'
    elif x == 'CE':
        return 'Ceara'
    elif x == 'GO':
        return 'Goias'
    elif x == 'ES':
        return 'Espirito Santo'
    elif x == 'MA':
        return 'Maranhao'
    elif x == 'MT':
        return 'Mato Grosso'
    elif x == 'MS':
        return 'Mato Grosso do Sul'
    elif x == 'MG':
        return 'Minas Gerasi'
    elif x == 'PA':
        return 'Para'
    elif x == 'PB':
        return 'Paraiba'
    elif x == 'PR':
        return 'Parana'
    elif x == 'PE':
        return 'Pernambuco'
    elif x == 'PI':
        return 'Piaui'
    elif x == 'RJ':
        return 'Rio de Janeiro'
    elif x == 'RN':
        return 'Rio Grande do Norte'
    elif x == 'RS':
        return 'Rio Grande do Sul'
    elif x == 'RO':
        return 'Rondonia'
    elif x == 'RR':
        return 'Roraima'
    elif x == 'SP':
        return 'Sao Paulo'
    elif x == 'SC':
        return 'Santa Catarina'
    elif x == 'SE':
        return 'Sergipe'
    elif x == 'TO':
        return 'Tocantins'
    else:
        return 'Others'

# Data
temp_9 = pd.read_csv('module-3/Project Akhir/Datasets/temp9.csv')
temp_10 = pd.read_csv('module-3/Project Akhir/Datasets/temp10.csv')
temp_11 = pd.read_csv('module-3/Project Akhir/Datasets/temp11.csv')
temp_13 = pd.read_csv('module-3/Project Akhir/Datasets/temp13.csv')



# first_timer = temp_13[temp_13['order_item_id'] == 1]['customer_unique_id'].count()
# existing = temp_13[temp_13['order_item_id'] != 1]['customer_unique_id'].nunique()
# data_temp = [first_timer, existing]
# df = pd.read_csv('module-3/Project Akhir/Datasets/olist_dataset_all.csv')
# df.drop(columns='Unnamed: 0', inplace=True)
# df['revenue'] = df['price'] + df['freight_value']
# temp_1 = df.pivot_table(index='order_date_monthyear', values='revenue', aggfunc='sum').reset_index()
summary_data = pd.read_csv('module-3/Project Akhir/Datasets/summary-beg.csv')
temp_1 = pd.read_csv('module-3/Project Akhir/Datasets/temp1.csv')
temp_2 = pd.read_csv('module-3/Project Akhir/Datasets/temp2.csv')
temp_6_products_revenue = pd.read_csv('module-3/Project Akhir/Datasets/temp6productsrevenue.csv')
# products vs state map
temp_6_state = pd.read_csv('module-3/Project Akhir/Datasets/temp6state.csv')
temp_6_state['text'] = 'Total Order produk ' + str(temp_6_state['product_category_name_english'].values) + " di " + label_state(str(temp_6_state['customer_state'].values)) + ' berjumlah ' + str(temp_6_state['order_id'].values)
temp_12 = pd.read_csv('module-3/Project Akhir/Datasets/temp12.csv')
temp_12a = pd.read_csv('module-3/Project Akhir/Datasets/temp12s.csv')
# state_revenue = pd.DataFrame(df.groupby(['customer_lat', 'customer_lng', 'order_date_year'])['revenue'].sum().reset_index())
# state_revenue['order_date_year'] = state_revenue['order_date_year'].astype(int)

# state_order = pd.DataFrame(df.groupby(['customer_state', 'order_date_year'])['order_id'].nunique().reset_index())
# state_order['order_date_year'] = state_order['order_date_year'].astype(int)

## SUMMARY


## REVENUE
# revenue_data = pd.DataFrame({
#     "x": temp_1['order_date_monthyear'],
#     "y": temp_1['revenue']
# })
fig_revenue = go.Figure()
fig_revenue.add_trace(go.Scatter(
    x=temp_1['order_date_monthyear'],
    y=temp_1['revenue'],
    mode="lines"
))
fig_revenue.update_xaxes(
    ticktext=[str(i) for i in temp_1['order_date_monthyear']],
    tickvals=[str(i) for i in temp_1['order_date_monthyear']],
)
fig_revenue.update_yaxes(tickprefix="$")
fig_revenue.update_layout(title_text="Total Revenue per Month", xaxis_title="Year-Month",
    yaxis_title="Revenue")

## TOTAL ORDER

## TOTAL CUSTOMERS
fig_customer = go.Figure()
fig_customer.add_trace(go.Scatter(
    x=temp_2['order_date_monthyear'],
    y=temp_2['customer_unique_id'],
    mode="lines"
))
fig_customer.update_xaxes(
    ticktext=[str(i) for i in temp_1['order_date_monthyear']],
    tickvals=[str(i) for i in temp_1['order_date_monthyear']],
)
# fig_customer.update_yaxes(tickprefix="$")
fig_customer.update_layout(title_text="Total Customers per Month", xaxis_title="Year-Month",
    yaxis_title="Total Customers")

## Heatmap Total Order
fig_heatmap_order = go.Figure()
fig_heatmap_order.add_trace(go.Heatmap(
    z=np.array(temp_12),
    x=temp_12.columns.values,
    y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
))
fig_heatmap_order.update_layout(
    title='Total Order per Hour and Day',
    xaxis_nticks=36,
    xaxis_title="Hour",
    yaxis_title="Day",)
fig_heatmap_order.update_yaxes(
    ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    tickvals=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
)

## Heatmap Revenue
fig_heatmap_revenue = go.Figure()
fig_heatmap_revenue.add_trace(go.Heatmap(
    z=np.array(temp_12a),
    x=temp_12a.columns.values,
    y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
))
fig_heatmap_revenue.update_layout(
    title='Revenue Generated per Hour and Day',
    xaxis_nticks=36,
    xaxis_title="Hour",
    yaxis_title="Day",)
fig_heatmap_revenue.update_yaxes(
    ticktext=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    tickvals=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
)

# Map
def label_customer(x):
    if x == True:
        return 'Existing Customers'
    else:
        return 'New Customers'

## EXISTING VS NEW CUSTOMERS
trace9 = [
    go.Scatter(
    x=temp_9[temp_9['isExisting'] == False]['MonthYear'],
    y=temp_9[temp_9['isExisting'] == False]['Revenue'],
    name = 'New Customers'
),
    go.Scatter(
        x=temp_9[temp_9['isExisting'] == True]['MonthYear'],
        y=temp_9[temp_9['isExisting'] == True]['Revenue'],
        name = 'Existing Customers'
    ),
]
trace9_layout = go.Layout(
        xaxis={
            "type": "category", 
            'title': 'Year-Month'
        },
        yaxis={
            'title':'Revenue'
        },
        title='Revenue of New Customers vs Existing Customers'
    )
fig9 = go.Figure(data=trace9, layout=trace9_layout)

## CUSTOMERS RATIO
trace10 = [
    go.Bar(
        x=temp_10['MonthYear'],
        y=temp_10['ratio'],
    )
]

trace10_layout = go.Layout(
        xaxis={"type": "category", 'title':'Year-Month'},
        title='New Customers\'s Ratio',
        yaxis={'title': 'Customer Ratio'}
    
    )
fig10 = go.Figure(data=trace10, layout=trace10_layout)

trace11 = [
    go.Scatter(
        x=temp_11['Year_Month'],
        y=temp_11['Retention_Rate'],
    ) 
]

trace11_layout = go.Layout(
        xaxis={"type": "category", 'title': 'Year-Month'},
        title='Retention Rate per Month',
        yaxis=dict(title='Retention Rate')
    )
fig11 = go.Figure(data=trace11, layout=trace11_layout)


app.layout = html.Div([
    # Dashboard
    html.H1("Olist Dashboard", style={'text-align': 'center', 'padding-top': '20px', 'font-size': '30px'}),
    html.Hr(),
    html.Div(),
    # Navbar
    navbar,
    html.Hr(),
    html.Div(style={'padding-top': '10px'}),
    html.Div(className='row', children=[
        html.P('Choose Customer Type:'),
        html.Div(
            
            dbc.Checklist(
                id='isExisting',
                options=[
                    {'label': 'Existing Customer', 'value': 'existing'},
                    {'label': 'New Customers', 'value': 'new'},
                    ],
                value=[],
                # switch=True,
                labelStyle={'display': 'inline-block'}
                
            ),
            style={'padding-left': '10px'}
            # value=['True', 'False'],
            # labelStyle={'display': 'inline-block'}
        ),
    ],
    style={'margin-left': '200px'}
    ),
    html.Div(className='row', children=[
        html.Div(
            # html.P(id='check')
            dcc.Graph(
                id='isExisting-revenue',
                figure=fig9,
            )
        ),
        html.Div(
            dcc.Graph(
                figure=px.pie(temp_13, values='Total', names='isExisting', title='Total Existing Customers VS New Customers')
            )
            # html.P('Analytics')
            # dcc.Graph(
            #     id='isExisting-totalCustomer'
            # )
        )
    ],
    style={'margin-left':'150px'}
    ),
    html.Div(className='row', children=[
        html.Div(
            dcc.Graph(
                figure=fig10
            )
        ),
        html.Div(
            html.P("New Customers's Ratio = Total of New Customers / Total of Existing Customers"),
        )
        
        # html.P("This new Customer Ratio")
        
    ],
    style={'margin-left': '150px'}),
    html.Div(className='row', children=[
        html.Div(
            dcc.Graph(
                figure=fig11
            )
        )
    ])
    
])

@app.callback(
    Output('isExisting-revenue', 'figure'),
    [Input('isExisting', 'value')]
)

def update_graph_isExisting(isExisting):
    if ('existing' in isExisting) & ('new' in isExisting):
        trace9 = [
            go.Scatter(
            x=temp_9[temp_9['isExisting'] == False]['MonthYear'],
            y=temp_9[temp_9['isExisting'] == False]['Revenue'],
            name = 'New Customers'
        ),
            go.Scatter(
                x=temp_9[temp_9['isExisting'] == True]['MonthYear'],
                y=temp_9[temp_9['isExisting'] == True]['Revenue'],
                name = 'Existing Customers'
            ),

        ]
        layout = go.Layout(
                xaxis={
                    "type": "category", 
                    'title': 'Year-Month'
                },
                yaxis={
                    'title':'Revenue'
                },
                title='Revenue of New Customers vs Existing Customers'
            )
        fig = go.Figure(data=trace9, layout=layout)
        return fig
    elif ('existing' in isExisting):
        trace9_b = [
    
            go.Scatter(
                x=temp_9[temp_9['isExisting'] == True]['MonthYear'],
                y=temp_9[temp_9['isExisting'] == True]['Revenue'],
                name = 'Existing Customers'
            ),

        ]

        layout = go.Layout(
                xaxis={
                    "type": "category", 
                    'title': 'Year-Month'
                },
                yaxis={
                    'title':'Revenue'
                },
                title='Revenue of Existing Customers per Month'
            )
        fig = go.Figure(data=trace9_b, layout=layout)
        return fig 
    elif ('new' in isExisting):
        trace9_b = [
            go.Scatter(
                x=temp_9[temp_9['isExisting'] == False]['MonthYear'],
                y=temp_9[temp_9['isExisting'] == False]['Revenue'],
                name = 'Existing Customers'
            ),

        ]

        layout = go.Layout(
                xaxis={
                    "type": "category", 
                    'title': 'Year-Month'
                },
                yaxis={
                    'title':'Revenue'
                },
                title='Revenue of New Customers per Month'
            )
        fig = go.Figure(data=trace9_b, layout=layout)
        return fig 
    else:
        trace9 = [
            go.Scatter(
            x=temp_9[temp_9['isExisting'] == False]['MonthYear'],
            y=temp_9[temp_9['isExisting'] == False]['Revenue'],
            name = 'New Customers'
        ),
            go.Scatter(
                x=temp_9[temp_9['isExisting'] == True]['MonthYear'],
                y=temp_9[temp_9['isExisting'] == True]['Revenue'],
                name = 'Existing Customers'
            ),

        ]
        layout = go.Layout(
                xaxis={
                    "type": "category", 
                    'title': 'Year-Month'
                },
                yaxis={
                    'title':'Revenue'
                },
                title='Revenue of New Customers vs Existing Customers'
            )
        fig = go.Figure(data=trace9, layout=layout)
        return fig
