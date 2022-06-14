#put the file uploaded to root dir /Upload and classify them by time
#the compress tools is under package utils
import sys,os.path as path
sys.path.append(path.dirname(__file__))
from Utils.DataFrame import *
from Utils.Database import conn
from Utils.Cfg import cfg

tbTask=conn["task"]
tb=conn["userCourse"]
tbCourse=conn["course"]
tbHmwk=conn["hmwk"]
tbHmwkRollBack=conn["hmwkRollBack"]
###########task_mgmt###########
def list_class_task(classId=-1):
  """list all class when classId=-1"""
  """
  ret={
   "1":{"name":"第一章习题","taskId":234,} ,
   "2":{"name":"第二章习题","taskId":316,} ,
   "3":{"name":"第二章习题(2)","taskId":536,}, 
  }
  """
  if classId==-1:res=tbTask.find_all({})
  else:res=tbTask.find_all({"id":classId})
  ret=dict()
  for x in range(len(res)):
    ret["x"]=res[x]
  return ret,"这是这门课的所有task"

def search_class_task(userId,classId=-1,match="有限状态自动机"):
  """search all class_task when classId=-1"""
  if not tb.find_one({"id":classId,"userId":userId}):return -1,"该学生没有这门课"
  res=tb.find_all({"userId":userId})
  ret=list()
  for x in res:
    ret.extend(tbCourse.find_one({"id":x["id"]}))
  return ret,"返回的是课程的list"


def list_user_task(userId):
  """
  ret= {
   "1":{"name":"第一章习题", "className":"计算机网络", "classId":24,"taskId":234,} ,
   "2":{"name":"第一周", "className":"编译原理", "classId":12,"taskId":231,} ,
  }
  """
  res=tb.find_all({"userId":userId})
  temp=dict()
  ret=dict()
  count=1
  for x in res:
    temp=list_class_task(x["id"])
    for x in range(len(temp)):
      ret[count]=temp[x]
  return

def search_user_task(userId,):
  #ret={}
  if not tb.find_one({"id":classId,"userId":userId}):return -1,"该学生没有这门课"
  res=tb.find_all({"userId":userId})
  ret=list()
  for x in res:
    ret.extend(tbCourse.find_one({"id":x["id"]}))
  return ret,"返回的是课程的list"

def create_class_task(classId,data):
  '''parameter data will be a dict,contain key
  name, des, attentionId,Deadline
  the func return taksId
  '''
  res=tbTask.find_all()
  data["classId"]=classId
  data["taskId"]=len(res)+1
  tbTask.insert(data)
  """
  data={
    "name":
    "des":
    "attentionId":
    "deadline":datetime(2022,5,12)
  }
    "classId":
    "taskId":
  """
  return len(res)+1,"已经创建task"

def view_task(taskId):
  '''return a dict contain key same as "create_task" '''
  res=tbTask.find_one({"taskId":taskId})
  return res[0],"已返回该task"

######hmwk_mgmt############

def view_hmwk(hmwkId):
  '''ret a dict contain all hmwk version '''
  ret=tbHmwk.find_one({"hmwkId":hmwkId})
  if not ret:return -1,"不存在该hmwkId"
  return ret

def rollback_hmwk(hmwkId,version):
  """reset hmwk version to old ret 1 when suc
  return 0 when creates failed because of noexist id"""
  res=tbHmwkRollBack.find_one({"hmwkId":hmwkId,"version":version})
  if not res:return 0,"不存在该版本"
  tbHmwk.update({"hmwkId":hmwkId},res)
  return 

def submit_hmwk(data):
  """generate and ret a hmwkId for the taskId of user"""
  """return 0 when creates failed because of insuffcient data or wrong userId/taskId"""
  """
  data={#example
    "date":datetime.now(),
    "userId":2020211888,
    "taskId":1312,
    "text":"解:1.A 2.B 3.正确 4.总线结构",#文本作业
    "fileId":2350,#作业附件文件Id
  }
  #save the data to database and hmwkId ++ and ret now hmwk
  """
  res=tbTask.find_one({"taskId":data["taskId"]})
  if not res:return -1,"taskId错误"
  if not tb.find_one({"id":res["classId"],"userId":userId}):return -1,"userId错误"
  hmwkId=len(tbHmwk.find_all())+1
  data["hmwkId"]=hmwkId
  data["version"]=0
  tbHmwk.insert(data)
  return hmwkId

def update_hmwk(data):
  '''return now versionId'''
  """return 0 when update failed because of blank data or wrong taskId"""
  """"
  data={#example
    "date":datetime.now(),
    "hmwkId":1312,
    "text":"解:1.A 2.B 3.正确 4.总线结构",#文本作业
    "fileId":2350,#作业附件文件Id
  }
  #save the data to database and hmwkId ++ and ret now hmwk
  """
  res=tbHmwk.find_one({"hmwkId":data["hmwkId"]})
  if not res:return 0,"hmwkId错误"
  data["userId"]=res["userId"]
  data["taskId"]=res["taskId"]
  data["version"]=res["version"]+1
  tbHmwkRollBack.update({"hmwkId":data["hmwkId"],"version":res["version"]},res)
  tbHmwk.update({"hmwkId":data["hmwkId"]},data)
  return data["version"]
