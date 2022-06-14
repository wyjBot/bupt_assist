import os,sys,time,os.path as path
sys.path.append(path.dirname(__file__))
import DataFrame,Time
absdir=path.dirname(__file__)
logdir=path.dirname(absdir)+"/Control/log/"
actPwd=logdir+"action.log"
infoPwd=logdir+"info.log"
warnPwd=logdir+"warn.log"
errorPwd=logdir+"error.log"


def log(mess,level=0):
  if not path.exists(logdir): os.mkdir(logdir)
  """
  0=act 1=info 2=warn 3=error
  """
  if level==0: fw=open(actPwd,"a+")
  if level==1: fw=open(infoPwd,"a+")
  if level==2: fw=open(warnPwd,"a+")
  if level==3: fw=open(errorPwd,"a+")
  fw.write(str(Time.now())+" : "+mess+"\n")
  fw.close()
