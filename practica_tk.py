#Vamos a hacer una prueba gráfica con tkinter
import tkinter as tk
from datetime import datetime
import random

window = tk.Tk()
window.title("Organization States")
window.geometry('900x600')
fecha = datetime.today()
tk.Label(window,text='WELCOME TO THE ORGANIZATION STATES',foreground='red',font=("Arial",16,'bold')).pack(pady=10)
tk.Label(window,text=f'YEAR: {fecha.year}, MONTH: {fecha.month} DAY: {fecha.day}',foreground='black',font=("Arial",12,'bold')).pack()
tk.Label(window,text='Enter your nacionality',foreground='black',font=("Arial",12,'bold')).pack(pady=10)
entrada_nacionalidad = tk.Entry()
entrada_nacionalidad.pack()
lbl_language = tk.Label(window)
lbl_language.pack()
def obtener_nacionalidad():
    if entrada_nacionalidad.get() in ['México','Colombia','Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia',
                                      'Ecuador',' Guyana', 'Paraguay', 'Perú', 'Uruguay', 'Venezuela', 'Guyana Francesa', 'Surinam',
                                      'Belice', 'Costa Rica', 'El Salvador', 'Guatemala', 'Honduras', 'Nicaragua', 'Panamá'
                                      ]:
        lbl_language.config(text='Language: Español',pady=10)
    elif entrada_nacionalidad.get() in ['Canada','United States','EUA','United Kingdom','Malta','New Zealand','Australia']:
        lbl_language.config(text='Language: English',pady=10)
    elif entrada_nacionalidad.get() in ['China','Taiwán','Singapur','Hong Kong','Macao']:
        lbl_language.config(text='Language: Chinese',pady=10)
    elif entrada_nacionalidad.get() == 'Japón':
        lbl_language.config(text='Language: Japanese',pady=10)
    else:
        lbl_language.config(text='Language not detected',pady=10)
lbl_number = tk.Label(window)
lbl_number.pack()
number = random.randint(1, 101)

def asignar_number():
    lbl_number.config(text=f'Assigned Numbre: {number}',pady=10)
    boton_número.config(state='disabled')
lbl_save = tk.Label(window)
lbl_save.pack()
def guardar_cambios():
    with open('asignación.txt','w') as file:
        file.write(f"Language---- {entrada_nacionalidad.get()}\nNumber----- {number}\nDate---- YEAR: {fecha.year}, MONTH: {fecha.month} DAY: {fecha.day}")
    lbl_save.config(text='YOUR DATA HAS BEEN SAVED AS: asignación.txt',foreground='green')
    boton_save.config(state='disabled')

tk.Button(window,text='GET LANGUAGE',command=obtener_nacionalidad,font=('Arial',12,'bold'),foreground='blue').pack(pady=10)
boton_número = tk.Button(window,text='GET NUMBER',command=asignar_number,font=('Arial',12,'bold'),foreground='blue')
boton_número.pack(pady=10)
boton_save = tk.Button(window,text='SAVE DATA',command=guardar_cambios,font=('Arial',12,'bold'),foreground='blue',pady=15)
boton_save.pack()

