from time import sleep
import os,sys,time,os.path as path
sys.path.append(path.dirname(path.dirname(__file__)))
import clean
from datetime import datetime
from Utils.database import conn
import json as js
from Utils.Time import datetime,timedelta
import os.path as path
import os,sys,shutil
#user初始数据（学号，密码，类型，姓名，电话，地址）
from Utils import user

def pwd(subfile):
  _pwd=path.dirname(path.dirname(__file__))
  return os.path.join(_pwd,subfile)

def _user():
  usertb=conn.create("user")
  usertb.set_ukey("id")
  fr=open(pwd("Control/metaData/user.json"),"r",encoding='utf-8')
  data=js.load(fr)
  for key in data:
    print(user.sign_up(*data[key]))

from CourseMgmt import course
def _crouse():
  #class初始数据（id，name，教师，上课星期，上课节次，持续时间，建筑id）
  coursetb=conn.create("course")
  coursetb.set_ukey("id")
  fr=open(pwd("Control/metaData/class.json"),"r",encoding='utf-8')
  data=js.load(fr)
  for item in data:
    course.update_class(item['id'], item['teacherId'], item)

def _exam():
  #exam初始数据
  examtb=conn.create("exam")
  examtb.set_ukey("examId")
  from CourseMgmt import Exam
  fr=open(pwd("Control/metaData/exam.json"),"r",encoding='utf-8')
  data2=js.load(fr)
  for item in data2:
    print(Exam.create_class_exam(item["classId"], item))

_user();_crouse();_exam()

tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
tbActvt.set_ukey("actvtId")
from Activity import actvt
fr=open(pwd("Control/metaData/actvt.json"),"r",encoding='utf-8')
# print(fr.read());exit(0)
data1=js.load(fr)
for item in data1:
  print(actvt.actvt_create(item))
fr.close()



#task初始数据
print("create task")
tasktb=conn.create("task")
tasktb.set_ukey("taskId")
from CourseMgmt import homework as hmwk
fr=open(pwd("Control/metaData/task.json"),"r",encoding='utf-8')
data3=js.load(fr)
for item in data3:
  print(hmwk.create_class_task(item["classId"], item))


#material初始数据
materialtb=conn.create("material")
materialtb.set_ukey("materialId")
from CourseMgmt import material as res
fr=open(pwd("Control/metaData/material.json"),"r",encoding='utf-8')
data4=js.load(fr)
for item in data4:
  print(res.create_class_material(item["id"], item))

#file
from Utils import File as F
F.saveFile(pwd("Control/metaData/file/1.jpg"),True)
F.saveFile(pwd("Control/metaData/file/2.jpg"),True)
F.saveFile(pwd("Control/metaData/file/3.jpg"),True)
F.saveFile(pwd("Control/metaData/file/4.jpg"),True)


#notice初始数据
from Schedule import interface as notice
noticetb=conn.create("notice")
fr=open(pwd("Control/metaData/notice.json"),"r",encoding='utf-8')
data6=js.load(fr)
for item in data6:
  print(notice.notice_add(item["userId"], item))

#file初始数据
conn.create("file")


#user课程关联
userCoursetb=conn.create("userCourse")
userid="2020211839"
for i in range(10):
  print(course.join_class(i,userid))

for i in range(10):
  print(actvt.actvt_join(userid,i))

#hmwk提交
#提交和更新hmwk的示例
#data={
#  "date":
#  "userId":
#  "taskId":
#  "text":
#}
hmwktb=conn.create("hmwk")
hmwkRollBacktb=conn.create("hmwkRollBack")
fr=open(pwd("Control/metaData/hmwk.json"),"r",encoding='utf-8')
data5=js.load(fr)
for item in data5:
  print(item)
  print(hmwk.update_hmwk(item))

#下面是对上面两个提交的hmwk的更新
fr=open(pwd("Control/metaData/hmwkupdate.json"),"r",encoding='utf-8')
data6=js.load(fr)
for item in data6:
  print(item)
  print(hmwk.update_hmwk(item))


#reset Time
import Utils.Time as Time
Time.resetTo(datetime(2022,6,14,8,44))
Time.rate(60)


userId="2020211839"
#test
# print(hmwk.list_user_task("2020211839"))
# print(hmwk.view_hmwk("2020211839",3))
# print(hmwk.view_hmwk("2020211839",4))
# print(course.list_class("2020211839"))
# print(Exam.list_user_exam("2020211839"))
# print(res.list_user_material(userId))
# print("all notice: ",notice.notice_list("2020211839"))
# print(notice.notice_del(userId,1))
# for i in range(1000):
#   sleep(1)
#   print(Time.now(),"notice work:",notice.notice_work(Time.now(), "2020211839"))
