import sys
def splitss(s:str,i:int):
    ii=i+1
    
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    if ii>len(ss):
        ii=len(ss)
    for s1 in range(ii):
        print(ss[s1])



def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    ss=f1.read()
    f1.close()
    splitss(ss,arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





