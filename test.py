from datetime import datetime
from Utils.database import conn
import json as js
from Utils.Time import datetime,timedelta

#user初始数据（学号，密码，类型，姓名，电话，地址）
from Utils import user
usertb=conn.create("user")
usertb.set_ukey("id")
user.sign_up("2020211838", "12345678", "教师", "珠峰", "17623596408",23)
user.sign_up("2020211839", "12345678", "学生", "彭木", "17623596409",16)
user.sign_up("2020211840", "12345678", "教师", "陈锋", "17623596410",23)
user.sign_up("2020211841", "12345678", "教师", "郭斌", "17623596411",21)
user.sign_up("2020211842", "12345678", "教师", "吴岗", "17623596412",21)
user.sign_up("2020211843", "12345678", "教师", "周智", "17623596413",23)
user.sign_up("2020211844", "12345678", "学生", "张韬", "17623596414",15)
user.sign_up("2020211845", "12345678", "学生", "焦俊毅", "17623596415",14)
user.sign_up("2020211846", "12345678", "学生", "高稚柳", "17623596416",16)
user.sign_up("2020211847", "12345678", "学生", "肖晟轩", "17623596417",15)
user.sign_up("2020211848", "12345678", "教师", "郜濒", "17623596418",23)

#class初始数据（id，name，教师，上课星期，上课节次，持续时间，建筑id）
from CourseMgmt import course
coursetb=conn.create("course")
coursetb.set_ukey("id")
fr=open("Control/metaData/class.json","r",encoding='utf-8')
data=js.load(fr)
for item in data:
  print(course.update_class(item['id'], item['teacherId'], item))



import json as js
from Activity import actvt
tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
tbActvt.set_ukey("actvtId")
fr=open("Control/metaData/actvt.json","r",encoding='utf-8')
# print(fr.read());exit(0)
data1=js.load(fr)
for item in data1:
  actvt.actvt_create(item)
fr.close()

#user课程关联
userCoursetb=conn.create("userCourse")
course.join_class(2,"2020211839")
actvt.actvt_join("2020211839",3)

uid="2020211839"
print(course.list_class(uid))
print(actvt.actvt_list(uid))
