import sys,os.path as path
sys.path.append(path.dirname(__file__))
sys.path.append(path.dirname(path.dirname(__file__)))
import Utils
from Utils.Log import *
from Utils.Time import datetime,timedelta
from Utils.DataFrame import *
from Utils.database import conn

"""The implementation principle of this module 
    is highly similar to hmwt module
    you could refer to detail annotation in homework.py/hmwt
"""
tbMaterial=conn.create("material")
tb=conn.create("userCourse")
tbCourse=conn.create("course")
tbMaterialRollBack=conn.create("materialRollBack")
################class_material##################
def list_class_material(classId=-1):
  """list all class when classId=-1"""
  if classId==-1:res=tbMaterial.find_all({})
  else:res=tbMaterial.find_all({"id":classId})
  for x in res:
    x.pop("id")
    x.pop("version")
    x["标题"]=x.pop("title")
    x["描述"]=x.pop("descript")
  log("list_class_material:class="+str(classId),0)
  return res,"这是所有的task"

def view_material(materialId):
  """return all version """
  #返回的id是课程的id
  res=tbMaterial.find_one({"materialId":materialId})
  if not res:
    log("view_task fail",2)
    return -1,"不存在该taskId"
  res.pop("materialId")
  res.pop("version")
  res["标题"]=res.pop("title")
  res["描述"]=res.pop("descript")
  ret=list()
  ret.append(res)
  log("view_material:material="+str(materialId),0)
  return res,"已返回该material"

def rollback_class_material(materialId,version):
  """恢复到历史版本"""
  res=tbMaterialRollBack.find_one({"materialId":materialId,"version":version})
  if not res:
    log("rollback_class_material fail",2)
    return 0,"不存在该版本"
  tbMaterial.update({"materialId":materialId},res)
  log("rollback_class_material:materialId="+str(materialId),0)
  return 1,"已返回版本"

def create_class_material(classId,data):
  """
  data={
    "title":"课件1",
    "descript":"the ppt of the first chapter",
    "attachId":2435,
  }
  "classId":
  "materialId"
  """
  res=tbMaterial.find_all({})
  data["id"]=classId
  if len(res)==0:
    data["materialId"]=0
  else:
    data["materialId"]=(res[len(res)-1])["materialId"]+1
  data["version"]=0
  tbMaterial.insert(data)
  log("create_class_task:class="+str(classId),0)
  return data["materialId"],"已经创建资料"

def update_class_material(materialId,data):
  "refer to the descript of update_material"
  res=tbMaterial.find_one({"materialId":materialId})
  if not res:
    log("update_class fail",2)
    return 0,"materialId错误"
  data["version"]=res["version"]+1
  tbMaterialRollBack.update({"materialId":materialId,"version":res["version"]},res)
  tbMaterial.update({"materialId":materialId},data)
  log("update_class_material:materialId="+str(materialId),0)
  return data["version"],"已更新资料"

def delete_class_material(materialId):
  res=tbMaterial.find_one({"materialId":materialId})
  tbMaterial.remove(res)
  ret=tbMaterialRollBack.find_all({"materialId":materialId})
  for x in range(len(ret)):
    tbMaterialRollBack.remove(ret[x])
  log("delete_class_material:material="+str(materialId),0)
  return 1,"已删除资料"

if __name__ == "__main__":
  data1={
    "title":"课件1",
    "descript":"the ppt of the first chapter",
    "attachId":2435,
  }
  data2={
    "title":"课件2",
    "descript":"the ppt of the second chapter",
    "attachId":2436,
  }
  data3={
     "title":"课件1",
    "descript":"the ppt",
    "attachId":2437,
  }
  create_class_material(12, data1)
  create_class_material(12, data2)
  create_class_material(13, data3)
  print("12: ",list_class_material(12))
  print("13: ",list_class_material(13))
  print("material1: ",view_material(1))
  data4={
    "title":"课件4",
    "descript":"the ppt of the 4 chapter",
    "attachId":2438,
  }
  update_class_material(1, data4)
  print("12: ",list_class_material(12))
  rollback_class_material(1, 0)
  print("12: ",list_class_material(12))
  delete_class_material(2)
  print("12: ",list_class_material(12))
