import sys,os.path as path
sys.path.append(path.dirname(__file__))
from Utils.Time import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn

"""The implementation principle of this module 
    is highly similar to CourseMgmt
    you could refer to detail annotation in CourseMgmt/interface.py
"""
tbActvt=conn["actvt"]
tbUserActvt=conn["userActvt"]
##########活动管理与查看，加入#############
def actvt_list(userId):
  ret=tbActvt.find_all({"userId":userId})
  if not ret:return 0,"userId错误"
  return ret,"这是所有的活动"

def actvt_create(data):
  '''input data,return generated actvtId'''
  """
  data={
    "type":2,#1 represent personal ,2 means collective
    "name":"class meeting",
    "InitiatorId":2020211888,
    "time":datetime(2022,6,15,14),
    "last":timedelta(2),
  }
  "actvtId":actvtId
  """
  res=tbActvt.find_all()
  data["actvtId"]=len(res)+1
  tbActvt.insert(data)
  if data[type]==1:
    data["userId"]=data["InitiatorId"]
    tbUserActvt.insert(data)
  return data["actvtId"]

def actvt_join(userId,actvtId):
  '''join a actvt created by others'''
  res=tbActvt.find_one({"InitiatorId":userId})
  if not res:return -1,"不存在该活动"
  if tbActvt.find_one({"InitiatorId":userId,"actvtId":actvtId}):return -2,"该活动已加入"
  res["userId"]=userId
  tbUserActvt.insert(res)
  return 1,"已加入集体活动"

def actvt_del(actvtId,userId=-1):
  '''delete a actvt,pay attention to check user's Permission'''
  tbActvt.remove({"actvtId":actvtId},data)
  ret=tbUserActvt.find_all({"actvtId":actvtId})
  for x in ret:
    data["userId"]=x["userId"]
    tbUserActvt.remove({"id":classId,"userId":x["userId"]},data)
  return 1,"已更新活动信息"
  return

def actvt_update(actvtId,data):
  tbActvt.update({"actvtId":actvtId},data)
  ret=tbUserActvt.find_all({"actvtId":actvtId})
  for x in ret:
    data["userId"]=x["userId"]
    tbUserActvt.update({"id":classId,"userId":x["userId"]},data)
  return 1,"已更新活动信息"
