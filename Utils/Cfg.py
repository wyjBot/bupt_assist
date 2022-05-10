import json as js
import os,sys
import os.path as path
import shutil

class Cfg:
  def __init__(self):
    self.load_cfg()

  def save_cfg():
      global pwd,cfgPwd
      global cfgs
      cfgfile=cfgPwd+"cfg.json"
      try:
          with open(cfgfile,"w+") as fw:
              js.dump(cfgs,fw)
      except:pass


  def load_cfg():
      global cfgs
      global cronLock
      global pwd,cfgPwd
      cronLock=0;upfileId=0
      pwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/"
      cfgPwd=os.path.join(pwd,"config")+"/"
      cfgfile=cfgPwd+"cfg.json"
      try:
          with open(cfgfile,"r+") as fr: cfgs=js.load(fr)
          upfileId=cfgs['upfileId']
      except:pass
      try:
          shutil.rmtree(pwd+"tmp")
      except:pass
      try:
          os.makedirs(pwd+"tmp")
          os.makedirs(cfgPwd)
      except:pass


cfg=Cfg