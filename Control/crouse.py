from flask import Blueprint
import os,sys,os.path as path
import json as js
from flask import request,redirect,make_response
from Utils.user import vrfSession
from Control.webrpc import rjs
from CourseMgmt import course


api = Blueprint('crouse_api', __name__)
@api.route('/api/crouse/list',methods=['POST','GET'])
def list_class():
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
    data,msg=course.list_class(userid)
    return rjs(1,data)


@api.route('/api/crouse/join',methods=['POST','GET'])
def join_class():
    data = request.get_data()
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    if not "session" in data:
      return rjs(400,"参数缺失")
    user=vrfSession(data['session'])
    if not user:
      return rjs(0,"登录失效")