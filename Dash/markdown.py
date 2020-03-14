
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Markdown('''
        # 見出し１
        ## 見出し２

        - 箇条書き
        - 箇条書き
        - 箇条書き
    '''),
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'},
        ],
        value='suzuki'
    ),
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'},
        ],
        value=['suzuki','tanaka'],
        multi=True,
    ),
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'},
        ],
        value='suzuki'
    ),
    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': '佐藤', 'value': 'sato'},
            {'label': '鈴木', 'value': 'suzuki'},
            {'label': '田中', 'value': 'tanaka'},
        ],
        value=['suzuki', 'tanaka'],
    ),
    html.Label('Text Input'),
    dcc.Input(value='佐藤', type='text'),

    html.Label('Slider'),
], style={'columnCount': 3})


if __name__ == '__main__':
    app.run_server(debug=True)
