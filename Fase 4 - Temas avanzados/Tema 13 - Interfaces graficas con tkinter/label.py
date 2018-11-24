from tkinter import *

# Configuración de la raíz
root = Tk()
'''
# Variables dinámicas
texto = StringVar()
texto.set('Un nuevo texto')

# Configuración de un marco
#frame = Frame(root, width=480, height=320)
#frame.pack()

#label = Label(root, text="¡Hola Mundo!")
#label.pack()

Label(root, text="¡Hola Mundo!").pack(anchor='nw')
label = Label(root, text="¡Otra etiqueta!")
label.pack(anchor='center')
Label(root, text="¡Última etiqueta!").pack(anchor='se')

label.config(bg='green', fg='blue', font=('DejaVuSansMono', 24))
label.config(textvariable=texto)
'''

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side='left')

# Abajo del todo
root.mainloop()