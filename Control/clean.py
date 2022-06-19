import shutil,os
import os,sys,time,os.path as path
pwd=path.dirname(path.dirname(__file__))+"/"
try:
  shutil.rmtree(pwd+"DataBase")
  os.remove(pwd+"cfg.json")
  shutil.rmtree(pwd+"Upload")
except:pass

try:
  os.makedirs(pwd+"Upload/tmp")
  with open(pwd+"Upload/tmp/test.txt","w+") as fw:
    fw.write("test file")
except:pass