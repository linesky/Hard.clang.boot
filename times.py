import subprocess
from datetime import datetime
from datetime import timedelta
import sys
def readstdin():
    t=datetime.now()
    subprocess.run([sys.argv[1],sys.argv[2]])
    tt=datetime.now()
    t=tt-t
    print(t)
    
print("\x1b[43;37m")
if 0==0:
    readstdin()





