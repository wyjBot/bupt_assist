from flask import Blueprint
import os,sys,os.path as path
import json as js
from flask import request,redirect,make_response
from Utils.user import vrfSession
from Control.rpc.webrpc import rjs
from CourseMgmt import material as res


api = Blueprint('res_api', __name__)
@api.route('/api/res/list',methods=['POST','GET'])
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
    data,msg=res.list_user_material(userid)
    return rjs(1,data)

