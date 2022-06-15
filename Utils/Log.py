import os,sys,time,os.path as path
sys.path.append(path.dirname(__file__))
import DataFrame,Time
absdir=path.dirname(__file__)
logdir=path.dirname(absdir)+"/Control/log/"
actPwd=logdir+"action.log" #用户操作
warnPwd=logdir+"warn.log" #用户警告
infoPwd=logdir+"info.log" #管理员通知信息/轻度错误
errorPwd=logdir+"error.log" #系统致命报错


def log(mess,level=0):
  if not path.exists(logdir): os.mkdir(logdir)
  """
  0=act 1=info 2=warn 3=error
  """
  if level==0: fw=open(actPwd,"a+",encoding="utf-8")
  if level==1: fw=open(warnPwd,"a+",encoding="utf-8")
  if level==2: fw=open(infoPwd,"a+",encoding="utf-8")
  if level==3: fw=open(errorPwd,"a+",encoding="utf-8")
  fw.write(str(Time.now())+" : "+mess+"\n")
  fw.close()


if __name__ == '__main__':
  log("Time module test 你好",level=2)
