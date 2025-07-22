import tkinter as tk
from tkinter import BooleanVar, Button, Checkbutton, StringVar, Entry, Label, IntVar, Radiobutton, Toplevel, Menubutton
from tkinter.ttk import Checkbutton, Combobox
ventana = tk.Tk()
ventana.geometry("900x900")
#PRACTICAR CON VARIABLES DE CONTROL
texto = StringVar()
texto.set('texto añadido')

#EJEMPLO CON ETIQUETA
#entrada = Entry(ventana,textvariable=texto)
#entrada.pack()
#etiqueta = Label(ventana)
#etiqueta.pack()
#FUNCION DE ACTUALIZAR ETIQUETA
#def act_etiqueta(*args):
 #   etiqueta.config(text=texto.get())
#texto.trace('w',act_etiqueta)

#LAS Intvar()
#entero = IntVar(value=42)
#opcin1 = Radiobutton(ventana,text='Opción1',variable=entero,value=1)
#opcin1.pack()
#opcin2 = Radiobutton(ventana,text='Opción2',variable=entero,value=2)
#opcin2.pack()
#def actualizar(*args):
 #   print(entero.get())
#ntero.trace('w',actualizar)
#USAR DOUBLEVAR
#BOOLEANVAR
booleano = BooleanVar(value=True)
casilla = tk.Checkbutton(ventana,text='Aceptar',variable=booleano)
casilla.pack()
def actualizar(*args):
    print(f"Opción elegida: {booleano.get()}")
booleano.trace('w',actualizar)

labelmio = Label(ventana,text='PRIMERA OPCIÓN, SOY VERDE',fg='green')
labelmio.pack()

entero2 = IntVar(value=30)
radio = Radiobutton(ventana,text='Primera opción',variable=entero2,value=1)
radio2 = Radiobutton(ventana,text='Srgunda opción',variable=entero2,value=2)
radio.pack()
radio2.pack()
boton_comando = Button(ventana,text='OPCIÓN 1 PARA HABILITAR',state='disabled')
boton_comando.pack()
def mostrar(*args):
    if entero2.get() == 2:
        labelmio.config(text='SEGUNDA OPCIÓN, SOY ROJO',fg='red')
        boton_comando.config(text='OPCIÓN 1 PARA HABILITAR',state='disabled')
    elif entero2.get() == 1:
        labelmio.config(text='PRIMERA OPCIÓN. SOY VERDE', fg='green')
        boton_comando.config(state='normal',text='BOTÓN HABILITADO')

entero2.trace('w',mostrar)
ventana.mainloop()
