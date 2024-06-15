import sys
import os
import glob
def splitss(s1:str,s2:str):
    os.rename(s1, s2)

def readstdin(arg1:str,arg2:str):
    splitss(arg1,arg2)
    

    
print("\x1b[43;37m")
if len(sys.argv)>2:
    readstdin(sys.argv[1],sys.argv[2])


