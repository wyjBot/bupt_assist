import os,sys,os.path as path
sys.path.append(path.dirname(__file__))
filedir=path.join(path.dirname(path.dirname(__file__)),"Upload/")
import compress as cpr
import shutil as st
import Time
import compress
import Cfg;cfg=Cfg.cfg
from Log import log
from database import conn
import compress as cps


tb=conn.create("file")

def saveFile(opath:str,copy=False)->int:
  cfg["file_sum"]+=1
  fileId=cfg["file_sum"]
  name=path.basename(opath)
  fpath=path.join(filedir,str(cfg["file_sum"])+name)
  if copy:
    st.copyfile(opath,fpath)
  else:
    os.rename(opath,fpath)
  cfpath=cps.file_encode(fpath)
  os.remove(fpath)
  time=str(Time.now())
  tb.insert({"id":fileId,"name":name,"path":fpath,"time":time})
  return fileId

def getFile(fileId:int):
  fileId=int(fileId)
  line=tb.find_one({"id":fileId})
  try:
    fpath=line['path']#.split('#')[0]
    cfpath=fpath.split('.')[0]+".cc"
    print(cfpath)
    cps.file_decode(cfpath)
  except Exception as e:
    fpath=path.join(filedir,"tmp/test.txt")
  return fpath

# print(getFile(5))
