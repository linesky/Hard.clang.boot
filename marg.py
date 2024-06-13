import sys
def splitss(s:str,i:int):
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    sss=" "*i
    for s1 in ss:
        print(sss+s1)



def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    ss=f1.read()
    f1.close()
    splitss(ss,arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





