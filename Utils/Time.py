#时间是深拷贝
from cgitb import reset
from datetime import datetime,timedelta
import Cfg;cfg=Cfg.cfg
realnow=datetime.now 

def now():
  cfg['now']+=(realnow()-cfg['rate_time_b'])*cfg['rate']
  cfg['rate_time_b']=realnow()
  return cfg['now']

def resetTo(tgt_tim:datetime):
  cfg['now']=tgt_tim

def rate(num:int):
  if num<1: 
    return "错误,最小为一"
  cfg['rate']=num

if __name__=="__main__":
  rate(3600)
  resetTo(datetime(1999,1,1))
  print(now())