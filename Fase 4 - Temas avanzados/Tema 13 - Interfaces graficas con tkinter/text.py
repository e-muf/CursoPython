from tkinter import *

# Configuracion de la raiz
root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=('Consolas', 12), padx=5, pady=5, selectbackground='red')

# Finalmente bucle de la aplicación
root.mainloop()