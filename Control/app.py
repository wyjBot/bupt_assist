from flask import Flask,request,redirect,make_response,render_template
from flask import send_from_directory,send_file  
import sys,os.path as path
sys.path.append('..')
import time,random,sys,os,shutil
import json as js
import numpy as np
from multiprocessing import Process
from Utils.Log import log 
from Utils.database import conn
from Utils.Cfg import cfg
from datetime import datetime,timedelta
from flask_cors import *
from Control.user import user_api
from Control.crouse import api as crouse_api
sys.path.append(path.dirname(path.dirname(__file__)))

app = Flask(__name__,template_folder='')
app.register_blueprint(user_api)
app.register_blueprint(crouse_api)
CORS(app, supports_credentials=True)


if __name__ == '__main__':
    # print(conn)
    app.run(debug=True,port=1024,host="0.0.0.0")
