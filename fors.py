import subprocess
import sys
def readstdin(arg1:int,arg2:int,arg3:str):
    for n in range(arg1,arg2):
        subprocess.run([arg3 ,str(n)])
    

    
print("\x1b[43;37m")
if len(sys.argv)>3:
    readstdin(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])





