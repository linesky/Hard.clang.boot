import sys
def splitss(s:str,i:int):
    ii:int=0
    iii:int=0
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    iii=len(ss)
    ii=iii-i-1
    if ii<0:
        ii=0
    for s1 in range(ii,iii):
        print(ss[s1])



def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    ss=f1.read()
    f1.close()
    splitss(ss,arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





