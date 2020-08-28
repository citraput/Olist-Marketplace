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
    requests_pathname_prefix='/data-visualization/',
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
        dbc.NavItem(dbc.NavLink("Data Visualization", active=True, href="http://localhost:8050/data-visualization/")),
        dbc.NavItem(dbc.NavLink("Data Analytics", href="http://localhost:8050/data-analytics/"))
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





app.layout = html.Div([
    html.H1("Olist Dashboard", style={'text-align': 'center', 'padding-top': '20px', 'font-size': '30px'}),
    html.Hr(),
    html.Div(),
    navbar,
    html.Hr(),
    html.Div(style={'padding-top': '10px'}),
    # Grafik Summary
    html.Div(className='row', children=[
        html.Div([
            html.P("Total Orders:"),
            html.P(f"{summary_data['Order'].values[0]}")
        ],
        style={'font-size': '24px', 'margin-left': '100px', 'text-align': 'center', 'border': '1px solid #007BFF', 'padding': '20px'}),
        
        html.Div([
            html.P("Total Customers:"),
            html.P(f"{summary_data['Customer_unique_ID'].values[0]}")
        ],
        style={'font-size': '24px', 'margin-left': '10px', 'text-align': 'center', 'border': '1px solid #007BFF', 'padding': '20px'}),

        html.Div([
            html.P("Total Products:"),
            html.P(f"{summary_data['Products'].values[0]}")
        ],
        style={'font-size': '24px', 'margin-left': '10px', 'text-align': 'center', 'border': '1px solid #007BFF', 'padding': '20px'}),

        html.Div([
            html.P("Total Cities:"),
            html.P(f"{summary_data['Cities'].values[0]}")
        ],
        style={'font-size': '24px', 'margin-left': '10px', 'text-align': 'center', 'border': '1px solid #007BFF', 'padding': '20px'}),

        html.Div([
            html.P("Total Sellers:"),
            html.P(f"{summary_data['Sellers'].values[0]}")
        ],
        style={'font-size': '24px', 'margin-left': '10px', 'text-align': 'center', 'border': '1px solid #007BFF', 'padding': '20px'}),
    ],
    style={'text-align': 'center', 'padding-left': '200px'}
    ),
    # Grafik Revenue & Customer
    html.Div(className='row', children=[
        html.Div([
            dcc.Graph(
                id='revenue',
                figure=fig_revenue)
        ], className='six columns'),
        html.Div([
            dcc.Graph(
                id='customer',
                figure=fig_customer)
        ], className='six columns'),
    ],
    style={'margin-left':'120px', 'margin-right': '80px', 'margin-top':'10px', 'text-align': 'center', 'border-bottom': '1px solid #EEEEEE'}
    ),
    # Grafik Heatmap
    html.Div(className='row', children=[
        html.Div([
            dcc.Graph(
                id='heatmap_order',
                figure=fig_heatmap_order
            )
        ]),
        html.Div([
            dcc.Graph(
                id='heatmap_revenue',
                figure=fig_heatmap_revenue
            )
        ]),
    ],
    style={'margin-left':'100px', 'text-align': 'center', 'border-bottom': '1px solid #EEEEEE'}
    ),
    html.Div(
        className='row',children=[
            html.Div(
                dcc.Graph(
                    id='top-50-products',
                    figure= px.bar(temp_6_products_revenue, x='product_category_name_english', y='revenue', labels={'product_category_name_english': 'products'}, height=800, width=1000, color='revenue', title='Top 50 Products Most Generated Revenue')
                )
            ),
            # html.Div()
        ],
        style={'margin-top': '10px', 'margin-left': '300px'}
    ),
    # Grafik Produk
    html.Div(className='row', children=[
        # html.Div([
        #     html.P('Choose State:'),
        #     dcc.Dropdown(
        #         id='state-pilih-1',
        #         options=[{'label': label_state(i), 'value': i} for i in temp_6_state['customer_state'].unique()]
        #     )
        # ], style={'margin-left': '200px', 'width': '49%', 'display': 'inline-block'}),
        
        html.Div([
            html.P('Total Products Ordered in each States', 
            style={'font-size': '24px'}
            ),
            html.P('Choose Products:'),
            dcc.Dropdown(
                id='product-pilih-1',
                options=[{'label': i, 'value': i} for i in temp_6_state['product_category_name_english'].unique()]
            )
        ], style={'margin-left': '300px', 'width': '25%', 'margin-right': '200px'}),
        html.Div([
            html.P('Top 10 Products Ordered in States', style={'font-size': '24px'}),
            html.P('Choose States:'),
            dcc.Dropdown(
                id='state-pilih-1',
                options=[{'label': label_state(i), 'value': i} for i in temp_6_state['customer_state'].unique()]
            )
        ], style={'width': '25%'})
    ]),
    html.Div(className='row', children=[
        html.Div([
            dcc.Graph(
                id='products-in-state',
                # figure=
                # hoverData={'points': [{'customedata': 'Sao Paulo'}]}
            ),
        ]),
        html.Div([
            dcc.Graph(
                id='top-products-in-state'
            )
        ])

       
    
        # dcc.Graph(

        # )
    ])


    # html.Div(className='row', children=[
    #     html.Div([
    #         dcc.Graph(
    #             id='revenue-1',
    #             figure={
    #                 'data': [
    #                     {'x': temp_1['order_date_monthyear'], 'y': temp_1['revenue'], 'type': 'line', 'name': 'revenue'}
    #                 ],
    #                 'layout': {
    #                     'title': 'Total Revenue per Month'
    #                 },
    #                 'update_xaxes': {
    #                     'tickvals': [str(i) for i in temp_1['order_date_monthyear'].nunique()] 
    #                 }

    #             }
    #         )
    #     ], 
    #     style={'width': '49%', 'display': 'inline-block'}
    #     ),

    #     html.Div([
    #         dcc.Graph(
    #             id='revenue-2',
    #             figure={
    #                 'data': [
    #                     {'x': temp_1['order_date_monthyear'], 'y': temp_1['revenue'], 'type': 'line', 'name': 'revenue2'}
    #                 ],
    #                 'layout': {
    #                     'title': 'Total Revenue per Month'
    #                 }
    #             }
    #         )
    #     ])
    #     ]
    # )
])

@app.callback(
    Output('products-in-state', 'figure'),
    [Input('product-pilih-1', 'value')]
)
def update_graph_state_products(product):
    
    fig_map = go.Figure()
    fig_map.add_trace(go.Scattergeo(
        lon=temp_6_state[temp_6_state.product_category_name_english == product]['customer_lng'],
        lat=temp_6_state[temp_6_state.product_category_name_english== product]['customer_lat'],
        mode='markers',
        text = temp_6_state[temp_6_state.product_category_name_english== product][['order_id', 'customer_state']],
        marker_color = temp_6_state[temp_6_state.product_category_name_english == product]['order_id'],
        marker=dict(
            size=8,
            opacity=0.8,
            reversescale=True,
            autocolorscale=False,
            colorscale='Blues',
            cmin=temp_6_state[temp_6_state.product_category_name_english == product]['order_id'].min(),
            color=temp_6_state[temp_6_state.product_category_name_english == product]['order_id'],
            cmax=temp_6_state[temp_6_state.product_category_name_english == product]['order_id'].max(),
            colorbar_title="Total Order"
        )
    ))
    fig_map.update_layout(
        geo_scope='south america',
        width=800,
        height=800,
        title={
            'text':f'Total products {product} ordered',
            'x':0.5, 
            'xanchor':'center', 
            'y':0.1, 
            'yanchor':'top'
        }
    )
    return fig_map
    # data = []
    # pass
@app.callback(
    Output('top-products-in-state', 'figure'),
    [Input('state-pilih-1', 'value')]
)
def top_20_products(state):
    temp = temp_6_state[temp_6_state.customer_state == state][['product_category_name_english', 'order_id']].sort_values(by='order_id', ascending=False).head(10)
    fig_top_20 = px.bar(temp, x='product_category_name_english', y='order_id', title=f'Top 10 Products Ordered in {label_state(state)}', height=800, labels={'order_id': 'Total Order', 'product_category_name_english': 'Products Category'})
    return fig_top_20
# app.layout = html.Div([
#     dcc.Graph(id='map-with-slider'),
#     dcc.Slider(
#         id='year-slider',
#         min=2016,
#         max=2018,
#         step=1,
#         marks={year: str(year) for year in state_revenue['order_date_year'].unique()}
#     )
# ])

# @app.callback(
#     Output('map-with-slider', 'figure'),
#     [Input('year-slider', 'value')])
# def map_from_csv(year):
#     data = [
#         go.Scattergeo(
#             lat=state_revenue.loc[state_revenue['order_date_year'] <= year, 'customer_lat'],
#             lon=state_revenue.loc[state_revenue['order_date_year'] <= year, 'customer_lng']
#         )
#     ]
#     layout = go.Layout(
#         title='Total Revenue in {}'.format(str(year)),
#         geo=dict(
#             scope='south america',
#             showland=True
#         )

#     )


## ADVANCE
# df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')

# available_indicators = df['Indicator Name'].unique()

# app.layout = html.Div([
#     html.H1("Olist Dashboard", style={'text-align': 'center', 'padding': '20px', 'font-size': '30px'}),
#     html.Hr(),
#     html.Div(),
#     navbar,
#     html.Hr(),
#     html.Div(style={'padding-top': '10px'}),
#     html.Div([
        # Dropdown and radioitems kiri
#         html.Div([
#             dcc.Dropdown(
#                 id='crossfilter-xaxis-column',
#                 options=[{'label': i, 'value': i} for i in available_indicators],
#                 value='Fertility rate, total (births per woman)'
#             ),
#             dcc.RadioItems(
#                 id='crossfilter-xaxis-type',
#                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                 value='Linear',
#                 labelStyle={'display': 'inline-block'}
#             )
#         ],
#         style={'width': '49%', 'display': 'inline-block'}),
            # dropdown dan radio item kanan
#         html.Div([
#             dcc.Dropdown(
#                 id='crossfilter-yaxis-column',
#                 options=[{'label': i, 'value': i} for i in available_indicators],
#                 value='Life expectancy at birth, total (years)'
#             ),
#             dcc.RadioItems(
#                 id='crossfilter-yaxis-type',
#                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                 value='Linear',
#                 labelStyle={'display': 'inline-block'}
#             )
#         ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'})
#     ], style={
#         'borderBottom': 'thin lightgrey solid',
#         'backgroundColor': 'rgb(250, 250, 250)',
#         'padding': '10px 5px'
#     }),
    # Graph
#     html.Div([
#         dcc.Graph(
#             id='crossfilter-indicator-scatter',
#             hoverData={'points': [{'customdata': 'Japan'}]}
#         )
#     ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
#     html.Div([
#         dcc.Graph(id='x-time-series'),
#         dcc.Graph(id='y-time-series'),
#     ], style={'display': 'inline-block', 'width': '49%'}),

#     html.Div(dcc.Slider(
#         id='crossfilter-year--slider',
#         min=df['Year'].min(),
#         max=df['Year'].max(),
#         value=df['Year'].max(),
#         marks={str(year): str(year) for year in df['Year'].unique()},
#         step=None
#     ), style={'width': '49%', 'padding': '0px 20px 20px 20px'})
# ])


# @app.callback(
#     dash.dependencies.Output('crossfilter-indicator-scatter', 'figure'),
#     [dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
#      dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
#      dash.dependencies.Input('crossfilter-xaxis-type', 'value'),
#      dash.dependencies.Input('crossfilter-yaxis-type', 'value'),
#      dash.dependencies.Input('crossfilter-year--slider', 'value')])
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type,
#                  year_value):
#     dff = df[df['Year'] == year_value]

#     fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
#             y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
#             hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name']
#             )

#     fig.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

#     fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'Linear' else 'log')

#     fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'Linear' else 'log')

#     fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

#     return fig


# def create_time_series(dff, axis_type, title):

#     fig = px.scatter(dff, x='Year', y='Value')

#     fig.update_traces(mode='lines+markers')

#     fig.update_xaxes(showgrid=False)

#     fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')

#     fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom',
#                        xref='paper', yref='paper', showarrow=False, align='left',
#                        bgcolor='rgba(255, 255, 255, 0.5)', text=title)

#     fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})

#     return fig


# @app.callback(
#     dash.dependencies.Output('x-time-series', 'figure'),
#     [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
#      dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
#      dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
# def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
#     country_name = hoverData['points'][0]['customdata']
#     dff = df[df['Country Name'] == country_name]
#     dff = dff[dff['Indicator Name'] == xaxis_column_name]
#     title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
#     return create_time_series(dff, axis_type, title)


# @app.callback(
#     dash.dependencies.Output('y-time-series', 'figure'),
#     [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
#      dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
#      dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
# def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
#     dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
#     dff = dff[dff['Indicator Name'] == yaxis_column_name]
#     return create_time_series(dff, axis_type, yaxis_column_name)
