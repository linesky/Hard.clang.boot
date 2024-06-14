import sys
def splitss():
    s=""
    print("to exit press empty line...")
    for s1 in range(65000):
        a=input("")
        if a=="":
            break
        s=s+"\n"+a
    return s

def readstdin(arg1:str):

    print(arg1)
    ss=splitss()
    f1=open(arg1,"w")
    f1.write(ss)
    f1.close()

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin(sys.argv[1])





