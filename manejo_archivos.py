import tkinter as tk
from tkinter.ttk import Label
from tkinter import filedialog, Button



ventana = tk.Tk()
#file_object= tk.filedialog.askopenfile(mode='r') #Para seleccionar archivos
#if file_object:
#    print(file_object.read())
#    file_object.close()  #----FUNCIÓN BÁSICA PARA ABRIR ARCHIVO----

#----FUNCIÓN PARA ABRIR ARCHIVO----
def abrir_archivo():
    filename = filedialog.asksaveasfilename(filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')])
    if filename:
        with open(filename, 'r') as file_obj:
            contenido = file_obj.read()
            text_widget.delete(1.0, tk.END)  # Borrar el contenido de widget
            text_widget.insert(tk.INSERT, contenido)  # Insertar el contenido en el widget

#----FUNCIÓN PARA GUARDAR ARCHIVO----
def guardar_archivo():
    file_path = filedialog.asksaveasfilename(filetypes=[('Archivos de texto','*.txt'), ('Todos los archivos','*.*')])
    if file_path:
        with open(file_path,'w') as file_object:
            contenido = text_widget.get(1.0,tk.END)
            file_object.write(contenido)

text_widget = tk.Text(ventana, wrap='word')  # Crear el campo de texto
text_widget.pack(expand=True, fill='both')
abrir_button = Button(ventana, text='ABRIR ARCHIVO', command=abrir_archivo)  # Crear el botón para ejecutar función
abrir_button.pack(side='left')
guardar_button = Button(ventana, text='ABRIR ARCHIVO', command=guardar_archivo)  # Crear el botón para ejecutar función
guardar_button.pack(side='right')
ventana.mainloop()