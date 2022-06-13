import sys,os.path as path
sys.path.append(path.dirname(__file__))
from Utils.Time import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn

"""The implementation principle of this module 
    is highly similar to CourseMgmt
    you could refer to detail annotation in CourseMgmt/interface.py
"""
##########活动管理与查看，加入#############
def actvt_list(userId):
  return

def actvt_create(data):
  '''input data,return generated actvtId'''
  data={
    "type":2,#1 represent personal ,2 means collective
    "name":"class meeting",
    "InitiatorId":2020211888,
    "time":datetime(2022,6,15,14),
    "last":timedelta(2),
  }
  return 

def actvt_join(userId,):
  '''join a actvt created by others'''
  return 

def actvt_del(actvtId,userId=-1):
  '''delete a actvt,pay attention to check user's Permission'''
  return

def actvt_update(actvtId):
  return