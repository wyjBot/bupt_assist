from Utils.database import conn

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
userCoursetb=conn.create("userCourse")
coursetb=conn.create("course")
usertb=conn.create("user")
data1={"id":1,"name":"计算机系统基础","教师":"陈锋","上课星期":0,"上课节次":3,"持续时间":3,"buildId":18}
data2={"id":2,"name":"数据结构","教师":"郜濒","上课星期":1,"上课节次":2,"持续时间":2,"buildId":18}
data3={"id":3,"name":"离散数学","教师":"珠峰","上课星期":2,"上课节次":3,"持续时间":3,"buildId":18}
data4={"id":4,"name":"习近平新时代中国特色社会主义思想概论","教师":"郭斌","上课星期":3,"上课节次":1,"持续时间":2,"buildId":19}
data5={"id":5,"name":"概率论","教师":"吴岗","上课星期":4,"上课节次":2,"持续时间":2,"buildId":18}
data6={"id":6,"name":"电子学","教师":"周智","上课星期":0,"上课节次":6,"持续时间":2,"buildId":2}
data7={"id":7,"name":"高等数学","教师":"陈锋","上课星期":1,"上课节次":3,"持续时间":2,"buildId":11}
data8={"id":8,"name":"英语","教师":"珠峰","上课星期":2,"上课节次":7,"持续时间":2,"buildId":11}
data9={"id":9,"name":"中国近代史","教师":"郭斌","上课星期":3,"上课节次":7,"持续时间":2,"buildId":19}
data10={"id":10,"name":"军事理论","教师":"吴岗","上课星期":4,"上课节次":6,"持续时间":3,"buildId":2}
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

from Activities import interface
tbActvt=conn.create("actvt")
tbUserActvt=conn.create("userActvt")
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":1,"name":"running","InitiatorId":"2020211839","time":str(datetime(2022,6,5,20)),"last":str(timedelta(minutes=30))}
data1={"type":1,"name":"play basketball","InitiatorId":"2020211844","time":str(datetime(2022,6,5,17)),"last":str(timedelta(hours=2))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
data1={"type":2,"name":"class meeting","InitiatorId":"2020211839","time":str(datetime(2022,6,5,18)),"last":str(timedelta(hours=1))}
#file初始数据
conn.create("file")
