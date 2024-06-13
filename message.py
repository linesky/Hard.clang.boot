import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os
import sys
from datetime import date
import time 
import sys


class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("clock")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=60)
        self.text_area.pack(pady=10)

        # Botões
        
        
        
        try:
            filename="/tmp/"+sys.argv[1]
            print(filename)
            while True:

                f1=open("/tmp/"+sys.argv[1])
                r=f1.read()
                f1.close()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END,r )
                
                self.root.update()
                time.sleep(4)
        except:
           a=0
           
    def execute_command(self, command,show:bool):
        try:
            
                result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
                self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    

    
        




if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
