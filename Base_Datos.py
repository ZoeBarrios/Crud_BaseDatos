import sqlite3
import tkinter 
from tkinter import messagebox as mb
from tkinter import *
import Funciones_Variadas


#CONECTAR BASE DE DATOS
def crear_Base():  
        
    try:
        miConexion=sqlite3.connect("BASE_DE_DATOS")
        miCursor=miConexion.cursor()
        miCursor.execute("CREATE TABLE DATOSUSUARIOS (ID INTEGER PRIMARY KEY AUTOINCREMENT,NOMBRE_USUARIO VARCHAR(25) ,PASSWORD VARCHAR(50),APELLIDO VARCHAR(25),DIRECCION VARCHAR(25),COMENTARIOS VARCHAR(100))")
        miConexion.commit()
       
       
        mb.showinfo("Base de datos","La base de datos ha sido creada exitosamente")
    except:
        mb.showwarning("Cuidado","La base de datos ya existe")


#SALIR
def salir():
    quit()

#CREAR REGISTRO
def crear(nombre,apellido,password,direccion,tcomentarios):
    if nombre.get()=="" and apellido.get()=="" and password.get()=="" and direccion.get()=="" and tcomentarios.get(1.0,tkinter.END)=="\n":
        mb.showwarning("Fallo en la creación","No hay datos suficientes para agregar el registro")
    elif Funciones_Variadas.validacion(nombre,apellido,password,direccion)==False:
        mb.showinfo("Error","Modifique los datos para poder crear el registro")
    else:
        
        try:
            miConexion=sqlite3.connect("BASE_DE_DATOS")
            miCursor=miConexion.cursor()
            miCursor.execute(f"INSERT INTO DATOSUSUARIOS (NOMBRE_USUARIO ,PASSWORD ,APELLIDO ,DIRECCION ,COMENTARIOS) VALUES('{nombre.get()}','{password.get()}','{apellido.get()}','{direccion.get()}','{tcomentarios.get(1.0,tkinter.END)}')")
            miConexion.commit()
        
            mb.showinfo("Base de datos","Registro insertado exitosamente")
        except:
            mb.showerror("Cuidado","Ocurrio un error, cree la base de datos y verifique colocar una contraseña")
        
#ACTUALIZAR BADE DE DATOS
def leer(raiz,panel,lista_id,mostrar_lista): 
    
    try:
        miConexion=sqlite3.connect("BASE_DE_DATOS")
        miCursor=miConexion.cursor()
        miCursor.execute("SELECT ID FROM DATOSUSUARIOS")
        lista_id=miCursor.fetchall()
        Funciones_Variadas.panel_mostrar(raiz,panel,lista_id,mostrar_lista)
        
    except:
        mb.showerror("Error","No hay registros en la base de datos")   
        panel.set("Inserte nuevos registros.")

#MODIFICAR REGISTRO
def actualizar(nombre,apellido,password,direccion,tComentarios,ident,raiz,panel,lista_id,mostrar_lista):
    try:
        miConexion=sqlite3.connect("BASE_DE_DATOS")
        miCursor=miConexion.cursor()
        miCursor.execute(f"UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO='{nombre.get()}',PASSWORD='{password.get()}',APELLIDO='{apellido.get()}',DIRECCION='{direccion.get()}',COMENTARIOS='{tComentarios.get(1.0,tkinter.END)}' WHERE ID={ident}")
        miConexion.commit()
        mb.showinfo("Excelente","Se ha actualizado el registro correctamente")
        leer(raiz,panel,lista_id,mostrar_lista)
    except:
        mb.showerror("Error","Ha ocurrido un error")
    

#MENSAJE DE CONFIRMACION
def borrar_registro(panel):
    try:
        id=Funciones_Variadas.obtener_id(panel)
        valor=mb.askyesno(message=f"¿Desea borrar el registro con id={id}?")
        if valor==True:
            miConexion=sqlite3.connect("BASE_DE_DATOS")
            miCursor=miConexion.cursor()
            miCursor.execute(f"DELETE FROM DATOSUSUARIOS WHERE ID={id}")
            miConexion.commit()
    except:
        mb.showerror("Error","No ha seleccionado ningun registro")
        
        

    


    




