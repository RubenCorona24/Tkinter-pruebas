import tkinter
import tkinter as tk
from tkinter import IntVar, Entry, Label, Checkbutton, Radiobutton, Menubutton
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("CONVERTIDOR DE CELCIUS A Fahrenheit") #título en label
ventana.geometry('900x600')
title = Label(ventana,text='CONVERTIDOR CELCIUS-FAHRENHEIT',font=("Arial",12,'bold'),foreground='red')
title.pack(side='top',pady=10)
option = IntVar()
boton_check = Radiobutton(ventana,text='Obtener Celcius',variable=option,value=1)
boton_check.pack(pady=5)
boton_check2 = Radiobutton(ventana,text='Obtener Fahrenheit',variable=option,value=2)
boton_check2.pack(pady=5)  #RadioButton para grados
label_mostrar = Label(ventana)
entrada = Entry()
otro_label = Label(ventana)
def mostrar_resultado(): #función para entradas
    global otro_label
    global label_mostrar
    global entrada
    resultado = option.get()
    if resultado == 1:
        label_mostrar.config(text='Has elegido la opción de Celcius')
        label_mostrar.pack()
        entrada.delete(0, tk.END)
        entrada.insert(0,'Valor en Fahrenheit')
        entrada.pack()


    else:
        label_mostrar.config(text='Has elegido la opción de Fahrenheit')
        label_mostrar.pack()
        entrada.delete(0,tk.END)
        entrada.insert(0, 'Valor en Celcius')
        entrada.pack()
label_resultado = Label(ventana, text="", font=("Arial", 12))
label_resultado.pack(pady=5)
def calcular():  #Función para mostras resultados
    try:
        faren = float(entrada.get()) * (9/5) + 32
        celcius = (float(entrada.get()) - 32) * (5/9)
        if option.get() == 1:
            label_resultado.config(text=f'{entrada.get()} °F → {round(celcius, 2)} °C')
        elif option.get() == 2:
            label_resultado.config(text=f'{entrada.get()} °C → {round(faren, 2)} °F')
    except ValueError:
        messagebox.showerror('Error','Opción Inválida') #Message box de error




boton = tk.Button(ventana,text='MOSTRAR',command=mostrar_resultado)
boton.pack(pady=5)
boton_calcular= tk.Button(ventana,text='CALCULAR',command=calcular)
boton_calcular.pack(pady=5)  #Empacamos los botones

ventana.mainloop()