from flask import Blueprint
import os,sys,os.path as path
import json as js
from flask import request,redirect,make_response
from Utils.user import vrfSession
from Control.webrpc import rjs
from crouse import homework as hmwk


api = Blueprint('task_api', __name__)
@api.route('/api/task/submit',methods=['POST','GET'])
def submit():
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
    print(data)