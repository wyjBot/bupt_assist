import sys,os.path as path
sys.path.append(path.dirname(__file__))
sys.path.append(path.dirname(path.dirname(__file__)))
import Utils
from Utils.Log import *
from Utils.Time import *
from Utils.DataFrame import *
from Utils.database import conn

"""The implementation principle of this module 
    is highly similar to CourseMgmt
    you could refer to detail annotation in CourseMgmt/interface.py
"""
tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
tbUserCourse=conn["userCourse"]
##########活动管理与查看，加入#############
def actvt_list(userId):
  ret=tbUserActvt.find_all({"userId":userId})
  if not ret:
    log("actvt_list blank",2)
    return [],"还没有加入活动"
  log("actvt_list:userId="+userId,0)
  for x in ret:
    x.pop("userId")
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
  res=tbActvt.find_all({})
  for i in range(len(res)+1):
    if tbActvt.find_one({"actvtId":i}):continue
    data["actvtId"]=i
  data["userId"]=data["InitiatorId"]
  tbActvt.insert(data)
  tbUserActvt.insert(data)
  log("actvt_create",0)
  return data["actvtId"],"成功创建活动"

def actvt_join(userId,actvtId):
  '''join a actvt created by others'''
  res=tbActvt.find_one({"actvtId":actvtId})
  if not res:
    log("actvt_join fail",2)
    return -1,"不存在该活动"
  if tbUserActvt.find_one({"userId":userId,"actvtId":actvtId}):
    log("actvt_join fail",2)
    return -2,"该活动已加入"
  if res["type"]==1:
    log("actvt_join fail",2)
    return -3,"该活动为个人活动"
  res["userId"]=userId
  tbUserActvt.insert(res)

  log("actvt_join:actvtId="+str(actvtId),0)
  return 1,"已加入集体活动"

def actvt_del(actvtId,userId=-1):
  '''delete a actvt,pay attention to check user's Permission'''
  ret=tbActvt.find_one({"actvtId":actvtId})
  if not ret:
    log("actvt_del fail",2)
    return -1,"不存在该活动"
  res=tbUserActvt.find_one({"actvtId":actvtId,"userId":userId})
  if not res:
    log("actvt_del fail",2)
    return -1,"该用户不存在该活动"
  if ret["userId"]==userId:
    tbActvt.remove(ret)
    temp=tbUserActvt.find_all({"actvtId":actvtId})
    for x in temp:
      tbUserActvt.remove(x)
  else:
    tbUserActvt.remove(res)
  log("actvt_del:actvtId="+str(actvtId),0)
  return 1,"已删除活动信息"

def actvt_update(actvtId,data):
  tbActvt.update({"actvtId":actvtId},data)
  ret=tbUserActvt.find_all({"actvtId":actvtId})
  for x in ret:
    data["userId"]=x["userId"]
    tbUserActvt.update({"actvtId":actvtId,"userId":x["userId"]},data)
  log("actvt_update:actvtId="+str(actvtId),0)
  return 1,"已更新活动信息"

if __name__ == "__main__":
  data1={
    "type":2,#1 represent personal ,2 means collective
    "name":"class meeting",
    "InitiatorId":"2020211838",
    "time":str(now()),
    "last":str(timedelta(2))
  }
  data2={
    "type":1,#1 represent personal ,2 means collective
    "name":"run",
    "InitiatorId":"2020211839",
    "time":str(now()),
    "last":str(timedelta(2)),
  }
  actvt_create(data1)
  actvt_create(data2)
  print("2020211839: ",actvt_list("2020211839"))
  actvt_join("2020211839", 0)
  print("2020211839: ",actvt_list("2020211839"))
  data3={
    "type":1,#1 represent personal ,2 means collective
    "name":"run again",
    "InitiatorId":2020211839,
    "time":str(now()),
    "last":str(timedelta(2)),
  }
  actvt_update(1, data3)
  print("2020211839: ",actvt_list("2020211839"))
  actvt_del(0,"2020211838")
  print("2020211839: ",actvt_list("2020211839"))
