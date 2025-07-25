import datetime
import tkinter as tk
from cProfile import label
from tkinter import StringVar, Entry
from tkinter.ttk import Label, Button
from datetime import  date,time,datetime

ventana =tk.Tk()
ventana.title("Calculadora de Edad")
#Título de la ventana

titulo = Label(ventana,text='CALCULADORA DE EDAD',font=('Arial',16,'bold'),foreground='red')
titulo.pack(side='top')

day = datetime.today()
dia = Label(ventana,text=f"Hoy es {datetime.today()}")
dia.pack()
nombre_var = tk.StringVar()
fecha_var = StringVar()
resultado_var  =StringVar()
def calcular_edad():
    global day
    try:
        fecha_nacimiento = datetime.strptime(fecha_var.get(),'%d/%m/%Y')
        hoy = datetime.today()
        edad_dias = (day-fecha_nacimiento).days

        anios = edad_dias//365
        meses = (edad_dias%365)//30
        dias = (edad_dias%365) %30

        resultado = f"{nombre_var.get()}, tienes {anios} años, {meses} meses y {dias} días de vivir"
        resultado_var.set(resultado)
        despedida = Label(ventana,text='MUCHAS GRACIAS POR TU ELECCIÓN :)',font=('Arial',12,'bold'),foreground='green')
        despedida.pack()
    except Exception as e:
        resultado_var.set("Formato incorrecto, usa dd/mm/yyyy")
#Widgets

#Botón de calcular edad
Label(ventana,text='Tu nombre:').pack()
entrada_nombre = tk.Entry(ventana,textvariable=nombre_var)
entrada_nombre.pack()

#Fecha de nacimiento
label_fecha = Label(ventana,text='Fecha de nacimiento(dd/mm/yyyy)')
label_fecha.pack()
entrada_fecha = Entry(ventana,textvariable=fecha_var)
entrada_fecha.pack()

#Botón de calcular
boton_calcular = Button(ventana,text='CALCULAR EDAD',command=calcular_edad)
boton_calcular.pack()

#Mostrar resultado
resultado_label = Label(ventana,textvariable=resultado_var,foreground='blue',font=('Arial',12,'bold'),wraplength=350)
resultado_label.pack()


ventana.mainloop()