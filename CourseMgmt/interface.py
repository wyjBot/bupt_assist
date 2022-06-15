import sys,os.path as path
sys.path.append(path.dirname(path.dirname(__file__)))
import Utils
from Utils.Time import datetime,timedelta
from Utils.DataFrame import *
from Utils.database import conn
from Utils.Log import *

tb=conn.create("userCourse")
tbCourse=conn.create("course")
tbUser=conn.create("user")

################class_mgmt##################
def search_class(userId,str="操作系统"):
  '''  
  tb为用户-课程表,当str为“”时返回所有课程
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
  '''
  ret=tb.find_all({})
  res=list()
  for x in ret:
    if not x["userId"]==userId:continue
    if not kmp(str,x["name"]):continue
    res.append(x.copy())
    log("search_class--"+str)
  return res,"已返回查到的课程"

def list_class(userId):
  ret=tb.find_all({"userId":userId})
  return ret,"已返回所有课程"

def join_class(classId,userId):
  res=tbCourse.find_one({"id":classId})
  if not res:return -1,"不存在该课程"
  if tb.find_one({"id":classId,"userId":userId}):return -2,"该课程已加入"
  res["userId"]=userId
  tb.insert(res)
  return 1,"已加入该学生课表"

def quit_class(classId,userId):
  res=tbCourse.find_one({"id":classId})
  if not res:return -1,"不存在该课程"
  if not tb.find_one({"id":classId,"userId":userId}):return -2,"该学生无该门课程"
  res["userId"]=userId
  tb.remove(res)
  return 1,"已退课"

def update_class(classId,userId,data:dict):
  """data为dict格式"""
  res=tbUser.find_one({"id":userId})
  if not res:return -1,"用户名错误"
  if res["role"]=="学生":return -2,"用户权限错误"
  tbCourse.update({"id":classId},data)
  ret=tb.find_all({"id":classId})
  for x in ret:
    data["userId"]=x["userId"]
    tb.update({"id":classId,"userId":x["userId"]},data)
  return 1,"已更新课程信息"

def kmp(keyword,name):#返回值0代表没有，1代表有
    if isinstance(keyword,str) and isinstance(name,str):#判断输入条件
        if len(keyword)==0:
            return 1
        if len(name)==0:
            return 0
        nextplace=[-1 for i in range(len(keyword))]#初始化next数组
        nextplace[1]=0
        i=1
        j=0
        while i<len(keyword)-1:#计算next数组
            if j==-1 or keyword[i]==keyword[j]:
                i+=1
                j+=1
                nextplace[i]=j
            else:
                j=nextplace[j]
        a=b=0#初始化串的开始位置
        while(a<len(name) and b<len(keyword)):#kmp算法
            if b==-1 or name[a]==keyword[b]:
                a+=1
                b+=1
            else:
                b=nextplace[b]
        if b==len(keyword):#匹配成功
          return 1
    return 0

if __name__ == '__main__':
  # """
  data1={
      "id":14,
      "name":"计算机组成",
      "教师":"陈锋",
      "上课星期":1,#星期二
      "上课节次":3,#第八节
      "持续时间":3,#以节为单位，每节课45min
      "教学楼":"n3多功能教学楼",
      "教室":641,
      "上课地点":18,#返回建筑Id
  }
  data2={
      "id":15,
      "name":"计算机网络课程设计",
      "教师":"",
      "上课时间":1,
      "持续时间":2,
  }
  update_class(14, "2020211838", data1)
  update_class(15, "2020211838", data2)
  # """
  print("all: ",list_class("2020211839"))
  print("操作: ",search_class("2020211839","操作"))
  join_class(13, "2020211839")
  print("操作: ",search_class("2020211839","操作"))
