from tkinter import *

root = Tk()

root.title('Hola mundo')
root.resizable(1, 1) # Booleano (vertical, horizontal)
root.iconbitmap("@hola.xbm")

frame = Frame(root, width=480, height=320)
#frame.pack(side="bottom", anchor="w") side = position, anchor = anclar en (e,w,n,s)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")



root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")


# Abajo del todo
root.mainloop()