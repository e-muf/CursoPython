from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

# Configuración de la raíz
root = Tk()

def test():
	# MessageBox.showinfo('Hola!', 'Hola mundo')
	# MessageBox.showwarning('Alerta', 'Sección sólo para administradores')
	# MessageBox.showerror('Error!', 'Ha ocurrido un error inesperado')
	#resultado = MessageBox.askquestion("Salir", '¿Está seguro que quiere salir sin guardar?')
	#if resultado == 'yes': # 'no'
	#	root.destroy()
	#resultado = MessageBox.askokcancel("Salir", '¿Sobreescribir en el fichero actual?')
	#resultado = MessageBox.askyesno("Salir", '¿Está seguro que quiere salir sin guardar?')
	#if resultado:
	#	root.destroy()
	#resultado = MessageBox.askretrycancel("Reintentar", 'No se puede conectar')
	#if resultado:
	#	root.destroy()
	#color = ColorCh.ooser.askcolor(title="Elige un color")
	#print(color)
	#ruta = FileDialog.askopenfilename(title='Abrir un fichero', initialdir='/home/emanuel/', filetypes=(('Ficheros de texto', '*.txt'), 
	#																									('Fichero de texto avanzado', '.txt2'),
	#																									('Todos los ficheros', '*.*')))
	#print(ruta)
	fichero = FileDialog.asksaveasfile(title='Guardar un fichero', mode='a', defaultextension='.txt') # Equivale a open('ruta', 'w')
	if fichero is not None:
		fichero.write('Hola voy a escribir otra cosa!')
		fichero.close()

Button(root, text='Clícame', command=test).pack()


# Finalmente bucle de la aplicación
root.mainloop()