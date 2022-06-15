import sys,os
import sys,os.path as path
sys.path.append(path.dirname(__file__))
sys.path.append('.')
from Utils.database import conn
from datetime import datetime
import json as js
import Md5 as md5

tb=conn["user"]


def sign_up(id,passwd,role,name,phone):
  if role not in ["学生","教师"]:
    return -101,"请选择正确的用户角色(学生/教师)"
  if len(phone)!=11 or phone[0]!='1':
    return -10,"请输入正确的中国大陆手机号"
  if len(passwd)<6 or 25<len(passwd):
    return -20,"密码长度在6~25个字符之间"
  if len(id)!=10:
    return -30,"请输入正确的10位学号/工号"
  if len(name)<2 or 15<len(name):
    return -40,"姓名长度在2~15个字符之间"
  passwd=md5.en(passwd)
  data={
      "role":role,
      "id":id,
      "phone":phone,
      "name":name,
      "passwd":passwd,
      "sessionId":None
    }
  if  tb.find_one({"phone":phone}):return -11,"手机号已注册"
  if  tb.find_one({"id":id}):   return -33,"学号/工号已注册"
  tb.insert(data)
  return 1,"注册成功"

def sign_in(IdorPhone,passwd):
  passwd=md5.en(passwd)
  res=tb.find_one({"phone":IdorPhone,"passwd":passwd})
  if not res: res=tb.find_one({"id":IdorPhone,"passwd":passwd})
  if not res: return -1,"用户名或密码错误"
  return 1,newSession(res['id'])

def newSession(userId):
  sessionId =md5.en(str(userId)+str(datetime.now()))
  tb.update({"id":userId},{"sessionId":sessionId})
  return sessionId 

def vrfSession(serial):
  user=tb.find_one({"session":serial})
  if user:return user
  else:return None

if __name__=='__main__':
  sign_up("2020211838", "12345678", "教师", "珠峰", "17623596408")
  sign_up("2020211839", "12345678", "学生", "彭木", "17623596409")
# import json

# class user:
#   def __init__(self,user_status:str,id:str,phone:int,passwd:str):
#     self.user_status=user_status
#     self.id=id
#     self.phone=phone
#     self.passwd=passwd

# def dict2user(d):
#     return user(d['user_status'],d['id'],d['phone'],d['passwd'])


# IS_LOGIN="NO"
# USER_LIST=user("unlogin",0,0,0)

# def login():#登录
#     userid=input("请输入用户id")
#     userpasswd=input("请输入密码")
#     judge=0#判断有无用户
#     with open("user.txt","r") as f:
#         for line in f:
#             user_list=json.loads(line,object_hook=dict2user)
#             if user_list.id==userid and user_list.passwd==userpasswd:
#                 print("登录成功")
#                 global USER_LIST,IS_LOGIN
#                 USER_LIST=user_list
#                 IS_LOGIN="YES"
#                 judge=1
#     if judge==0:
#         print("用户名或密码错误")
            

# def is_login(func):#装饰器，判断是否已经登录
#     def decorator(*args,**kwargs):
#         if IS_LOGIN=="YES":
#             return func(*args,**kwargs)
#         else:
#             print("未登录，请登录后再试")
#     return decorator

# @is_login
# def change_password():#修改密码
#     print("当前用户id为:%s"%USER_LIST.id)
#     count=3
#     while count>=0:
#         old_password=input("请输入当前用户的旧密码：")
#         if old_password==USER_LIST.passwd:
#             new_password1=input("请输入当前用户的新密码：")
#             if len(new_password1)>=8:
#                 new_password2=input("请再次输入当前用户的新密码：")
#                 if new_password1==new_password2:
#                     USER_LIST.passwd=new_password1
#                     with open("user.txt","r") as old:
#                         all_user=old.readlines()
#                     with open("user.txt","w") as new:
#                         for line in all_user:
#                             user_list=json.loads(line,object_hook=dict2user)
#                             if user_list.id==USER_LIST.id:
#                                 line=line.replace(json.dumps(user_list,default=lambda obj: obj.__dict__)+"\n", json.dumps(USER_LIST,default=lambda obj: obj.__dict__)+"\n")
#                             new.write(line)
#                     print("修改成功")
#                     break
#             else:
#                 print("密码过短，请重新尝试")
#                 count-=1
#         if count==-1:
#             print("错误次数过多，即将退出")
