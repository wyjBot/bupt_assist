import os,sys,time,os.path as path
sys.path.append(path.dirname(__file__))
import DataFrame,Time
absdir=path.dirname(__file__)
logdir=path.dirname(absdir)+"/Control/log/"
actPwd=logdir+"action.log"
infoPwd=logdir+"info.log"
warnPwd=logdir+"warn.log"
errorPwd=logdir+"error.log"

class Log:
  def __init__(self):
    if not path.exists(logdir): os.mkdir(logdir)

  def write(mess,Level=0):
    """
    0=act 1=info 2=warn 3=error
    """
    if Level==0: fw=open(actPwd,"a+")
    if Level==1: fw=open(infoPwd,"a+")
    if Level==2: fw=open(warnPwd,"a+")
    if Level==3: fw=open(errorPwd,"a+")
    fw.write(str(Time.now())+" : "+mess+"\n")
    fw.close()

log=Log()