import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1', type='text', value='Input 1'),
    dcc.Input(id='input-2', type='text', value='Input 2'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-div')
])

@app.callback(
    Output('output-div', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('input-1', 'value'), State('input-2', 'value')]
)
def update_output(n_clicks, input1, input2):
    return f'El botón ha sido presionado {n_clicks} veces, y los inputs tienen los valores: {input1} y {input2}.'

if __name__ == '__main__':
    app.run_server(debug=True)