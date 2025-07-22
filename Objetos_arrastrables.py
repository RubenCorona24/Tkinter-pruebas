# Segundo rectángulo arrastrable
otro_rect = canva.create_rectangle(100, 100, 200, 200, fill='blue', tags='rectángulo')

# Variables globales
objeto_seleccionado = None
x_anterior = 0
y_anterior = 0

# Funciones de arrastre
def iniciar_arrastre(event):
    global objeto_seleccionado, x_anterior, y_anterior
    objeto_seleccionado = canva.find_closest(event.x, event.y)[0]
    x_anterior = event.x
    y_anterior = event.y

def mover_objeto(event):
    global objeto_seleccionado, x_anterior, y_anterior
    if objeto_seleccionado:
        dx = event.x - x_anterior
        dy = event.y - y_anterior
        canva.move(objeto_seleccionado, dx, dy)
        x_anterior = event.x
        y_anterior = event.y

# Asociar eventos al rectángulo
canva.tag_bind('rectángulo', '<ButtonPress-1>', iniciar_arrastre)
canva.tag_bind('rectángulo', '<B1-Motion>', mover_objeto)

ventana.mainloop()
