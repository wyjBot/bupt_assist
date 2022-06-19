import shutil,os
import os,sys,time,os.path as path
pwd=path.dirname(path.dirname(__file__))
pjoin=path.join
try:
  shutil.rmtree(pjoin(pwd,"Database"))
  shutil.rmtree(pjoin(pwd,"Upload"))
  os.remove(pjoin(pwd,"cfg.json"))
  os.remove(pjoin(pwd,"Control/cfg.lock"))
except Exception as e:
  print(e,"In Clean")

try:
  os.makedirs(pjoin(pwd,"Upload/tmp"))
  with open(pjoin(pwd,"Upload/tmp/test.txt"),"w+") as fw:
    fw.write("test file")
except:pass