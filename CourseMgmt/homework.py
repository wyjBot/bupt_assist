#put the file uploaded to root dir /Upload and classify them by time
#the compress tools is under package utils
import sys,os.path as path
sys.path.append(path.dirname(path.dirname(__file__)))
import Utils
from Utils.Log import *
from Utils.Time import *
from Utils.DataFrame import *
from Utils.database import conn
from Utils.Cfg import cfg

tbTask=conn.create("task")
tb=conn.create("userCourse")
tbCourse=conn.create("course")
tbHmwk=conn.create("hmwk")
tbHmwkRollBack=conn.create("hmwkRollBack")
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
  else:res=tbTask.find_all({"classId":classId})
  log("list_class_task:class="+str(classId),0)
  return res,"这是这门课的所有task"

def search_class_task(userId,classId=-1,match="有限状态自动机"):
  """search all class_task when classId=-1"""
  if not tb.find_one({"id":classId,"userId":userId}):return -1,"该学生没有这门课"
  res=tb.find_all({"userId":userId})
  ret=list()
  for x in res:
    ret.extend(tbCourse.find_one({"id":x["id"]}))
  log("search_class_task",0)
  return ret,"返回的是课程的list"


def list_user_task(userId):
  """
  ret= {
   "1":{"name":"第一章习题", "className":"计算机网络", "classId":24,"taskId":234,} ,
   "2":{"name":"第一周", "className":"编译原理", "classId":12,"taskId":231,} ,
  }
  """
  res=tb.find_all({"userId":userId})
  ret=list()
  for x in res:
    temp=list_class_task(x["id"])
    ret.extend(temp[0])
  log("list_user_task:user="+userId,0)
  return ret,"这是这个学生的所有task"


def create_class_task(classId,data):
  '''parameter data will be a dict,contain key
  name, des, attentionId,Deadline
  the func return taksId
  '''
  res=tbTask.find_all({})
  data["classId"]=classId
  data["taskId"]=len(res)+1
  tbTask.insert(data)
  log("create_class_task:class="+str(classId),0)
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
  log("view_task:task="+str(taskId),0)
  ret=list()
  ret.append(res)
  return ret,"已返回该task"

######hmwk_mgmt############

def view_hmwk(hmwkId):
  '''ret a dict contain all hmwk version '''
  ret=tbHmwk.find_one({"hmwkId":hmwkId})
  if not ret:
    log("view_hmwk fail",2)
    return -1,"不存在该hmwkId"
  log("view_hmwk:hmwkId="+str(hmwkId),0)
  res=list()
  res.append(ret)
  return res,"已经返回该作业"

def rollback_hmwk(hmwkId,version):
  """reset hmwk version to old ret 1 when suc
  return 0 when creates failed because of noexist id"""
  res=tbHmwkRollBack.find_one({"hmwkId":hmwkId,"version":version})
  if not res:
    log("rollback_hmwk fail",2)
    return 0,"不存在该版本"
  tbHmwk.update({"hmwkId":hmwkId},res)
  log("rollback_hmwk:hmwkId="+str(hmwkId),0)
  return 1,"已返回版本"

def submit_hmwk(userId,data):
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
  if not res:
    log("submit_hmwk fail",2)
    return -1,"taskId错误"
  if not tb.find_one({"id":res["classId"],"userId":userId}):
    log("submit_hmwk fail",2)
    return -1,"userId错误"
  hmwkId=len(tbHmwk.find_all({}))+1
  data["hmwkId"]=hmwkId
  data["version"]=0
  tbHmwk.insert(data)
  log("submit_hmwk:userId"+userId,0)
  return hmwkId,"已经提交作业"

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
  if not res:
    log("update_hmwk fail",2)
    return 0,"hmwkId错误"
  data["userId"]=res["userId"]
  data["taskId"]=res["taskId"]
  data["version"]=res["version"]+1
  tbHmwkRollBack.update({"hmwkId":data["hmwkId"],"version":res["version"]},res)
  tbHmwk.update({"hmwkId":data["hmwkId"]},data)
  log("update_hmwk",0)
  return data["version"],"已经更新作业"

if __name__ == "__main__":
  
  data1={
    "name":"第一章习题",
    "des":"一个习题",
    "attentionId":1,
    "deadline":str(now())
  }
  data2={
    "name":"第二章习题",
    "des":"二个习题",
    "attentionId":2,
    "deadline":str(now())
  }
  data3={
    "name":"第一章习题",
    "des":"一个习题",
    "attentionId":3,
    "deadline":str(now())
  }
  create_class_task(12, data1)
  create_class_task(12, data2)
  create_class_task(13, data3)
  print("12: ",list_class_task(12))
  print("13: ",list_class_task(13))
  print("2020211839: ",list_user_task("2020211839"))
  print("task1: ",view_task(1))
  
  data4={#example
    "date":str(now()),
    "userId":2020211839,
    "taskId":1,
    "text":"解:1.A 2.B 3.正确 4.总线结构",#文本作业
    "fileId":2350,#作业附件文件Id
  }
  data5={#example
    "date":str(now()),
    "userId":2020211839,
    "taskId":2,
    "text":"解:1.A 2.B 3.正确 4.总线结构",#文本作业
    "fileId":2351,#作业附件文件Id
  }
  submit_hmwk("2020211839",data4)
  submit_hmwk("2020211839",data5)
  print("hmwk1: ",view_hmwk(1))
  print("hmwk2: ",view_hmwk(2))
  data6={#example
    "date":str(now()),
    "hmwkId":1,
    "text":"错误答案",#文本作业
    "fileId":2352,#作业附件文件Id
  }
  update_hmwk(data6)
  print("hmwk1: ",view_hmwk(1))
  rollback_hmwk(1, 0)
  print("hmwk1: ",view_hmwk(1))
