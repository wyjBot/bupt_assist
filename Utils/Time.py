#时间是深拷贝
from cgitb import reset
from datetime import datetime,timedelta
import sys,os.path as path
sys.path.append(path.dirname(__file__))
import Cfg;cfg=Cfg.cfg
realnow=datetime.now 
fromstr=datetime.fromisoformat
strptime=datetime.strptime


def now():
  cfg['rate']=int(cfg['rate'])
  nowtm=cfg['now']
  nowtm+=(realnow()-cfg['rate_time_b'])*cfg['rate']
  return nowtm
def strnow():
  return str(now())

def resetTo(tgt_tim:datetime):
  _now()
  cfg['now']=tgt_tim



def rate(num:int):
  if num<1: 
    return "错误,最小为一"
  cfg['rate']=num
  _now()

def _now():
  rate=int(cfg['rate'])
  cfg['now']+=(realnow()-cfg['rate_time_b'])*cfg['rate']
  cfg['rate_time_b']=realnow()
  return cfg['now']

def stop():
  _now()
  cfg['stop']=True

def start():
  cfg['rate_time_b']=realnow()
  cfg['stop']=False

if __name__=="__main__":
  print(_now())
  rate(60)
  resetTo(datetime(2000,1,1))
  print(now())