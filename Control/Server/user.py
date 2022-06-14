# only suitable for importing from app 
from flask import Blueprint
import os,sys,os.path as path
import json as js
import webrpc
from flask import request,redirect,make_response
from Utils import User
from Utils import Database
from Utils.User import vrfSession


user_api = Blueprint('user_api', __name__)
@user_api.route('/api/signin',methods=['POST','GET'])
def login():
    data = request.get_data()
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    if "session" in data and vrfSession(data['session']):
      return rjs(1,data["session"])
    try:
      parm=set(["act","pwd"])
      if not parm.issubset(data):return "参数错误"
      flag,res=User.sign_in(data["act"],data["pwd"])
      return rjs(flag,res)
    except Exception as e: # raise e
      return rjs(400,"账户名或密码错误")

      
@user_api.route('/api/signup',methods=['POST','GET'])
def signup():
    data = request.get_data()
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    try:
      parm=set(["act","pwd","role","name","phone"])
      if not parm.issubset(set(data)):return rjs(400,"参数不足")
      flag,res=User.sign_up(data["act"],data["pwd"],data["role"],data["name"],data["phone"])
      return rjs(flag,res)
    except Exception as e: # raise e
      return rjs(400,"注册失败,请联系系统管理员")



