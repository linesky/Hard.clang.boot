import sys
def splitss(s:str):
    ii=0
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    for s1 in ss:
        print(s1)




def readstdin(arg1:str):

    f1=open(arg1,"r")
    ss=f1.read()
    f1.close()
    splitss(ss)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1])





