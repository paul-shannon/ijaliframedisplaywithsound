import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, Event, State
from flask import Flask
import flask
import webbrowser
import os
import pdb
#------------------------------------------------------------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#------------------------------------------------------------------------------------------------------------------------
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

@app.server.route('/PROJECTS/<path:urlpath>')
def serve_static_file(urlpath):
   print("--- serve_static_file")
   print("urlpath:  %s" % urlpath)
   fullPath = os.path.join("PROJECTS", urlpath)
   dirname = os.path.dirname(fullPath)
   filename = os.path.basename(fullPath)
   print("about to send %s, %s" % (dirname, filename))
   return flask.send_from_directory(dirname, filename)

#------------------------------------------------------------------------------------------------------------------------
app.scripts.config.serve_locally = True

menu = dcc.Dropdown(id="menu",
    options=[
        {'label': 'fubar', 'value': 'fubar'},
        {'label': 'fubar2', 'value': 'fubar2'}
        ],
    value="fubar",
    style={"width": "100px", "margin": "5px"}
    )

app.layout = html.Div([
   html.Button('Display IJAL Text', id='displayIJALTextButton', style={"margin": "5px", "margin-top": "0px"}),
   menu,
   html.Br(),
   html.Iframe(id="storyIFrame", width=1200, height=800)]
   )

#------------------------------------------------------------------------------------------------------------------------
@app.callback(
    Output('storyIFrame', 'src'),
    [Input('displayIJALTextButton', 'n_clicks'),
     Input('menu', 'value')]
    )
def displayText(n_clicks, storyName):
   if n_clicks is None:
      return("")
   print("storyName: %s" % storyName)
   if(storyName == "fubar"):
      return('/PROJECTS/fubar/test.html')
   elif(storyName=="fubar2"):
      return('/PROJECTS/fubar2/daylight/test.html')

#------------------------------------------------------------------------------------------------------------------------
server = app.server

if __name__ == "__main__":
   webbrowser.open('http://127.0.0.1:8068/', new=0, autoraise=True)
   app.run_server(host='0.0.0.0', port=8068)

#------------------------------------------------------------------------------------------------------------------------
