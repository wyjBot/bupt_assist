import sys,os.path as path
sys.path.append(path.dirname(__file__))
from datetime import datetime,timedelta
from Utils.DataFrame import *

def view_timetable(userId):
  '''input userId,return his or her integral weekly schedule
      include courses and activities'''
  res={
    "1":{#星期一
      "1":{#第一节
          "type":1,#0表示空堂，1表示一门新课开始，2表示一个新活动开始，3表示继续上一节内容
          "id":12,
          "name":"操作系统",
          "教学楼":"n3多功能教学楼",
          "教室":641,
      },
      "2":{#第二节
          "type":3,
      },
      "3":{#第三节
          "type":3,
      },
      "4":{#第四节
          "type":2,
          "id":3421,
          "name":"疫苗接种"
      },
      "5":{#第五节
          "type":0,
      },
    }
  }
  return res

##########闹钟管理与查看#############
def notice_list(userId):
  return

def notice_available(userId):
  '''return a list of acitvity/course which is able to set a alarm clock'''
  return 

def notice_add(data):
  '''input data,return generated noticeId'''
  return 

def notice_del(noticeId):
  return

def notice_update(noticeId):
  return