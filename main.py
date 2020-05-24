from flask import Flask
from flaskwebgui import FlaskUI #get the FlaskUI class
from flask import render_template

import sys
import os


#for background activity
from ctypes import *
import win32gui
import threading
import time
from datetime import datetime, timedelta
import win32api

app = Flask(__name__)

# Feed it the flask app instance 
ui = FlaskUI(app)

# do your logic as usual in Flask
@app.route("/")

def index():
  # return render_template('index.html')
  return "It works!" + str(os.getcwd())



# call the 'run' method
ui.run()
