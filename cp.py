import sys


def readstdin(arg1:str,arg2:str):
    if arg1==arg2:
        return
    f1=open(arg1,"r")
    ss=f1.read()
    f1.close()
    
    f1=open(arg2,"w")
    f1.write(ss)
    f1.close()
    
    

    
print("\x1b[43;37m")
if len(sys.argv)>2:
    readstdin(sys.argv[1],sys.argv[2])





