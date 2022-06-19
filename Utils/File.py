import os,sys,os.path as path
sys.path.append(path.dirname(__file__))
import compress as cpr
import shutil as st
import Time
import compress
import Cfg;cfg=Cfg.cfg
from Log import log
from database import conn

filedir=path.dirname(__file__)+"/../Upload/tmp/"

tb=conn.create("file")

def saveFile(opath:str,copy=False)->int:
  cfg["file_sum"]+=1
  fileId=cfg["file_sum"]
  name=path.basename(opath)
  fpath=path.join(path.dirname(opath),str(cfg["file_sum"])+name)
  if copy:
    st.copyfile(opath,fpath)
  else:
    os.rename(opath,fpath)
  time=str(Time.now())
  tb.insert({"id":fileId,"name":name,"path":fpath,"time":time})
  return fileId

def getFile(fileId:int):
  fileId=int(fileId)
  line=tb.find_one({"id":fileId})
  try:
    fpath=line['path']#.split('#')[0]
  except Exception as e:
    fpath=path.dirname(__file__)+"/../Upload/tmp/test.txt"
  return fpath

# print(getFile(5))
