import sys
def splitss(s:str):
    ss=s.split("\n")
    ii=len(ss)
    ss.sort()
    for s1 in ss:
        print(s1)
        


def readstdin(arg1:str,arg2:str):

    f1=open("/dev/stdin","r")
    s=f1.read()
    f1.close()
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    arg11=arg1.replace("\\n","\n")
    arg11=arg11.replace("\\r","\r")
    arg11=arg11.replace("\\t","\t")
    arg11=arg11.replace("\\s"," ")
    arg22=arg2.replace("\\n","\n")
    arg22=arg22.replace("\\r","\r")
    arg22=arg22.replace("\\t","\t")
    arg22=arg22.replace("\\s"," ")
    s=s.replace(arg11,arg22)
    splitss(s)
    

    
print("\x1b[43;37m")
if len(sys.argv)>2:
    readstdin(sys.argv[1],sys.argv[2])





