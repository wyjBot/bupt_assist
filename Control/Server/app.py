from flask import Flask,request,redirect,make_response,render_template
from flask import send_from_directory,send_file  
import os.path as path
import time,random,sys,os,shutil
import json as js
import numpy as np
from multiprocessing import Process
sys.path.append('.')
from Utils.Log import log 
from Utils.Database import conn
from datetime import datetime,timedelta
from login import *

app = Flask(__name__,template_folder='')



if __name__ == '__main__':
    loadCfg()
    print(conn)
    app.run(debug=True,port=1024,host="0.0.0.0")
