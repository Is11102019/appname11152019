import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_table.Format import Format, Scheme, Sign, Symbol

import pandas as pd

df = pd.read_excel('rsr data.xlsx', sheet_name='Sheet1')

def convertt(t):
    if t.year > 1:
        return t.strftime('%a, %b %e %Y, %I:%M %p')
    return ""

df['Latest Visit Date'] = df['Latest Visit Date'].apply(lambda t: convertt(t))

selection_store = df['Store'].unique()

dff = df[df['Store'] == df['Store'][0]]
dff = dff.transpose()
dff.reset_index(inplace=True)
dff.columns=['Attribute', 'Value']

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Div([
        dcc.Dropdown(
            id='selection-store',
            options=[{'label': i, 'value': i} for i in selection_store],
            value=df['Store'][0]
            )
        ],
        style={'width': '100%', 'display': 'inline-block'}
    ),   

    html.Div([
        html.H4(children='Store Data'),
    ]),

    html.Div([
        dash_table.DataTable(
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto'
            },
            style_as_list_view=True,
            style_cell={'fontSize':20, 'font-family':'sans-serif'},
            id='table',
            columns=[{"name": i, "id": i} for i in dff.columns],
            data=dff.to_dict('records'),
            page_size=100,
            style_data_conditional=[
                {
                    'if': {
                        'column_id': 'Value',
                        'filter_query': '{Attribute} eq "Latest Visit Date"'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                }]
        ),
    ])
])

@app.callback(
    Output('table', 'data'),
    [Input('selection-store','value')]
)
def update_table(selection_store_val):
    dff = df[df['Store'] == selection_store_val]
    dff = dff.transpose()
    dff.reset_index(inplace=True)
    dff.columns=['Attribute', 'Value']
    return dff.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)

