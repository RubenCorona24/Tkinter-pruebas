import tkinter as tk
from tkinter import Checkbutton, BooleanVar

ventana = tk.Tk()
ventana.geometry('600x900')

label1 = tk.Label(ventana,text='LABEL 1',fg='red',font=('Arial',12,'bold'))
label2 = tk.Label(ventana,text='LABEL 2',fg='red',font=('Arial',12,'bold'))
label3 = tk.Label(ventana,text='LABEL 3',fg='red',font=('Arial',12,'bold'))
label1.grid(row=0,column=0)
label2.grid(row=1,column=1)
label3.grid(row=2,column=1)
def cambiar_color():
    label1.config(fg='green',font=('Arial',10,'bold'))

def cambiar_label2():
    label2.config(fg='green', font=('Arial', 10, 'bold'))
def cambiar_label3():
    label3.config(fg='green', font=('Arial', 10, 'bold'))

boton = tk.Button(ventana,text='Cambiaar color label1',command=cambiar_color)
boton2 = tk.Button(ventana,text='Cambiaar color label2',command=cambiar_label2)
boton3 = tk.Button(ventana,text='Cambiaar color label3',command=cambiar_label3)
boton.grid(row=3,column=3)
boton2.grid(row=3,column=4)
boton3.grid(row=3,column=5)

checador = BooleanVar()

label4 = tk.Label(ventana,text='LABEL 4',fg='red',font=('Arial',12,'bold'))
label4.grid(row=3,column=6)
def cambiar_label4():
    if checador.get():
        label4.config(fg='green', font=('Arial', 10, 'bold'))
michecl = Checkbutton(ventana,text='Apriétame si quieres cambiar al label 4',fg='brown',font=('Arial',12,'bold'),variable=checador,command=cambiar_label4)
michecl.grid(row=4,column=2)


ventana.mainloop()