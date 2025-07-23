import tkinter as tk
from tkcalendar import Calendar
from tkcalendar import  DateEntry
ventana = tk.Tk()
#WIDGETS DE TIEMPO
calendario = Calendar(ventana)
calendario.pack()
#FUNCION
def print_day(date):
    print(date)
calendario.bind("<<CalendarSelected>>", lambda e: print_day(calendario.get_date())) #Imprimir el día seleccionado

#CON DATE ENTRY
date_entry= DateEntry(ventana)
date_entry.pack()
date_entry.bind("<<DateEntrySelected>>",lambda e: print(date_entry.get())) #Imprimir el día seleccionado

ventana.mainloop()