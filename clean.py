import shutil,os
shutil.rmtree("DataBase")
try:
  os.makedirs("Upload/tmp")
except:pass