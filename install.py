from Utils.database import conn

#user初始数据
from Utils import user
usertb=conn.create("user")
usertb.set_ukey("id")
user.sign_up("2020211838", "12345678", "教师", "珠峰", "17623596408")
user.sign_up("2020211839", "12345678", "学生", "彭木", "17623596409")


#file初始数据
conn.create("file")