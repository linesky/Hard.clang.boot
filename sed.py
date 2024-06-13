import sys
def splitss(s:str):
    ss=s.split("\n")
    ii=len(ss)
    ss.sort()
    for s1 in ss:
        print(s1)
        


def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    s=f1.read()
    f1.close()
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    s=s.replace(sys.argv[1],sys.argv[2])
    splitss(s)
    

    
print("\x1b[43;37m")
if 0==0:
    readstdin(0)





