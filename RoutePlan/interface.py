from datetime import datetime,timedelta
from Utils.Database import conn
from Utils.DataFrame import cdnt,buildId
import cv2,numpy as np
#以下为地图的结构化描述，完善后，还应用numpy/cv2生成一张点整图
builds=[
    { "Id":1,"名称":"体育馆",
      "bx":60,#占地矩形左上角x坐标
      "by":800,#占地矩形左上角y坐标
      "ex":180,#占地矩形右下角x坐标
      "ey":1000,#占地矩形右下角y坐标
      "func":2,#0为交通设施，1为上课，2为举办活动，3既可上课又可举办活动
    },
    { "Id":13,"名称":"南丰东路",
      "bx":860,#占地矩形左上角x坐标
      "by":655,#占地矩形左上角y坐标
      "ex":1700,#占地矩形右下角x坐标
      "ey":670,#占地矩形右下角y坐标
      "func":0,#0为交通设施，1为上课，2为举办活动，3既可上课又可举办活动
    },
    { "Id":22,"名称":"n3多功能教学楼",
      "bx":700,#占地矩形左上角x坐标
      "by":920,#占地矩形左上角y坐标
      "ex":760,#占地矩形右下角x坐标
      "ey":1080,#占地矩形右下角y坐标
      "func":3,
    },
    { "Id":31,"名称":"s2科研实验楼",
      "bx":355,#占地矩形左上角x坐标
      "by":470,#占地矩形左上角y坐标
      "ex":1592,#占地矩形右下角x坐标
      "ey":1675,#占地矩形右下角y坐标
      "func":1,
    },
    { "Id":37,"名称":"景观池",
      "bx":355,#占地矩形左上角x坐标
      "by":470,#占地矩形左上角y坐标
      "ex":1092,#占地矩形右下角x坐标
      "ey":1375,#占地矩形右下角y坐标
      "func":2,
    },
  ]

def get_all_build():
  """返回所有建筑信息的字典列表,以下为样例"""
  global builds
  return builds

def get_plan_c2c(s:cdnt,t:cdnt,perfer:int):
  """输入坐标->坐标，进行导航"""
  return res

def get_plan_c2b(s:cdnt,t:buildId,perfer:int):
  """输入坐标->建筑Id，进行导航"""
  return res

def get_plan_b2b(s:cdnt,t:buildId,perfer:int):
  """输入建筑Id->建筑Id，进行导航"""
  return res

def query_cdnt_with_bulidId(num:buildId):
  '''输入一个建筑物ID，输出其入矩形占地
  注意判断id是否有效，无效返回cdnt(-1,-1)'''
  
  crood=cdnt(760,1150)
  return crood

def query_crowd_with_bulidId(num:buildId):
  '''输入一个建筑物ID，查询其拥挤程度，当前在其中人数
  注意判断id是否有效，无效返回-1'''
  crood=cdnt(760,1150)
  return crood

def query_func_with_bulidId(num:buildId):
  '''输入一个建筑物ID，查询其功能,
  0为交通设施，1为上课，2为举办活动，3既可上课又可举办活动 '''
  return 0


def query_bulid_with_cdnt(crood:cdnt):
  '''输入一个坐标，输出其所在的建筑物ID,
  注意判断坐标是否有效，无效返回-1'''
  bulidId=31
  return bulidId

#构造地图时，比例尺为1格：1米
#导航返回以dict格式，样例：
res={
  "step":5,
  "perfer":3,#1步行最短距离策略，2步行最短时间策略，3混合交通工具的最短时间
  "1":{
    "description": "沿着雁北路向南骑行700米，至第一个十字路口",
    #以左上角为左边系原点(0，0),x轴正方向向右,y轴正方向向下
    "cdntSx":253, #起始横坐标
    "cdntSy":639, #起起始纵坐标
    "cdntTx":852, #结束横坐标
    "cdntSy":677,#结束纵坐标
    "duration":300,#以秒为单位
    "crowd":80,#正在该条道路上的人/车数量
    "bulidId":11,#当前路径所位于的建筑物Id
    "by":1,#0表示步行，1表示骑行，2表示校车
  },
  "2":{
    "description": "向右转，进入南丰东路",
    #以左上角为左边系原点(0，0),x轴正方向向右,y轴正方向向下
    "cdntSx":852, #起始横坐标
    "cdntSy":639, #起起始纵坐标
    "cdntTx":860, #结束横坐标
    "cdntSy":655,#结束纵坐标
    "duration":80,#以秒为单位
    "crowd":30,#正在该路口的人/车数量
    "bulidId":12,#当前路径所位于的建筑物Id
    "by":1,#0表示步行，1表示骑行，2表示校车
  },
  "3":{
    "description": "沿着南丰东路向东骑行500米，至自行车停泊点并停车",
    #以左上角为左边系原点(0，0),x轴正方向向右,y轴正方向向下
    "cdntSx":860, #起始横坐标
    "cdntSy":655, #起起始纵坐标
    "cdntTx":1360, #结束横坐标
    "cdntSy":670,#结束纵坐标
    "duration":300,#以秒为单位
    "crowd":500,#正在该条道路上的人/车数量
    "bulidId":13,#当前路径所位于的建筑物Id
    "by":1,#0表示步行，1表示骑行，2表示校车
  },
  "4":{
    "description": "向北步行100米，到达目的地：n3多功能教学楼南门",
    #以左上角为左边系原点(0，0),x轴正方向向右,y轴正方向向下
    "cdntSx":770, #起始横坐标
    "cdntSy":1159, #起起始纵坐标
    "cdntTx":760, #结束横坐标
    "cdntSy":1050,#结束纵坐标
    "duration":120,#以秒为单位
    "crowd":200,#正在该条道路上的人/车数量
    "bulidId":19,#当前路径所位于的建筑物Id
    "by":0,#0表示步行，1表示骑行，2表示校车
  },
}
