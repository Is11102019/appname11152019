import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_table.Format import Format, Scheme, Sign, Symbol
import pandas as pd

selection_store = ['Option A', 'Option B', 'Option C']

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([

    html.Div([
        dcc.Dropdown(
            id='selection-store',
            options=[{'label': i, 'value': i} for i in selection_store],
            value='Option B'
            )
        ],
        style={'width': '100%', 'display': 'inline-block'}
    ),   

    html.Div([
        html.H4(children='Store Data'),
    ]),
    
])

if __name__ == '__main__':
    app.run_server(debug=True)

