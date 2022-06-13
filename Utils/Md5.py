
import hashlib
def en(txt):
  md5Obj = hashlib.md5(b'md5secert')
  md5Obj.update(txt.encode('utf-8'))
  ret = md5Obj.hexdigest()
  return ret