import sys
import os
def srun(data):
	os.system(data)
		
def scommand(data):
	datas=data.split(";")
	for n in datas:
		srun(n)
	
def sline(argvs):
	f1=open(argvs,"r")
	nn=f1.read()
	f1.close()
	nnn=nn.split("\n")
	for n in nnn :
	        
		
		if n!="":
			if n!="\n":
				if n=="EXIT":
				    return None
				if n=="exit":
				    return None 	
				scommand(n)
			else:
			    return None	
		else:
		    return None		
	
	
print("\x1bc\x1b[43;37m")	
if len(sys.argv)>1:
    sline(sys.argv[1])
