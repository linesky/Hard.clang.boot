from tkinter import *
from tkinter import messagebox

import sys
def splitss(s:str,i:int):
    a:str=""
    ii:int=0
    s=s.replace("\r","\n")
    s=s.replace("\n\n","\n")
    ss=s.split("\n")
    for s1 in ss:
        ii+=1
        print(s1)
        if ii>i:
            ii=0
            a=messagebox.showinfo("ok to continue","continue?")



def readstdin(arg1:int):

    f1=open("/dev/stdin","r")
    ss=f1.read()
    
    splitss(ss,arg1)
    

    
print("\x1b[43;37m")
root=Tk()
root.geometry("100x100")
root.config(bg="yellow")
if len(sys.argv)>1:
    readstdin(int(sys.argv[1]))





