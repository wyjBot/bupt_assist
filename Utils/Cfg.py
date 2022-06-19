import json as js
import os,sys
import os.path as path
from datetime import datetime
import shutil
timelist=['now','rate_time_b']

pwd=path.dirname(path.dirname(__file__))+"/"
cfgPwd=pwd
cfgFile=cfgPwd+"cfg.json"

class Cfg(dict):
  def __init__(self):
    self.loadCfg()

  def saveCfg(self):
    global pwd,cfgFile
    #enstr time
    try:
      fr=open(pwd+"Control/cfg.lock","r")
      ltime=js.load(fr)['time']
      if datetime.timestamp(datetime.now())-ltime<60: return
      else:fr.close()
    except:pass
    with open(pwd+"Control/cfg.lock","w+") as fw:
      js.dump({"time":datetime.timestamp(datetime.now())},fw)

    self.update({'timelist':list()})
    timelist=self['timelist']
    for key in self:
      if type(self[key])==datetime:
        timelist.append(key)
        self.update({key:str(self[key])})
    #write to file
    try:
      fw=open(cfgFile,"w+") 
      js.dump(self,fw)
      fw.close()
    except: print("save cfg failed")
    #revert timetype
    for key in timelist:
      if key in self:
        self.update({key:datetime.fromisoformat(self[key])})

  def __setitem__(self,key,value):
      dict.__setitem__(self,key,value)
      # print("changed")
      self.saveCfg()

  def loadCfg(self):
      global pwd,cfgFile
      cronLock=0;upfileId=0
      try:
        with open(cfgFile,"r+") as fr: _cfg=js.load(fr)
        self.update(_cfg)
        for key in timelist:
            self.update({key:datetime.fromisoformat(self[key])})
      except:
        print("配置文件损坏,已重置为默认值")
        init=dict()
        init['file_sum']=0
        init['user_sum']=0
        init['rate']=1
        init['now']=datetime.now()
        self.update(init)
        self.saveCfg()
        del init
      #Calibration time
      self['rate_time_b']=datetime.now()
      #folder
      try:
        shutil.rmtree(pwd+"tmp")
      except: pass
      try:
        os.makedirs(pwd+"tmp")
        os.makedirs(cfgPwd)
      except:pass



cfg=Cfg()