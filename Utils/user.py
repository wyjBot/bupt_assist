import sys,os
import sys,os.path as path
sys.path.append(path.dirname(__file__))
sys.path.append('.')
from Utils.database import conn
from Utils.Log import log
from datetime import datetime
import json as js
import Md5 as md5

tb=conn.create("user")


def sign_up(id,passwd,role,name,phone,addr):
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
      "addr":addr,
      "session":None
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
  tb.update({"id":userId},{"session":sessionId})
  return sessionId 

def vrfSession(serial):
  user=tb.find_one({"session":serial})
  if user:return user['id']
  else:return None

if __name__=='__main__':
  sign_up("2020211838", "12345678", "教师", "珠峰", "17623596408")
  sign_up("2020211839", "12345678", "学生", "彭木", "17623596409")
# import json
