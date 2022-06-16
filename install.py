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



from Activity import actvt
tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
tbActvt.set_ukey("actvtId")
fr=open("Control/metaData/actvt.json","r",encoding='utf-8')
# print(fr.read());exit(0)
data1=js.load(fr)
for item in data1:
  print(actvt.actvt_create(item))
fr.close()


#exam初始数据
from CourseMgmt import Exam
examtb=conn.create("exam")
examtb.set_ukey("examId")
fr=open("Control/metaData/exam.json","r",encoding='utf-8')
data2=js.load(fr)
for item in data2:
  print(Exam.create_class_exam(item["classId"], item))

#task初始数据
print("create task")
from CourseMgmt import homework as hmwk
tasktb=conn.create("task")
tasktb.set_ukey("taskId")
fr=open("Control/metaData/task.json","r",encoding='utf-8')
data3=js.load(fr)
for item in data3:
  print(hmwk.create_class_task(item["classId"], item))
"""
data36={"name":"第一次作业","des":"完成1,3,4题","attentionId":0,"deadline":str(datetime(2022,6,15,23,59))}
data37={"name":"第一章","des":"","attentionId":0,"deadline":str(datetime(2022,6,15))}
data38={"name":"期末作业","des":"请独自完成","attentionId":1,"deadline":str(datetime(2022,6,24))}
data39={"name":"第二次作业","des":"请完成2,3(1)(2)","attentionId":0,"deadline":str(datetime(2022,6,16))}
data40={"name":"第二章","des":"完成3,5,7题","attentionId":0,"deadline":str(datetime(2022,6,18))}
data41={"name":"期末作业","des":"","attentionId":2,"deadline":str(datetime(2022,6,25))}
hmwk.create_class_task(1, data36)
hmwk.create_class_task(2, data37)
hmwk.create_class_task(3, data38)
hmwk.create_class_task(4, data39)
hmwk.create_class_task(5, data40)
hmwk.create_class_task(6, data41)
"""

#material初始数据
from CourseMgmt import material
materialtb=conn.create("material")
materialtb.set_ukey("materialId")
fr=open("Control/metaData/material.json","r",encoding='utf-8')
data4=js.load(fr)
for item in data4:
  material.create_class_material(item["id"], item)
"""
data42={"title":"课件1","descript":"the ppt of the first chapter","attachId":2435}
data43={"title":"课件2","descript":"the ppt of the second chapter","attachId":2436}
data44={"title":"课件1","descript":"the ppt","attachId":2437}
data45={"title":"pdf教材","descript":"教材","attachId":2438}
data46={"title":"第一章","descript":"the ppt of the first chapter","attachId":2439}
data47={"title":"第二章","descript":"the ppt of the second chapter","attachId":2440}
data48={"title":"课件3","descript":"answer of chapter one","attachId":2441}
data49={"title":"第一章第一节","descript":"the ppt of the first chapter one session","attachId":2442}
data50={"title":"第一章第二节","descript":"the ppt of the first chapter two session","attachId":2443}
data51={"title":"第二章第二节","descript":"the ppt of the second chapter two session","attachId":2444}
updata_number_42=material.create_class_material(1, data42)
material.create_class_material(1, data43)
material.create_class_material(2, data44)
material.create_class_material(3, data45)
updata_number_46=material.create_class_material(4, data46)
updata_number_47=material.create_class_material(4, data47)
material.create_class_material(1, data48)
material.create_class_material(5, data49)
material.create_class_material(5, data50)
material.create_class_material(5, data51)
"""
data52={"title":"课件1","descript":"the ppt of the first chapter","attachId":2445}
data53={"title":"课件1","descript":"the ppt of the first chapter","attachId":2446}
data54={"title":"课件1","descript":"the ppt of the first chapter","attachId":2447}
#material.update_class_material(, data52)
#material.update_class_material(, data53)
#material.update_class_material(, data54)

#file初始数据
conn.create("file")

#user课程关联
userCoursetb=conn.create("userCourse")
course.join_class(2,"2020211839")

print(course.list_class("2020211839"))
print(Exam.list_user_exam("2020211839"))
