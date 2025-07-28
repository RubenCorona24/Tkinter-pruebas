import tkinter as tk
from tkinter import IntVar, Entry, Label

ventana = tk.Tk()
ventana.title("CONTADOR")
ventana.geometry('900x600')

def calcular_imc():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get()) /100
        imc = peso /(altura**2)
        imc = round(imc,2)
        if imc <18.5:
            estado = 'Bajo peso'
        elif 18.5 <= imc < 25:
            estado = 'Normal'
        elif 25 <=imc <29.9:
            estado = 'Sobrepeso'
        elif imc>30:
            estado  = 'Obesidad'
        resultado.config(text=f'TENEMOS TUS DATOS, IMC: {imc} ESTADO: {estado}')
        resultado.pack()
    except ValueError:
        label_error = Label(ventana,text='HAS INGRESADO MAL LOS NÚMEROS',foreground='red')
        label_error.pack()

title = tk.Label(ventana,text="CALCULADORA DE IMC",font=("Arial",12,'bold'),foreground='red')
title.pack(side='top')  #Título dentro ventana

name = tk.Entry()
name.insert(0,'NOMBRE COMPLETO')
name.pack()
def ver_descripcion():
    label_descripcion = tk.Label(ventana,text=f'Ok {name.get()}, tienes que introducir tu peso y estatura dentro de las secciones,\n tus resulados serán mostrados con el botón: VER RESULTADOS',
                                 foreground='blue',font=('Arial',10,'bold'))
    label_descripcion.pack()
boton = tk.Button(ventana,text='AYUDA',command=ver_descripcion)
boton.pack()

def borrar_datos():
    entrada_peso.delete(0,tk.END)
    entrada_altura.delete(0,tk.END)

entrada_peso = Entry()
entrada_peso.insert(0,'PESO')
entrada_peso.pack()
entrada_altura = Entry()
entrada_altura.insert(0,'ALTURA EN cm')
entrada_altura.pack()

resultado = Label(ventana,font=("Arial",12,'bold'),foreground='black')
boton_resultado = tk.Button(ventana,text='VER RESULTADOS',command=calcular_imc)
boton_resultado.pack()
boton_reiniciar= tk.Button(ventana,text='REINICIAR',command=borrar_datos)
boton_reiniciar.pack()

ventana.mainloop()