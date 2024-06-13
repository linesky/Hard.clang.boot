import sys
def splitss(s:str):
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    for s1 in ss:
        print(s1)
        


def readstdin():
    ss:str=""
    i=len(sys.argv)-1
    if i<0:
        i=0
    for ii in range(i):
        ss=ss+" "+sys.argv[ii+1]
    splitss(ss)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin()


