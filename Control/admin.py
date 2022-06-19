from time import sleep
import os,sys,time,os.path as path
sys.path.append(path.dirname(path.dirname(__file__)))
pwd=path.dirname(path.dirname(__file__))+"/"
from datetime import datetime
from Utils.database import conn
import json as js
from Utils.Time import datetime,timedelta
import os.path as path
import os,sys,shutil
#user初始数据（学号，密码，类型，姓名，电话，地址）
from Utils import user

def _user():
  usertb=conn.create("user")
  usertb.set_ukey("id")
  fr=open(pwd+"Control/import/user.json","r",encoding='utf-8')
  data=js.load(fr)
  for key in data:
    print(user.sign_up(*data[key]))

from CourseMgmt import course
def _crouse():
  #class初始数据（id，name，教师，上课星期，上课节次，持续时间，建筑id）
  coursetb=conn.create("course")
  coursetb.set_ukey("id")
  fr=open(pwd+"Control/import/class.json","r",encoding='utf-8')
  data=js.load(fr)
  for item in data:
    print(course.update_class(item['id'], item['teacherId'], item))

def _exam():
  #exam初始数据
  examtb=conn.create("exam")
  examtb.set_ukey("examId")
  from CourseMgmt import Exam
  fr=open(pwd+"Control/import/exam.json","r",encoding='utf-8')
  data2=js.load(fr)
  for item in data2:
    print(Exam.create_class_exam(item["classId"], item))

option=input("choose user,crouse or exam to import:\n")
if option=="user":
  _user()
if option=="crouse":
  _crouse()
if option=="exam":
  _exam()