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
        self.text_area = tk.Text(self.root, height=50, width=200)
        self.text_area.pack(pady=10)

        # Botões
        
        
        
        try:
            while True:
               
                self.text_area.delete(1.0, tk.END)
                #self.text_area.insert(tk.END,time.asctime() )
                self.execute_command('sh -c "ps -elf"',True)
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
