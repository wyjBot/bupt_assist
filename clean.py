import shutil,os
shutil.rmtree("DataBase")
shutil.rmtree("Upload")

try:
  os.makedirs("Upload/tmp")
  with open("Upload/tmp/test.txt","w+") as fw:
    fw.write("test file")
except:pass