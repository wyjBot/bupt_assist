from flask import Blueprint
import os,sys,os.path as path
import json as js
from flask import request,redirect,make_response
from Utils.user import vrfSession
from Control.webrpc import rjs
from CourseMgmt import homework as hmwk


api = Blueprint('hmwk_api', __name__)
@api.route('/api/hmwk/list',methods=['POST','GET'])
def list_hwmk():
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
    data,msg=hmwk.list_user_task(userid)
    return rjs(1,data)


@api.route('/api/hmwk/update',methods=['POST','GET'])
def update_hwmk():
    data = request.get_data()
    # file=request.files.get("attach")
    file=request.files.get("panel.vue")
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    if not "session" in data:
      return rjs(400,"参数缺失")
    userid=vrfSession(data['session'])
    if not userid:
      return rjs(-1,"登录失效")
    if  "file" in data:
      print(file)
      return rjs(1,data["file"])
