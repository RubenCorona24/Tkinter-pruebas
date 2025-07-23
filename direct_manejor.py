import tkinter as tk
from tkinter import filedialog
import os

ventana = tk.Tk()
def seleccionar_directorio():
    direct = filedialog.askdirectory()
    if direct:
        listbox.delete(0,tk.END)
        for file in os.listdir(direct):
            listbox.insert(tk.END,file)

listbox = tk.Listbox(ventana)
listbox.pack(expand=True,fill='both')
seleccionar_button = tk.Button(ventana,text='SELECCIONAR DIRECTORIO', command=seleccionar_directorio)
seleccionar_button.pack()





ventana.mainloop()