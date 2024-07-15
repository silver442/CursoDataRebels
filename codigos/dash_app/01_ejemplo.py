import dash
from dash import html, dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H6("Escribe algo en el campo de texto:"),
    dcc.Input(id='my-id', value='texto inicial', type='text'),
    html.Div(id='my-div')
])

@app.callback(
    Output(component_id='my-div', component_property='children'),
    Input(component_id='my-id', component_property='value')
)
def update_output_div(input_value):
    return 'Has introducido: "{}"'.format(input_value)

if __name__ == '__main__':
    app.run_server(debug=True)