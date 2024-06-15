import sys
import os
import glob
def splitss(s:str):
    files = glob.glob(s)
    ss=""
    c=0
    for s1 in files:
        if c==0:
            ss=s1
        else:
            ss=ss+" "+s1
        c=1
    print(ss)

def readstdin(arg1:str):
    splitss(arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1])
else:
    readstdin("*")



