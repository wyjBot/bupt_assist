import clean
from datetime import datetime
from Utils.database import conn
import json as js
from Utils.Time import datetime,timedelta
import os.path as path
import os,sys,shutil
#user初始数据（学号，密码，类型，姓名，电话，地址）
usertb=conn.create("user")
usertb.set_ukey("id")
from Utils import user
user.sign_up("2020211838", "12345678", "教师", "珠峰", "17623596408",23)
user.sign_up("2020211839", "12345678", "学生", "彭木", "17623596409",16)
user.sign_up("2020211840", "12345678", "教师", "陈锋", "17623596410",23)
user.sign_up("2020211841", "12345678", "教师", "郭斌", "17623596411",21)
user.sign_up("2020211842", "12345678", "教师", "吴岗", "17623596412",21)
user.sign_up("2020211848", "12345678", "教师", "郜濒", "17623596418",23)
user.sign_up("2020211843", "12345678", "教师", "周智", "17623596413",23)
user.sign_up("2020211844", "12345678", "学生", "张韬", "17623596414",15)
user.sign_up("2020211845", "12345678", "学生", "焦俊毅", "17623596415",14)
user.sign_up("2020211846", "12345678", "学生", "高稚柳", "17623596416",16)
user.sign_up("2020211847", "12345678", "学生", "肖晟轩", "17623596417",15)

#class初始数据（id，name，教师，上课星期，上课节次，持续时间，建筑id）
coursetb=conn.create("course")
coursetb.set_ukey("id")
from CourseMgmt import course
fr=open("Control/metaData/class.json","r",encoding='utf-8')
data=js.load(fr)
for item in data:
  print(course.update_class(item['id'], item['teacherId'], item))



tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
tbActvt.set_ukey("actvtId")
from Activity import actvt
fr=open("Control/metaData/actvt.json","r",encoding='utf-8')
# print(fr.read());exit(0)
data1=js.load(fr)
for item in data1:
  print(actvt.actvt_create(item))
fr.close()

#user课程关联
userCoursetb=conn.create("userCourse")
userid="2020211839"
course.join_class(2,userid)
course.join_class(3,userid)

#exam初始数据
examtb=conn.create("exam")
examtb.set_ukey("examId")
from CourseMgmt import Exam
fr=open("Control/metaData/exam.json","r",encoding='utf-8')
data2=js.load(fr)
for item in data2:
  print(Exam.create_class_exam(item["classId"], item))

#task初始数据
print("create task")
tasktb=conn.create("task")
tasktb.set_ukey("taskId")
from CourseMgmt import homework as hmwk
fr=open("Control/metaData/task.json","r",encoding='utf-8')
data3=js.load(fr)
for item in data3:
  print(hmwk.create_class_task(item["classId"], item))


#material初始数据
materialtb=conn.create("material")
materialtb.set_ukey("materialId")
from CourseMgmt import material as res
fr=open("Control/metaData/material.json","r",encoding='utf-8')
data4=js.load(fr)
for item in data4:
  print(res.create_class_material(item["id"], item))
#hmwk初始数据
hmwktb=conn.create("hmwk")
hmwkRollBacktb=conn.create("hmwkRollBack")
fr=open("Control/metaData/hmwk.json","r",encoding='utf-8')
data5=js.load(fr)
for item in data5:
  print(hmwk.update_hmwk(item))
#notice初始数据
from Schedule import interface as notice
noticetb=conn.create("notice")
fr=open("Control/metaData/notice.json","r",encoding='utf-8')
data6=js.load(fr)
for item in data6:
  print(notice.notice_add(item["userId"], item))
#file初始数据
conn.create("file")


userId="2020211839"
print(course.list_class("2020211839"))
print("all notice: ",notice.notice_available("2020211839"))
print(Exam.list_user_exam("2020211839"))
print(res.list_user_material(userId))
print("all notice: ",notice.notice_list("2020211839"))
print(notice.notice_del(userId,1))
