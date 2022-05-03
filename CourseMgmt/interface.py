import sys,os.path as path
sys.path.append(path.dirname(__file__))
from datetime import datetime,timedelta
from Utils.DataFrame import *


################course##################
def search_course(str="操作系统"):
  res=[
    {
      "id":12,
      "name":"操作系统",
      "教师":"吴军",
      "上课星期":2,#星期二
      "上课节次":6,#第八节
      "持续时间":3,#以节为单位，每节课45min
      "教学楼":"n3多功能教学楼",
      "教室":641,
      "上课地点":18,#返回建筑Id
      "最大人数":90,
      "当前人数":77,
      "已加入":True,
    },
    {
      "id":13,
      "name":"操作系统课程设计",
      "教师":"赵华",
      "上课时间":1,
      "持续时间":2,
      "最大人数":30,
      "当前人数":23,
      "已加入":True,
    },
  ]
  return

def join_course(classId):
  return

def quit_course(classId): 
  return

def edit_course(classId,data:dict):
  """data为dict格式"""
  return

################course_material##################
def list_course_material(classId):
  return

def view_material(materialId):
  """return the newest version and simple inform of history version"""
  return

def rollback_course_material(materialId,version):
  """恢复到历史版本"""
  return

def create_course_material(classId):
  """return -1 when creates failed"""
  materialId =3
  return materialId

def update_course_material(materialId):
  version+=1
  return

def delete_course_material(materialId):
  return

###########task_mgmt###########
def list_crouse_task(courseId):
  pass

def create_course_task(courseId):
  pass

def view_task(courseId):
  pass

######hmwk_mgmt############
def list_class_hmwk(classId):
  return

def view_hmwk(hmwkId):
  return

def submit_hmwk(hmwkId):
  return

def update_hmwk(hmwkId):
  return