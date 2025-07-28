import tkinter as tk
from tkinter import filedialog, messagebox,Label  # Importamos la libreria
from tkinter import font
def nuevo_archivo():
    area_de_texto.delete(1.0, tk.END)
def guardar():
    global ruta
    if ruta:
        try:
            with open(ruta,'w',encoding='utf-8') as file:
                file.write(area_de_texto.get(1.0,tk.END))
        except:
            print("No se pudo guardar")
def guardar_como():
    name = filedialog.asksaveasfilename(defaultextension='.txt',filetypes=[('Archivos de texto','*.txt'),
                                                                                    ('Archivos de Python','*.py'),
                                                                                    ('Todos','*.*')])
    if name:
        with open(name,'w',encoding='utf-8') as file:
            file.write(area_de_texto.get(1.0,tk.END))
            label = Label(ventana,text="ARCHIVO GUARDADO")
            label.pack(side='top')



def abrir():
    global ruta
    try:
        ruta = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('Archivos de texto','*.txt'),
                                                                                    ('Archivos de Python','*.py'),
                                                                                    ('Todos','*.*')])
        with open(ruta,'r',encoding='utf-8') as file:
            archive = file.read()
            area_de_texto.insert(1.0,archive)
    except:
        print("Algo salió mal")

def cerrar_ventana():
    ventana.destroy() #Funciones de menu archivo

def deshacer():
    area_de_texto.delete(1.0,tk.END)

def copiar():
    area_de_texto.event_generate(("<<Copy>>"))
def pegar():
    area_de_texto.event_generate(("<<Paste>>"))
def cortar():
    area_de_texto.event_generate(("<<Cut>>"))     #Funcioes de menú edición

def negrita():
    try:
        seleccion = area_de_texto.tag_ranges(tk.SEL)
        if seleccion:
            area_de_texto.tag_add("negrita", tk.SEL_FIRST, tk.SEL_LAST)
    except:
        messagebox.showwarning("Advertencia", "Selecciona texto para aplicar negrita")


ruta = ''
ventana = tk.Tk()
ventana.title('Bloc de notas')
ventana.geometry('900x600')
fuente =  font.Font(family='Arial',size=12)
fuente_negrita = font.Font(family="Arial", size=12, weight="bold")
menu = tk.Menu(ventana) #Creamos el menú en la ventana
ventana.config(menu=menu)

archivo = tk.Menu(menu)
menu.add_cascade(label='Archivo',menu=archivo)
edicion = tk.Menu(menu)
menu.add_cascade(label='Edición',menu=edicion)
ver = tk.Menu(menu,tearoff=0)
menu.add_cascade(label='Ver',menu=ver)  #Creamos todos los menus dentro del menú

area_de_texto = tk.Text(ventana, font=fuente)
area_de_texto.pack(expand=True, fill="both")
area_de_texto.tag_configure("negrita", font=fuente_negrita) #Creamos el área de texto

archivo.add_command(label='Nuevo archivo',command=nuevo_archivo)
archivo.add_command(label='Guardar',command=guardar)
archivo.add_command(label='Guardar como',command=guardar_como)
archivo.add_command(label='Abrir',command=abrir)
archivo.add_command(label='Cerrar Ventana',command=cerrar_ventana) #Creamos los comandos del menú "Archivo"

edicion.add_command(label='Deshacer',command=deshacer)
edicion.add_command(label='Copiar',command=copiar)
edicion.add_command(label='Pegar',command=pegar)
edicion.add_command(label='Cortar',command=cortar) #Creamos los comandos del menú "Edición

ver.add_command(label='Negrita',command=negrita)



ventana.mainloop()