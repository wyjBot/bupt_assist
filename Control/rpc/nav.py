from flask import Blueprint
import os,sys,os.path as path
import json as js
from flask import request,redirect
from Utils.user import vrfSession
from Control.webrpc import rjs
from Navigate import build


api = Blueprint('nav_api', __name__)
@api.route('/api/nav/build',methods=['POST','GET'])
def list_res():
    data = request.get_data()
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    if not "session" in data:
      return rjs(400,"参数缺失")
    userid=vrfSession(data['session'])
    if not userid:
      return rjs(-1,"登录失效")
    if  "classid" in data:
       classid=data['classid']
    return rjs(1,build.buildings)



from Navigate import astar
from Activity.actvt import find_user_location
@api.route('/api/nav/explore',methods=['POST','GET'])
def find_route():
    data = request.get_data()
    try:
        data = js.loads(data)
        pr=data['pr']
    except:
      return rjs(400,"无效请求")
    if not "session" in data:
      return rjs(400,"参数缺失")
    userid=vrfSession(data['session'])
    if not userid:
      return rjs(-1,"登录失效")
    if data["mode"]=="b2b":
      s=data['b1']
      t=data['b2']
    if data["mode"]=="b2t":
      s=data['b']
      # print(s,data['t'],pr)
      t,mess=find_user_location(data['t'],userid)
      t=t[0]['buildId']
    data=astar.plan(s,t,pr)
    return rjs(1,data)