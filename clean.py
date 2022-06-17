import shutil,os
try:
  shutil.rmtree("DataBase")
  os.remove("cfg.json")
  shutil.rmtree("Upload")
except:pass

try:
  os.makedirs("Upload/tmp")
  with open("Upload/tmp/test.txt","w+") as fw:
    fw.write("test file")
except:pass