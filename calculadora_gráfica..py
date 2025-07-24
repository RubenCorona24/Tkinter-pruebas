import tkinter as tk
from tkinter import Entry, Button

ventana = tk.Tk()
ventana.title("Calculadora")

valor_a = 0
valor_b = 0
operacion = ''
resultado = 0

# Funciones matemáticas
def sumar():
    return valor_a + valor_b

def restar():
    return valor_a - valor_b

def dividir():
    return valor_a / valor_b if valor_b != 0 else "Error"

def multiplicar():
    return valor_a * valor_b

def resultado_igual():
    global valor_a, valor_b, resultado, operacion
    try:
        valor_b = float(pantalla.get())
    except ValueError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")
        return

    pantalla.delete(0, tk.END)

    if operacion == 'sumar':
        resultado = sumar()
    elif operacion == 'restar':
        resultado = restar()
    elif operacion == 'multiplicar':
        resultado = multiplicar()
    elif operacion == 'dividir':
        resultado = dividir()
    else:
        resultado = "Error"

    pantalla.insert(tk.END, resultado)

def borrar():
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, 0)

def agregar_pantalla(valor):
    actual = pantalla.get()
    if actual == '0':
        pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, valor)

def operar(simbolo):
    global valor_a, operacion
    try:
        valor_a = float(pantalla.get())
    except ValueError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")
        return

    pantalla.delete(0, tk.END)

    if simbolo == '+':
        operacion = 'sumar'
    elif simbolo == '-':
        operacion = 'restar'
    elif simbolo == '*':
        operacion = 'multiplicar'
    elif simbolo == '/':
        operacion = 'dividir'

# Pantalla
pantalla = Entry(ventana, width=25, bd=5, justify='right')
pantalla.grid(row=0, column=0, columnspan=4)
pantalla.insert(tk.END, '0')

# Botones numéricos y de operaciones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    if texto in '0123456789.':
        comando = lambda x=texto: agregar_pantalla(x)
    elif texto == '=':
        comando = resultado_igual
    else:
        comando = lambda x=texto: operar(x)
    boton = Button(ventana, text=texto, width=4, command=comando)
    boton.grid(row=fila, column=columna)

# Botón de borrar
boton_borrar = Button(ventana, text='Borrar', width=20, command=borrar)
boton_borrar.grid(row=5, column=0, columnspan=4)

ventana.mainloop()