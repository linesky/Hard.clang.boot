import sys
import os
import glob
def splitss(s1:str):
    os.remove(s1)

def readstdin(arg1:str):
    splitss(arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1])


