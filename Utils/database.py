import os,sys
import os.path as path
import json as js
import shutil
pwd=path.dirname(path.dirname(path.abspath(__file__)))+"/Database/"# father directory

class Table:
  def __init__(self,tbname):
    self.name=tbname
    try: 
      fr=open(pwd+tbname+".json")
      self.lines=js.load(fr)
      fr.close()
    except:self.lines=list()
    try: 
      fr=open(pwd+tbname+".ukVals")
      self.ukVals=js.load(fr)
      self.ukeys=list(self.ukVals.keys())
      fr.close()
    except:
      self.ukeys=list()
      self.ukVals=dict()

  def set_ukey(self,keyX):
    if keyX in self.ukeys: return 1
    self.ukeys.append(keyX)
    self.ukVals[keyX]=list()
  def del_ukey(self,keyX):
    if keyX not in self.ukeys: return 1
    del self.ukVals[keyX]
    self.ukeys.remove(keyX)
  def show_ukey(self):
    return self.ukeys.copy()

  def find_one(self,fiter):
    '''
      adapt to find precise one with ukey
      while have many item, the earliest will be response 
    '''
    for x in self.lines:
      for key in fiter:
        if x[key]!=fiter[key]: continue
      return x.copy()

  def find_all(self,fiter):
    '''adapt for fuzzy lookup with some value'''
    ret=list()
    for x in self.lines:
      flag=True
      for key in fiter:
        if x[key]!=fiter[key]: flag=False
      if flag:ret.append(x.copy())
    return ret

  def update(self,fiter,newline):
    """If data existing,then Update it,else insert """
    items=self.find_all(fiter)
    if len(items)==0:
      self.insert(newline)
    if len(items)==1:
      items[0].update(newline)
      self._save()
    if len(items)>=2:
      raise ValueError("find Multiple eligible lines")

  def insert(self,dataX):
    keysX=dataX.keys()
    for ukey in self.ukeys:
      if ukey not in dataX:
        raise Exception("All ukey should't be empty")
      if dataX[ukey]==None or dataX[ukey] in self.ukVals[ukey]:
        raise Exception(f"ukey:{ukey} has been existing")
    for ukey in self.ukeys:
      self.ukVals[ukey].append(dataX[ukey])
    self.lines.append(dataX)
    self._save()
    
  def remove(self,dataX):
    '''必须传入完整的数据才可删除'''
    for ukey in self.xdata:
      self.ukVals[ukey].remove(dataX[ukey])
    self.lines.remove(dataX)
    self._save()
  
  def _save(self):
      fw=open(pwd+self.name+".json","w+")
      js.dump(self.lines, fw)
      fw.close()
      fw=open(pwd+self.name+".ukVals","w+")
      js.dump(self.ukVals, fw)
      fw.close()

  def _bak(self):
    # shutil.move()
    pass

class DateBase:
  def __init__(self,bufferTime=0):
    # print(os.getcwd())
    try: os.makedirs(pwd+"db")
    except:pass
    try:
      fr=open(pwd+"db/tbs.json")
      self.tbsIndex=js.load(fr)
      fr.close()
    except:self.tbsIndex=list()
    self.all=dict()
    for x in self.tbsIndex:
      self.all[x]=Table(x)
        
  def __getitem__(self, tbname):
    if tbname not in self.tbsIndex:
      # raise NameError("Try to access unexisting table")
      return None
    return self.all[tbname]

  def create(self,tbname):
    if tbname in self.tbsIndex:
      raise NameError("duplicate with existing table")
    self.all[tbname]=Table(tbname)
    self.tbsIndex.append(tbname)
    self._save()
    return self.all[tbname]

  def delete(self,tbname):
    if tbname not in self.tbsIndex:
      raise NameError("Try to delete unexisting table")
    self.tbsIndex.remove(tbname)
    self.all[tbname].delete()
    del self.all[tbname]
    self._save()

  def _save(self):
    fw=open(pwd+"db/tbs.json","w+")
    js.dump(self.tbsIndex,fw,ensure_ascii=False)
    fw.close()


if __name__ == '__main__':
  a=DateBase()
  if not a["Dfdf"]:a.create("Dfdf")
  a["Dfdf"].update({"name":"wyj"},{"name":"wyj","id":2020222333})
  tb=a["Dfdf"]
  tb.set_ukey("id")
  a["Dfdf"].update({"name":"bd1"},{"name":"bd1","id":2020222333})
  tb=a.create("users")
