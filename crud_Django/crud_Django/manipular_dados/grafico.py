from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import sqlite3

app = Dash(__name__)


conn = sqlite3.connect('db.sqlite3')
query = "SELECT * FROM app_empresa"
df = pd.read_sql_query(query, conn)

fig = px.bar(df, x="funcionarios", y="nome_setor", color="id", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='app_empresa',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
