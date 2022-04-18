from flask import Flask,request,redirect,make_response,render_template
from flask import send_from_directory,send_file  
import os.path as path
import time,random,sys
from datetime import datetime,timedelta

app = Flask(__name__,template_folder='')

if __name__ == '__main__':
    app.run(debug=True,port=19268,host="0.0.0.0")
