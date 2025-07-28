import tkinter as tk
ventana = tk.Tk()
ventana.title("CONTADOR")
ventana.geometry('900x600')

title = tk.Label(ventana,text="CONTADOR DE NÚMEROS",font=("Arial",12,'bold'),foreground='red')
title.pack(side='top')  #Título dentro ventana
contador = 0
label_contador = tk.Label(ventana,text=f'CLICS: {contador}',font=("Arial",10,'bold'),foreground='green')
label_contador.pack()
def contar():
    global contador
    contador +=1
    label_contador.config(text=f'CLICS:{contador}',font=("Arial",10,'bold'),foreground='green')
def descontar():
    global contador
    contador -=1
    label_contador.config(text=f'CLICS:{contador}',font=("Arial",10,'bold'),foreground='red')
boton_contar = tk.Button(ventana,text='CONTAR',font=('Arial',12,'bold'),command=contar)
boton_contar.pack()
boton_descontar = tk.Button(ventana,text='DESCONTAR',font=('Arial',12,'bold'),command=descontar)
boton_descontar.pack()



ventana.mainloop()