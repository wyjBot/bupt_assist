#put the file uploaded to root dir /Upload and classify them by time
#the compress tools is under package utils
import Utils.compress as cmpr

###########task_mgmt###########
def list_crouse_task(courseId):
  ret={
   "1":{"name":"第一章习题","taskId":234,} ,
   "2":{"name":"第二章习题","taskId":316,} ,
   "3":{"name":"第二章习题(2)","taskId":536,}, 
  }
  pass

def list_user_task(userId):
  ret= {
   "1":{"name":"第一章习题", "courseName":"计算机网络", "courseId":24,"taskId":234,} ,
   "2":{"name":"第一周", "courseName":"编译原理", "courseId":12,"taskId":231,} ,
  }
  return

def create_course_task(courseId,data):
  '''parameter data will be a dict,contain key
  name, des, attentionId,Deadline
  the func return taksId
  '''
  pass

def view_task(taskId):
  '''return a dict contain key same as "create_task" '''
  return

######hmwk_mgmt############

def view_hmwk(hmwkId):
  '''ret a dict contain all hmwk version '''
  return

def rollback_hmwk(hmwkId,version):
  """reset hmwk version to old ret 1 when suc
  return 0 when creates failed because of noexist id"""
  return 

def submit_hmwk(taskId,userId,data):
  """generate and ret a hmwkId for the taskId of user"""
  """return -1 when creates failed because of insuffcient data or wrong userId/taskId"""
  return

def update_hmwk(hmwkId,data):
  '''return now versionId'''
  """return -1 when update failed because of insuffcient data"""
  return