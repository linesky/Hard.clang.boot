import sys
def splitss(s:str):
    ss=s.split("\n")
    ii=len(ss)
    counters:int=0
    for s1 in ss:
        counters+=1
        print(str(counters)+"\t"+s1)
        


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





