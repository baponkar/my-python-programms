import os

print(os.getpid())

print(os.getgid())


#creating subprocess
import subprocess

ret = subprocess.getoutput('sleep 4')
print(ret)
