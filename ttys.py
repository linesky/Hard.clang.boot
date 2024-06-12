import sys
def splitss(s:str,i:int):
    ii=i-1
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    for s1 in ss:
        if len(s1)<i:
            print(s1)
        else:
            while s1!="":
                if len(s1)<ii:
                    print(s1)
                    s1=""
                else:
                    print(s1[0:ii])
                    s1=s1[ii:]



def readstdin(s:str,arg1:int):

    f1=open(s,"r")
    ss=f1.read()
    f1.close()
    splitss(ss,arg1)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1],int(sys.argv[2]))





