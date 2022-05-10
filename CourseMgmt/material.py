import sys,os.path as path
sys.path.append(path.dirname(__file__))
from datetime import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn

"""The implementation principle of this module 
    is highly similar to hmwt
    you could refer to detail annotation in homework.py
"""
################course_material##################
def list_course_material(classId):
  return

def view_material(materialId):
  """return all version """
  return

def rollback_course_material(materialId,version):
  """恢复到历史版本"""
  return

def create_course_material(classId,data):
  data={
    "title":"课件1",
    "descript":"the ppt of the first chapter",
    "attachId":2435,
  }
  materialId =3
  return materialId

def update_course_material(materialId,data):
  "refer to the descript of update_hmwk"
  version+=1
  return

def delete_course_material(materialId):
  return

