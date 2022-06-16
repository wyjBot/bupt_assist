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
tbUser=conn["user"]
##########活动管理与查看，加入#############
def actvt_list(userId):
  ret=tbUserActvt.find_all({"userId":userId})
  if not ret:
    log("actvt_list blank",2)
    return [],"还没有加入活动"
  log("actvt_list:userId="+userId,0)
  for x in ret:
    x.pop("userId")
    if x["type"]==1:
      x["类型"]="私人活动"
    else:
      x["类型"]="公开活动"
    x.pop("type")
    x["地点"]=x.pop("buildId")
    x["名称"]=x.pop("name")
    x["创建者"]=x.pop("InitiatorId")
    x["开始时间"]=x.pop("time")
    x["持续时间"]=x.pop("last")
  return ret,"这是所有的活动"

def actvt_canjoin_list(userId):
  ret=tbActvt.find_all({})
  res=list()
  for x in ret:
    temp=x
    temp["userId"]=userId
    if not tbUserActvt.find_one(temp):res.append(x)
  log("actvt_canjoin_list:userId="+userId,0)
  return res,"这是可以加入的活动"

def actvt_create(data):
  '''input data,return generated actvtId'''
  """
  data={
    "type":2,#1 represent personal ,2 means collective
    "name":"class meeting",
    "InitiatorId":2020211888,
    "time":datetime(2022,6,15,14),
    "last":timedelta(2),
    "buildId":
  }
  "actvtId":actvtId
  """
  res=tbActvt.find_all({})
  for i in range(len(res)+1):
    if tbActvt.find_one({"actvtId":i}):continue
    data["actvtId"]=i
  tbActvt.insert(data)
  insertdata=data.copy()
  insertdata["userId"]=insertdata["InitiatorId"]
  flag=actvt_conflict(insertdata["InitiatorId"], i)
  tbUserActvt.insert(insertdata)
  log("actvt_create",0)
  if flag==0:return data["actvtId"],"成功创建活动,无冲突活动或课程"
  return data["actvtId"],"成功创建活动,有冲突活动或课程"

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
  flag=actvt_conflict(userId, actvtId)
  tbUserActvt.insert(res)

  log("actvt_join:actvtId="+str(actvtId),0)
  if flag==0:return 1,"已加入集体活动,无冲突活动或课程"
  return 1,"已加入集体活动,有冲突活动或课程"

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
  if ret["InitiatorId"]==userId:
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

def actvt_conflict(userId,actvtId):#1有冲突，0无冲突
  res=tbUserActvt.find_all({"userId":userId})
  ret=tbActvt.find_one({"actvtId":actvtId})
  lasttimeret=lasttotimedelta(ret["last"])
  for x in res:#活动检测
    time1=datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S")
    time2=datetime.strptime(ret["time"], "%Y-%m-%d %H:%M:%S")
    if time1.__le__(time2):
      lasttime=lasttotimedelta(x["last"])
      time1=time1+lasttime
      if time1.__le__(time2):continue
      return 1
    else:
      time2=time2+lasttimeret
      if time1.__le__(time2):return 1
  timeact=datetime.strptime(ret["time"], "%Y-%m-%d %H:%M:%S")#计算星期几
  dayact=timeact.weekday()
  rex=tbUserCourse.find_all({"userId":userId,"星期":dayact})
  temptime=str(timeact.date())+" 08:00:00"
  for x in rex:#课程检测
    time1=datetime.strptime(temptime, "%Y-%m-%d %H:%M:%S")
    time1=time1+timedelta(minutes=(45*(x["节次"]-1)))
    time2=timeact
    if time1.__le__(time2):
      time1=time1+timedelta(minutes=(45*x["时长"]))
      if time1.__le__(time2):continue
      return 1
    else:
      time2=time2+lasttimeret
      if time1.__le__(time2):return 1
  return 0

def find_user_location(timein,userId):#通过时间找用户位置
  res=tbUserActvt.find_all({"userId":userId})
  timestr=str(timein)[0:19]
  time=datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
  for x in res:#活动检测
    time1=datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S")
    if time1.__le__(time2):
      lasttime=lasttotimedelta(x["last"])
      time1=time1+lasttime
      if time1.__le__(time2):continue
      return x["buildId"],"这是用户所在位置"
  day=time.weekday()#计算星期几
  rex=tbUserCourse.find_all({"userId":userId,"星期":day})
  temptime=str(timeact.date())+" 08:00:00"
  for x in rex:#课程检测
    time1=datetime.strptime(temptime, "%Y-%m-%d %H:%M:%S")
    time1=time1+timedelta(minutes=(45*(x["节次"]-1)))
    if time1.__le__(time2):
      time1=time1+timedelta(minutes=(45*x["时长"]))
      if time1.__le__(time2):continue
      return x["地点"],"这是用户所在位置"
  nofind=tbUser.find_one({"userId":userId})
  return nofind["addr"],"这是用户注册地址"


def lasttotimedelta(str):
  strtime=str.split(":")
  return timedelta(hours=int(strtime[0]),minutes=int(strtime[1]),seconds=int(strtime[2]))

if __name__ == "__main__":
  data1={
    "type":2,#1 represent personal ,2 means collective
    "name":"class meeting",
    "InitiatorId":"2020211838",
    "time":str(datetime(2022,6,14,11)),
    "last":str(timedelta(hours=2))
  }
  data2={
    "type":1,#1 represent personal ,2 means collective
    "name":"run",
    "InitiatorId":"2020211839",
    "time":str(datetime(2022,6,14,9)),
    "last":str(timedelta(hours=3)),
  }
  print(actvt_create(data1))
  print(actvt_create(data2))
  print("2020211839: ",actvt_list("2020211839"))
  print("canjoin:",actvt_canjoin_list("2020211839"))
  print(actvt_join("2020211839", 0))
  print("2020211839: ",actvt_list("2020211839"))
  data3={
    "type":1,#1 represent personal ,2 means collective
    "name":"run again",
    "InitiatorId":"2020211839",
    "time":str(datetime(2022,6,16,22)),
    "last":str(timedelta(hours=2)),
  }
  actvt_update(1, data3)
  print("2020211839: ",actvt_list("2020211839"))
  actvt_del(0,"2020211838")
  print("2020211839: ",actvt_list("2020211839"))
