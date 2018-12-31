import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State
from flask import Flask
import flask
import webbrowser
import os

#------------------------------------------------------------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
STATIC_PATH_fubar = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fubar')
STATIC_PATH_fubar_audio = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fubar', 'audio')
#------------------------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

@app.server.route('/fubar/<resource>')
def serve_static(resource):
   return flask.send_from_directory(STATIC_PATH_fubar, resource)

@app.server.route('/fubar/audio/<resource>')
def serve_static_audio(resource):
   return flask.send_from_directory(STATIC_PATH_fubar_audio, resource)
#------------------------------------------------------------------------------------------------------------------------
app.scripts.config.serve_locally = True

app.layout = html.Div([
   html.Button('Display IJAL Text', id='displayIJALTextButton', style={"margin": "20px"}),
   html.Br(),
   html.Iframe(id="storyIFrame", width=1200, height=800)
   ])

#------------------------------------------------------------------------------------------------------------------------
@app.callback(
    Output('storyIFrame', 'src'),
    [Input('displayIJALTextButton', 'n_clicks')])
def displayText(n_clicks):
   if n_clicks is None:
      return("")
   return('/fubar/test.html')

#------------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
   webbrowser.open('http://127.0.0.1:8068/', new=0, autoraise=True)
   app.run_server(host='0.0.0.0', port=8068)

#------------------------------------------------------------------------------------------------------------------------
