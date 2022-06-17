from flask import Blueprint
import os,sys,os.path as path
import json as js
from flask import request,redirect
from Utils.user import vrfSession
from Utils import Time
from Control.webrpc import rjs
from Schedule import interface as notice


api = Blueprint('notice_api', __name__)
@api.route('/api/notice/list',methods=['POST','GET'])
def list_n():
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
    ret,msg=notice.notice_list(userid)
    return rjs(1,ret)


@api.route('/api/notice/able',methods=['POST','GET'])
def list_a():
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
    ret,msg=notice.notice_available(userid)
    return rjs(1,ret)


@api.route('/api/notice/wk',methods=['POST','GET'])
def n_wk():
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
    ret,msg=notice.notice_work(str(Time.now()),userid)
    return rjs(1,ret)


@api.route('/api/notice/update',methods=['POST','GET'])
def n_add():
    data = request.get_data()
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    if not "session" in data:
      return rjs(400,"参数缺失")
    userid=vrfSession(data['session'])
    del data['session']
    if not userid:
      return rjs(-1,"登录失效")
    ret,msg=notice.notice_add(userid,data)
    return rjs(1,ret)
@api.route('/api/notice/del',methods=['POST','GET'])
def n_del():
    data = request.get_data()
    try:
        data = js.loads(data)
    except:
      return rjs(400,"无效请求")
    if not "session" in data:
      return rjs(400,"参数缺失")
    userId=vrfSession(data['session'])
    del data['session']
    if not userId:
      return rjs(-1,"登录失效")
    code,msg=notice.notice_del(userId,data['noticeId'])
    return rjs(code,msg)

