import subprocess
import sys
def readstdin(arg1:str):
    f1=open("/dev/stdin","r")
    ss=f1.read()
    f1.close()
    
    for n in ss:
        subprocess.run([arg1 ,n.strip()])
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1])





