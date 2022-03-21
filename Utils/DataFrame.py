import numpy as np

tim=str  # tim为cron格式的字符串 "* * * * * *" "分 时 日 月 周 年" 详见参考文档

#************************[1]的任务*******************#
class crood: #二维坐标
  def __init__(self,x,y):
    self.x=-1
    self.y=-1

class rect:
  def __init__(self,addr:crood,len,width):
    self.addr=addr  #右上角坐标


class build:
  def __init__(self,name:str,addr:rect,id:int,type,xb,yb,xlen,ylen):
    self.name="undefined"# 如3号教学楼
    self.addr=addr #坐标
    self.type=type #类型:教学楼、办公楼、宿舍楼、体育馆、学生活动中心,公交车站
    #方便起见,自行车道路也可视为build类
    self.id=id     
    #xb,yb确定建筑物右上角坐标,xlen,ylen确定建筑物长和宽,方便起见建筑物均为矩形...
    self.xb=xb;self.yb=yb
    self.xlen=xlen;self.ylen=ylen

class clsroom: #似乎多余了,用不到
  def __init__(self,roomId:str,buildId:int) :
    self.id=roomId #教室号 如312
    self.buildid=buildId

class busRoute:
  def __init__(self):
    self.stops=list() #站点列表
    self.stopsTimeGap=dict() #站点间时间间隔
    #具体由[1]根据需求自行完善

class pbusRoute(busRoute):#公共汽车
  def __init__(self):pass

class rbusRoute(busRoute):#定点班车
  def __init__(self):pass

#地图的二维数组,belong为该坐标归属的建筑物id(即使道路也有id)
mapel=np.dtype([('belong', np.int32),('crowdLevel', np.int32)])
map=np.zeros((10000,10000),dtype=mapel)


#************************[3]的任务***********************#
class course:
  def __init__(self,name:str,Id,campusId,buildId,Time:tim,duration):
    self.name=name
    self.Id=Id #课程编号
    self.campusId=campusId
    self.buildid=buildId
    self.time=Time
    self.duration=duration#每次活动/课程持续时间,int型以分钟为单位
    #课程教师、参与学生,电子资料、纸质资料、作业信息和考试信息等由[3]自行完善


class activity(course): #活动与课程的需求基本一样,直接继承课程就行了:
  def __init__(self,name:str,campusId,Id,buildId,Time:tim,duration):
    super(course, self).__init__(name,Id,campusId,buildId,Time,duration)
    pass

class user:#用户信息以json格式存储在user.txt中
  def __init__(self,user_status:str,id:int,phone:int,passwd:str):
    self.user_status=user_status
    self.id=id
    self.phone=phone
    self.passwd=passwd
    #模板,具体类函数等由[3]自行完善
 
