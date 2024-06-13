import sys

def readstdin():
    ss:str=""
    i=len(sys.argv)-2
    tt=sys.argv[1]
    ttt=tt.split("%")
    if i<0:
        i=0
    ss=ttt[0]
    if len(ttt)==1:
        ss=ttt[0]
    else:
        for ii in range(i):
            ggg=ttt[ii+1]
            if len(ggg)>0:        
                ggg=ggg[1:]
            ss=ss+sys.argv[ii+2]+ggg
    print(ss)
    

    
print("\x1b[43;37m")
if len(sys.argv)>1:
    readstdin()


