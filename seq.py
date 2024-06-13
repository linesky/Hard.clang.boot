import sys

def readstdin():
    ss:str=""
    for ii in range(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])):
        ss=ss+str(ii)+" "
    print(ss.strip())
    

    
print("\x1b[43;37m")
if len(sys.argv)>3:
    readstdin()


