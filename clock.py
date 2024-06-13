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
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)

        # Botões
        
        
        
        try:
            while True:
               
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END,time.asctime() )
                root.update()
                time.sleep(2)
        except:
           a=0
           

    
        




if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
