import sys
def splitss(s:str):
    ss=s.split("\n")
    ii=len(ss)
    counters:float=0
    for s1 in ss:
        try:
            ff:float=float(s1)
            counters+=ff
            print(str(counters)+"\t=\t"+s1)
        except:
            a=0
        


def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    s=f1.read()
    f1.close()
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    
    splitss(s)
    

    
print("\x1b[43;37m")
if 0==0:
    readstdin(0)





