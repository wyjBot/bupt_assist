#put the file uploaded to root dir /Upload and classify them by time
#the compress tools is under package utils
import sys,os.path as path
sys.path.append(path.dirname(__file__))
from datetime import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn
from Utils.Cfg import cfg
###########task_mgmt###########
def list_class_task(classId=-1):
  """list all class when classId=-1"""
  ret={
   "1":{"name":"第一章习题","taskId":234,} ,
   "2":{"name":"第二章习题","taskId":316,} ,
   "3":{"name":"第二章习题(2)","taskId":536,}, 
  }
  pass

def search_class_task(classId=-1,match="有限状态自动机"):
  """search all class_task when classId=-1"""
  return


def list_user_task(userId):
  ret= {
   "1":{"name":"第一章习题", "className":"计算机网络", "classId":24,"taskId":234,} ,
   "2":{"name":"第一周", "className":"编译原理", "classId":12,"taskId":231,} ,
  }
  return

def search_user_task(userId,):
  ret={}

def create_class_task(classId,data):
  '''parameter data will be a dict,contain key
  name, des, attentionId,Deadline
  the func return taksId
  '''
  data={
    "deadline":datetime(2022,5,12)
  }
  pass

def view_task(taskId):
  '''return a dict contain key same as "create_task" '''
  return

######hmwk_mgmt############

def view_hmwk(hmwkId):
  '''ret a dict contain all hmwk version '''
  return

def rollback_hmwk(hmwkId,version):
  """reset hmwk version to old ret 1 when suc
  return 0 when creates failed because of noexist id"""
  return 

def submit_hmwk(data):
  """generate and ret a hmwkId for the taskId of user"""
  """return 0 when creates failed because of insuffcient data or wrong userId/taskId"""
  data={#example
    "date":datetime.now(),
    "userId":2020211888,
    "taskId":1312,
    "text":"解:1.A 2.B 3.正确 4.总线结构",#文本作业
    "fileId":2350,#作业附件文件Id
  }
  #save the data to database and hmwkId ++ and ret now hmwk
  hmwkId=342
  return hmwkId

def update_hmwk(data):
  '''return now versionId'''
  """return 0 when update failed because of blank data or wrong taskId"""
  data={#example
    "date":datetime.now(),
    "hmwkId":1312,
    "text":"解:1.A 2.B 3.正确 4.总线结构",#文本作业
    "fileId":2350,#作业附件文件Id
  }
  #save the data to database and hmwkId ++ and ret now hmwk
  version=3
  return version