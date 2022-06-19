import os,sys,os.path as path
sys.path.append(path.dirname(__file__))
filedir=path.join(path.dirname(path.dirname(__file__)),"Upload/")

def cleanFile():
  for file in os.listdir(filedir):
    if file[-2:]!="cc":
      try:os.remove(path.join(filedir,file))
      except Exception as e:pass