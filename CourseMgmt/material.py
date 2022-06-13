import sys,os.path as path
sys.path.append(path.dirname(__file__))
from Utils.Time import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn

"""The implementation principle of this module 
    is highly similar to hmwt module
    you could refer to detail annotation in homework.py/hmwt
"""
################class_material##################
def list_class_material(classId=-1):
  """list all class when classId=-1"""
  return

def search_class_material(classId=-1,match="有限状态自动机"):
  """search all class_material when classId=-1"""
  return

def view_material(materialId):
  """return all version """
  return

def rollback_class_material(materialId,version):
  """恢复到历史版本"""
  return

def create_class_material(classId,data):
  data={
    "title":"课件1",
    "descript":"the ppt of the first chapter",
    "attachId":2435,
  }
  materialId =3
  return materialId

def update_class_material(materialId,data):
  "refer to the descript of update_hmwk"
  version+=1
  return

def delete_class_material(materialId):
  return

