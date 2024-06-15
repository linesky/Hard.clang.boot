#!/usr/bin/python3
import sys
def readstdin(arg1:str):

    f1=open(arg1,"w")
    f1.close()
    
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1])





