import sys
def splitss(s:list,i:int):
    for s1 in s:
        print(s1)



def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    ss=f1.read()
    f1.close()
    s=ss.replace("\r","\n")
    s=s.replace("\n\n","\n")
    s=s.replace("\t"," "*arg1)
    sss=s.split("\n")
    splitss(sss,arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





