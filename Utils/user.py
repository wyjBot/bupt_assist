import sys,os
sys.path.append('.')
from Utils.database import cnct_db
import json as js
import hashlib

def enMD5(txt):
  md5Obj = hashlib.md5(b'md5secert')
  md5Obj.update(txt)
  ret = md5Obj.hexdigest()
  return ret

db=cnct_db()["users"]

def signUp(tb,role,id,name,phone,passwd):
  if role not in [0,1,2]:
    return -101,"请选择正确的用户角色"
  if len(phone)!=11 or phone[0]!=1:
    return -1,"请输入正确的中国大陆手机号"
  if len(passwd)<8 or 25<len(passwd):
    return -2,"密码长度在8~25个字符之间"
  if len(name)<8 or 25<len(name):
    return -3,"姓名长度在2~15个字符之间"
  passwd=enMD5(passwd)
  data={
      "role":role,
      "id":id,
      "phone":phone,
      "name":name,
      "passwd":passwd
    }
  db.find_one({"phone":phone})

def signIn(tb,IdorPhone,password):
  pass


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

# def user_register():  #注册函数
#     registerid=input("请输入用户名：")
#     registertype_judge=input("请选择用户类型：0.管理员 1.学生")
#     if registertype_judge=="0":
#         registertype="administrator"
#     else:
#         registertype="student"
#     while True:
#         registerpasswd=input("请输入密码：")
#         if len(registerpasswd)>=8:
#             break
#     while True:
#         registerphone=input("请输入手机号：")
#         if len(registerphone)==11:
#             break
#     register_user = user(registertype,registerid,registerphone,registerpasswd)
#     registered=0
#     with open("user.txt","r") as f:
#         for line in f:
#             user_list=json.loads(line,object_hook=dict2user)
#             if register_user.id==user_list.id:
#                 print("用户名已被注册")
#                 registered=1
#                 break
#             if register_user.phone==user_list.phone:
#                 print("手机号已被注册")
#                 registered=1
#                 break
#     if registered==0:
#         with open("user.txt","a") as f:
#             f.write(json.dumps(register_user,default=lambda obj: obj.__dict__)+"\n")
#         print("注册成功")
            
# def register(): #注册
#     if IS_LOGIN=="YES":
#         print("已登录，无法注册")
#     else:
#         user_register()

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
