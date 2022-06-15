"""The implementation principle of this module 
    is highly similar task
    you could refer to detail annotation in homework.py/task
"""
import sys,os.path as path
sys.path.append(path.dirname(__file__))
from Utils.DataFrame import *
from Utils.Database import conn
from Utils.Cfg import cfg

tbExam=conn["exam"]
tb=conn["userCourse"]
tbCourse=conn["course"]
###########exam###########
def list_class_exam(classId=-1):
  """list all class when classId=-1"""
  if classId==-1:res=tbExam.find_all({})
  else:res=tbExam.find_all({"id":classId})
  return res,"这是所有的exam"

def search_class_exam(userId,classId=-1,match="有限状态自动机"):
  """search all class_task when classId=-1"""
  if not tb.find_one({"id":classId,"userId":userId}):return -1,"该学生没有这门课"
  res=tb.find_all({"userId":userId})
  ret=list()
  for x in res:
    ret.extend(tbCourse.find_one({"id":x["id"]}))
  return ret,"返回的是课程的list"


def list_user_exam(userId):
  """
  ret= {
   "1":{"title":"期末考试", "持续时间":2,"教学楼":"n3多功能","教室":108, "classId":24,"examId":234,} ,
   "2":{} ,
  }
  """
  res=tb.find_all({"userId":userId})
  temp=dict()
  ret=dict()
  count=1
  for x in res:
    temp=list_class_exam(x["id"])
    for x in range(len(temp)):
      ret[count]=temp[x]
  return

def search_user_exam(userId):
  #ret={}
  if not tb.find_one({"id":classId,"userId":userId}):return -1,"该学生没有这门课"
  res=tb.find_all({"userId":userId})
  ret=list()
  for x in res:
    ret.extend(tbCourse.find_one({"id":x["id"]}))
  return ret,"返回的是课程的list"

def create_class_exam(classId,data):
  '''parameter data will be a dict,contain key
  name, des, attentionId,Deadline
  the func return taksId
  '''
  res=tbExam.find_all()
  data["classId"]=classId
  data["examId"]=len(res)+1
  tbTask.insert(data)
  """
  data={
    "title":
    "持续时间":
    "教学楼":
    "教室":datetime(2022,5,12)
  }
    "classId":
    "examId":
  """
  return len(res)+1,"已经创建task"

def view_task(examId):
  '''return a dict contain key same as "create_task" '''
  res=tbExam.find_one({"taskId":taskId})
  return res,"已返回该exam"
