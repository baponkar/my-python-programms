import os

os.chmod('myfile.txt',0o400)


#another process

import stat
os.chmod('myfile.txt',stat.S_IRUSR)

#changng file ownership
uid = 5

gid = 22
os.chown('mfile.txt',uid,gid)

