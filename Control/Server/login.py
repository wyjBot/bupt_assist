# only suitable for importing from app 
import os,sys,os.path as path
from app import app
from flask import request,redirect,make_response
from Utils import User
from Utils import database



@app.route('/login',methods=['POST','GET'])
def login():
  sessionVrf=request.cookies.get('sessionVrf')
  if session_vrf(sessionVrf):
    return redirect("/center")
  else:
    response=make_response();  
    response.set_cookie('sessionVrf',None)  

  if request.method == 'POST':
    try:
      user_id=request.form['user_id']
      role=request.form['role']
      passwd=request.form['role']

    except:pass

