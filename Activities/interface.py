import sys,os.path as path
sys.path.append(path.dirname(__file__))
from datetime import datetime,timedelta
from Utils.DataFrame import *
from Utils.Database import conn

##########活动管理与查看，加入#############
def actvt_list(userId):
  return

def actvt_create(data):
  '''input data,return generated actvtId'''
  return 

def actvt_join(userId,):
  '''join a actvt created by others'''
  return 

def actvt_del(actvtId,userId=-1):
  '''delete a actvt,pay attention to check user's Permission'''
  return

def actvt_update(actvtId):
  return