from tkinter import *
from tkinter import messagebox as mb
import subprocess
import re

def panel_mostrar(raiz,panel,lista_id,mostrar_lista):
    miPanel=OptionMenu(raiz, panel, *lista_id,command=mostrar_lista)
    miPanel.config(width=20,background="white")
    miPanel.place(x=380,y=90)


def borrar_campos(nombre,apellido,password,direccion,tComentarios):
    nombre.set("")
    apellido.set("")
    password.set("")
    direccion.set("")
    tComentarios.delete(1.0,END)
    
def obtener_id(panel):
    informacion=panel.get()
    informacion=re.search("\d+",informacion)
    inicio=informacion.start()
    final=informacion.end()
    return panel.get()[inicio:final]

def licencia():
    mb.showinfo("Licencia","Propiedad de Zoe Barrios")

def manual():
    subprocess.run(['notepad.exe','HOW_TO_USE.txt'])

def validacion(nombre,apellido,password,direccion):
    con=0
    try:
        validar_string(nombre.get())
        con+=1
        
    except:
        nombre.set("No se admiten números")
    
    try:
        validar_string(apellido.get())
        con+=1
    
    except:
        apellido.set("No se admiten números")

    try:
        validar_string_int(password.get())
        con+=1
    except:
        mb.showinfo("Falta información","La contraseña debe tener almenos un número y letra")
    
    try:
        validar_string_int(direccion.get())
        con+=1
    except:
        direccion.set("Falta la calle o número")


    if con==4:
        return True
    else:
        return False
        


def validar_string(string):
    caracteres=re.findall("[0-9]",string)
    if len(caracteres)>0:
        raise ValueError

def validar_string_int(parametro):
    caracteres=re.findall("[a-zA-Z]",parametro)
    numeros=re.findall("[0-9]",parametro)
    if len(caracteres)==0 or len(numeros)==0:
        raise ValueError