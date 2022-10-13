import os
import hashlib

list = []
for file in os.listdir():
  with open(file,'rb') as fp:
    data = fp.read()
    f_md5 = hashlib.md5(data).hexdigest()
    if list.count(f_md5) == 0:
        list.append(f_md5)
    else:
        os.system('rm '+str(file))
