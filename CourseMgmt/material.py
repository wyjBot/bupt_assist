import sys,os.path as path
sys.path.append(path.dirname(__file__))
from datetime import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn
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

