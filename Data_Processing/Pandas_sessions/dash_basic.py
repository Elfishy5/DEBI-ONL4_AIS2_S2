import pandas as pd 
import plotly.express as px 
from dash import Dash, dcc, html, Input, Output 

df = pd.read_excel("E:/Alsayad Electronics/Downloads/Dash.xlsx")
app = Dash()
app.title = 'Interactive Dashboard'
num_cols = df.select_dtypes(include = 'number').columns
app.layout = html.Div([html.H1("Interactive Dashboard with pie plot"),
                       html.Label("select a value to show in the pie chart"),
                       dcc.Dropdown(id = 'column-dropdown',
                       options = [{'label' : col, 'value':col }for col in num_cols],
                       value = num_cols[0]),
                       num_cols[0],
                       dcc.Graph(id='pie-chart')
                       ])

@app.callback(
    Output('pie-chart', 'figure'),
    Input('column-dropdown', 'value')
)
def update_graph(selected_col):

    fig = px.pie(df, values=selected_col, names=df.index, title=f'Pie Chart for {selected_col}')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
