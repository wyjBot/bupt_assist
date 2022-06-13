import os,sys,os.path as path
sys.path.append(path.dirname(__file__))
import compress as cpr
import shutil as st
import Time
import Cfg;cfg=Cfg.cfg
from Log import log
from database import conn

tb=conn.create("file")

def saveFile(path:str):
  cfg["file_sum"]+=1
  fileId=cfg["file_sum"]
  name=path.basename(path)
  os.rename(path,path+"#123")
  time=Time.now()
  tb.insert({"id":fileId,"naem":name,"path":path,"time":time})
  return fileId

def getFile(fileId:int):
  line=tb.find_one({"id":fileId})
  return line
