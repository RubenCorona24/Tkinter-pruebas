#Hacer un programa con el fin de resolver una operación básica (el doble de un número)
import tkinter as tk
from random import random, randint

ventana = tk.Tk()
ventana.title("Elección de Número")
ventana.geometry("900x600")
tk.Label(ventana,text='EXTRAE TU NÚMERO EN "EXTRAER"',foreground='green',font=('Arial',12,'bold')).pack(pady=10)
num = randint(1,101)
lbl_number = tk.Label(ventana) #Label del mensaje
lbl_number.pack(pady=10)
def escoger(): #Función de mostrar en label el número
    lbl_number.config(text=f'Tu número es: {num}',foreground='black',font=('Arial',10,'bold'))
tk.Button(ventana,text='EXTRAER',command=escoger,foreground='red',font=('Arial',12,'bold')).pack()

tk.Label(ventana,text='¿Cuánto es el doble del número que te tocó?',foreground='black',font=('Arial',12,'bold')).pack(pady=10)
entrada_num = tk.Entry(ventana) #Entrada para introducir el resultado
entrada_num.pack()
lbl_revisar = tk.Label(ventana)
lbl_revisar.pack()
def revisar(): #Función de revisar si la operación está bien
    if entrada_num.get() == str(num*2):
        lbl_revisar.config(text='FELICIDADES, TU RESPUESTA ES LA CORRECTA',foreground='green',font=('Arial',10,'bold'))
    elif entrada_num.get() == '':
        lbl_revisar.config(text='INCORRECTO, NO HAS INTRODUCIDO UN NÚMERO',foreground='red',font=('Arial',10,'bold'))
    else:
        lbl_revisar.config(text='INCORRECTO, VUELVE A INTENTARLO', foreground='red', font=('Arial', 10, 'bold'))
tk.Button(ventana,text='REVISAR RESPUESTA',command=revisar,foreground='purple',font=('Arial',12,'bold')).pack(pady=15)
def cerrar(): #Función de cerrar el programa
    ventana.destroy()
tk.Button(ventana,text='CERRAR PROGRAMA',foreground='red',font=('Arial',16,'bold'),command=cerrar).pack(pady=10)



ventana.mainloop()