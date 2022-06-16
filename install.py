from datetime import datetime
from Utils.database import conn
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
data1={"id":1,"name":"计算机系统基础","教师":"陈锋","星期":0,"节次":3,"时长":3,"地点":18}
data2={"id":2,"name":"数据结构","教师":"郜濒","星期":1,"节次":2,"时长":2,"地点":18}
data3={"id":3,"name":"离散数学","教师":"珠峰","星期":2,"节次":3,"时长":3,"地点":18}
data4={"id":4,"name":"习近平新时代中国特色社会主义思想概论","教师":"郭斌","星期":3,"节次":1,"时长":2,"地点":19}
data5={"id":5,"name":"概率论","教师":"吴岗","星期":4,"节次":2,"时长":2,"地点":18}
data6={"id":6,"name":"电子学","教师":"周智","星期":0,"节次":6,"时长":2,"地点":2}
data7={"id":7,"name":"高等数学","教师":"陈锋","星期":1,"节次":3,"时长":2,"地点":11}
data8={"id":8,"name":"英语","教师":"珠峰","星期":2,"节次":7,"时长":2,"地点":11}
data9={"id":9,"name":"中国近代史","教师":"郭斌","星期":3,"节次":7,"时长":2,"地点":19}
data10={"id":10,"name":"军事理论","教师":"吴岗","星期":4,"节次":6,"时长":3,"地点":2}
course.update_class(1, "2020211840", data1)
course.update_class(2, "2020211848", data2)
course.update_class(3, "2020211838", data3)
course.update_class(4, "2020211841", data4)
course.update_class(5, "2020211842", data5)
course.update_class(6, "2020211843", data6)
course.update_class(7, "2020211840", data7)
course.update_class(8, "2020211838", data8)
course.update_class(9, "2020211841", data9)
course.update_class(10, "2020211842", data10)


#user加入课程
userCoursetb=conn.create("userCourse")
course.join_class(2,"2020211839")

from Activities import activity
tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
data11={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data12={"type":1,"name":"running","InitiatorId":"2020211839","time":str(datetime(2022,6,5,20)),"last":str(timedelta(minutes=30))}
data13={"type":1,"name":"play basketball","InitiatorId":"2020211844","time":str(datetime(2022,6,5,17)),"last":str(timedelta(hours=2))}
data14={"type":1,"name":"eating lunch","InitiatorId":"2020211839","time":str(datetime(2022,6,6,12)),"last":str(timedelta(hours=1))}
data15={"type":2,"name":"music activity","InitiatorId":"2020211845","time":str(datetime(2022,6,5,19)),"last":str(timedelta(hours=2))}
data16={"type":2,"name":"find teacher","InitiatorId":"2020211846","time":str(datetime(2022,6,6,10)),"last":str(timedelta(hours=2))}
data17={"type":1,"name":"play game","InitiatorId":"2020211847","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=4))}
data18={"type":1,"name":"sing","InitiatorId":"2020211845","time":str(datetime(2022,6,6,19)),"last":str(timedelta(hours=1))}
data19={"type":2,"name":"play on gym","InitiatorId":"2020211847","time":str(datetime(2022,6,6,18)),"last":str(timedelta(hours=3))}
data20={"type":2,"name":"watching basketball","InitiatorId":"2020211839","time":str(datetime(2022,6,6,18)),"last":str(timedelta(hours=3))}
data21={"type":2,"name":"早操","InitiatorId":"2020211838","time":str(datetime(2022,6,6,8)),"last":str(timedelta(minutes=40))}
data22={"type":1,"name":"go out","InitiatorId":"2020211846","time":str(datetime(2022,6,7,13)),"last":str(timedelta(hours=6))}
data23={"type":1,"name":"buy something","InitiatorId":"2020211845","time":str(datetime(2022,6,7,19)),"last":str(timedelta(minutes=30))}
data24={"type":2,"name":"play volleyball","InitiatorId":"2020211845","time":str(datetime(2022,6,7,20)),"last":str(timedelta(hours=2))}
data25={"type":1,"name":"write homework","InitiatorId":"2020211847","time":str(datetime(2022,6,7,21)),"last":str(timedelta(hours=3))}
data26={"type":1,"name":"code","InitiatorId":"2020211845","time":str(datetime(2022,6,8,10)),"last":str(timedelta(hours=3))}
data27={"type":2,"name":"club","InitiatorId":"2020211839","time":str(datetime(2022,6,8,13)),"last":str(timedelta(hours=4))}
data28={"type":1,"name":"movie","InitiatorId":"2020211845","time":str(datetime(2022,6,8,14)),"last":str(timedelta(hours=2))}
data29={"type":1,"name":"study","InitiatorId":"2020211847","time":str(datetime(2022,6,8,13)),"last":str(timedelta(hours=5))}
data30={"type":2,"name":"perform","InitiatorId":"2020211839","time":str(datetime(2022,6,8,18)),"last":str(timedelta(hours=1))}
activity.actvt_create(data11)
activity.actvt_create(data12)
activity.actvt_create(data13)
activity.actvt_create(data14)
activity.actvt_create(data15)
activity.actvt_create(data16)
activity.actvt_create(data17)
activity.actvt_create(data18)
activity.actvt_create(data19)
activity.actvt_create(data20)
activity.actvt_create(data21)
activity.actvt_create(data22)
activity.actvt_create(data23)
activity.actvt_create(data24)
activity.actvt_create(data25)
activity.actvt_create(data26)
activity.actvt_create(data27)
activity.actvt_create(data28)
activity.actvt_create(data29)
activity.actvt_create(data30)
#exam初始数据
from CourseMgmt import Exam
examtb=conn.create("exam")
data31={"title":"期末考试","开始时间":str(datatime(2022,6,22,10)),"持续时间":120,"地点":2}
data32={"title":"期末考试","开始时间":str(datatime(2022,6,22,14)),"持续时间":120,"地点":18}
data33={"title":"期末考试","开始时间":str(datatime(2022,6,23,9)),"持续时间":120,"地点":18}
data34={"title":"期末考试","开始时间":str(datatime(2022,6,23,13,30)),"持续时间":120,"地点":11}
data35={"title":"期末考试","开始时间":str(datatime(2022,6,24,8)),"持续时间":120,"地点":2}
Exam.create_class_exam(1, data31)
Exam.create_class_exam(2, data32)
Exam.create_class_exam(3, data33)
Exam.create_class_exam(4, data34)
Exam.create_class_exam(5, data35)
#task初始数据
from CourseMgmt import homework
data36={"name":"第一次作业","des":"完成1,3,4题","attentionId":0,"deadline":str(dataime(2022,6,15,23,59))}
data37={"name":"第一章","des":"","attentionId":0,"deadline":str(dataime(2022,6,15))}
data38={"name":"期末作业","des":"请独自完成","attentionId":1,"deadline":str(dataime(2022,6,24))}
data39={"name":"第二次作业","des":"请完成2,3(1)(2)","attentionId":0,"deadline":str(dataime(2022,6,16))}
data40={"name":"第二章","des":"完成3,5,7题","attentionId":0,"deadline":str(dataime(2022,6,18))}
data41={"name":"期末作业","des":"","attentionId":2,"deadline":str(dataime(2022,6,25))}
create_class_task(1, data36)
create_class_task(2, data37)
create_class_task(3, data38)
create_class_task(4, data39)
create_class_task(5, data40)
create_class_task(6, data41)
#file初始数据
conn.create("file")


print(course.list_class("2020211839"))
