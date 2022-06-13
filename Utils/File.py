import sys,os.path as path
sys.path.append(path.dirname(__file__))
import compress as cpr
import shutil as st
import Cfg;cfg=Cfg.cfg

def saveFile(path:str):
  cfg["file_sum"]+=1
  fileId=cfg["file_sum"]
  return fileId
