# only suitable for importing from app 
import os,sys,os.path as path
from app import app
from flask import request,redirect,make_response
from Utils import User



def session_vrf(serial):
  global db
  tb=db["user"]
  user=db.find_one({"session":serial})
  if user:return user
  else:return None




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
      useId=request.form['useId']
      role=request.form['role']

    except:pass

