import tkinter as tk
from tkinter.ttk import Label

ventana = tk.Tk()
etiqueta = Label(ventana,text='HAY DOS SCROLLBAR, UNO VERTICAL Y OTRO HORIZONTAL')
etiqueta.pack()
ventana.title("Scrollbar")
scrollbar_vertical = tk.Scrollbar(ventana)
scrollbar_vertical.pack(side='right',fill='y')
texto = tk.Text()
scrollbar_vertical.config(command=texto.yview)
texto.config(yscrollcommand=scrollbar_vertical.set)
texto.pack(side='left',fill='both',expand=True)
#BARRAS HORIZONTALES
scrollbar_horizontal = tk.Scrollbar(ventana,orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(fill='x')


ventana.mainloop()
