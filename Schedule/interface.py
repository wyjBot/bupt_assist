import sys,os.path as path
sys.path.append(path.dirname(__file__))
sys.path.append(path.dirname(path.dirname(__file__)))
import Utils
from Utils.Log import *
from Utils.Time import datetime,timedelta
from Utils.DataFrame import *
from Utils.database import conn

tbNotice=conn.create("notice")
tbActvt=conn["actvt"]
tbUserActvt=conn["userActvt"]
tbCourse=conn["course"]
tbUserCourse=conn["userCourse"]
tbExam=conn["exam"]
##########闹钟管理与查看#############
def notice_list(userId):
  ret=tbNotice.find_all({"userId":userId})
  if not ret:
    log("notice_list",2)
    return [],"还没有加入闹钟"
  log("actvt_list:userId="+userId,0)
  for x in ret:
    x.pop("userId")
    if x["type"]==1:
      x["闹钟类型"]="活动闹钟"
    elif x["type"]==2:
      x["闹钟类型"]="课程闹钟"
    else:
      x["闹钟类型"]="考试闹钟"
    if x["frequncy"]==1:
      x["频率"]="只响一次"
    elif x["type"]==2:
      x["频率"]="每天一次"
    else:
      x["频率"]="每周一次"
      x["星期"]=x.pop("day")
    x["闹钟时间"]=x.pop("time")
  return ret,"这是所有的闹钟"

def notice_available(userId):
  '''return a list of acitvity/course which is able to set a alarm clock'''
  ret=list()
  retactvt=tbUserActvt.find_all({"userId":userId})
  for x in retactvt:
    time1=datetime.strptime(x["time"], "%Y-%m-%d %H:%M:%S")
    time2=now()
    if time2.__le__(time1):#时间在现在的时间之后可以设置闹钟
      ret.append(x)
  retcourse=tbUserCourse.find_all({"userId"})
  retclass=list()
  for x in retcourse:#都可以设置闹钟
    ret.append(x)
    retcourse.append(x["classId"])
  for x in range(len(retclass)-1):
    retexam=tbExam.find_all({"classId":retclass[x]})
    for item in retexam:#时间在现在的时间之后可以设置闹钟
      time1=datetime.strptime(item["开始时间"], "%Y-%m-%d %H:%M:%S")
      time2=now()
      if time2.__le__(time1):
        ret.append(item)
  log("notice_available:userId="+str(userId),0)
  return ret,"这是可以设置闹钟的活动/课程/考试"

def notice_add(userId,data):
  '''input data,return generated noticeId'''
  """
  data={
    "type":1,#1表示活动闹钟,2表示课程闹钟,3表示考试闹钟
    "id":,#对应id
    "frequncy":#1表示单次,2表示每天一次,3表示每周一次
  }
  "time":
  "day":#星期几
  "userId":
  """
  data["userId"]=userId
  if data["type"]==1:
    ret=tbActvt.find_one({"actvtId":data["id"]})
    if not ret:return -1,"不存在这个活动"
    if data["frequncy"]==1:
      data["time"]=ret["time"]
    elif data["frequncy"]==2:
      temptime=datetime.strptime(ret["time"], "%Y-%m-%d %H:%M:%S")
      data["time"]=str(temptime.time())
    elif data["frequncy"]==3:
      temptime=datetime.strptime(ret["time"], "%Y-%m-%d %H:%M:%S")
      data["day"]=temptime.weekday()
      data["time"]=str(temptime.time())
    else:
      return -1,"data频率错误"
  elif date["type"]==2:
    ret=tbActvt.find_one({"id":data["id"]})
    if not ret:return -1,"不存在这个活动"
    if data["frequncy"]==1:
      tempnow=str(now())[0:19]
      temptime=datetime().strptime(tempnow, "%Y-%m-%d %H:%M:%S")
      tempday=temptime.weekday()
      nextday=ret["星期"]-tempday if ret["星期"]-tempday>0 else ret["星期"]-tempday+7
      temptime=temptime+timedelta(days=nextday)
      time1=str(temptime)[10]+" 00:00:00"
      needtime=datetime().strptime(time1, "%Y-%m-%d %H:%M:%S")
      needtime=needtime+timedelta(minutes=(45*(ret["节次"]-1)))
      data["time"]=str(needtime)
    elif data["frequncy"]==2:
      temptime=time(8,0)
      temptime=temptime+timedelta(minutes=(45*(ret["节次"]-1)))
      date["time"]=str(temptime)
    elif data["frequncy"]==3:
      data["day"]=ret["星期"]
      temptime=time(8,0)
      temptime=temptime+timedelta(minutes=(45*(ret["节次"]-1)))
      data["time"]=str(temptime)
    else:
      return -1,"data频率错误"
  elif date["type"]==3:
    ret=tbExam.find_one({"examId":id})
    if not ret:return -1,"不存在这个活动"
    if data["frequncy"]==1:
      data["time"]=ret["开始时间"]
    elif data["frequncy"]==2:
      temptime=datetime.strptime(ret["开始时间"], "%Y-%m-%d %H:%M:%S")
      data["time"]=str(temptime.time())
    elif data["frequncy"]==3:
      temptime=datetime.strptime(ret["开始时间"], "%Y-%m-%d %H:%M:%S")
      data["day"]=temptime.weekday()
      data["time"]=str(temptime.time())
    else:
      return -1,"data频率错误"
  else:
    return -1,"data错误"
  if len(res)==0:
    data["noticeId"]=0
  else:
    data["noticeId"]=(res[len(res)-1])["noticeId"]+1
  tbNotice.insert(data)
  log("notice_add:noticeId="+str(data["noticeId"]),0)
  return data["noticeId"],"已经创建闹钟"

def notice_del(userId,noticeId):
  res=tbNotice.find_one({"userId":userId,"noticeId":noticeId})
  if not res:return 0,"该用户不存在该闹钟"
  tbNotice.remove(res)
  log("notice_del:noticeId="+str(noticeId),0)
  return 1,"已删除该闹钟"

def notice_work(timein,userId):
  res=tbNotice.find_all({"userId":userId})
  ret=list()
  timestr=str(timein)[0:19]
  time=datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
  for x in res:
    timenotice=datetime.strptime(ret["开始时间"], "%Y-%m-%d %H:%M:%S")
    timepre=timenotice+timedelta(seconds=cfg['rate']*-1)
    timelat=timenotice+timedelta(seconds=cfg['rate']*1)
    if timepre.__le__(time) and timelat.__ge__(time):
      ret.append(x["noticeId"])
  return ret,"这是要响的闹钟"
