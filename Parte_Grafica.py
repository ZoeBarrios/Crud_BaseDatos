from tkinter import *
import Base_Datos
import Funciones_Variadas
import sqlite3
from tkinter import messagebox as mb

#---------RAIZ--------
raiz=Tk()
raiz.title("Base de datos")
raiz.geometry("650x400")
raiz.resizable(0,0)
raiz.iconbitmap("cat.ico")
raiz.config(bg="pink")


#VARIABLES
nombre=StringVar()
apellido=StringVar()
password=StringVar()
direccion=StringVar()
panel=StringVar()
ident=0
lista_id=["Actualice la base de datos."]


def mostrar_lista(cod):
    Funciones_Variadas.borrar_campos(nombre,apellido,password,direccion,tComentarios)
    miConexion=sqlite3.connect("BASE_DE_DATOS")
    miCursor=miConexion.cursor()
    id=Funciones_Variadas.obtener_id(panel)
    global ident
    ident=id
    miCursor.execute(f"SELECT * FROM DATOSUSUARIOS WHERE ID={ident}")
    lista_datos=list(miCursor.fetchall())
    lista_final=list()
    con=0
    for i in lista_datos:
        for e in i:
            if e=="" or e=="\n":
                lista_final.append(" ")
            else:
                lista_final.append(e)
            con+=1
            
    nombre.set(lista_final[1])
    apellido.set(lista_final[3])
    password.set(lista_final[2])
    direccion.set(lista_final[4])
    tComentarios.insert(1.0,lista_final[5])

    

#CUADROS DE TEXTO
cNombre=Entry(raiz)
cNombre.config(textvariable=nombre)
cNombre.grid(row="2",column="1",padx=10,pady=10)

cApellido=Entry(raiz)
cApellido.config(textvariable=apellido)
cApellido.grid(row="3",column="1",padx=10,pady=10)

cPassword=Entry(raiz,show="*")
cPassword.config(textvariable=password)
cPassword.grid(row="4",column="1",padx=10,pady=10)

cDireccion=Entry(raiz)
cDireccion.config(textvariable=direccion)
cDireccion.grid(row="5",column="1",padx=10,pady=10)

#SCROLLBAR

tComentarios=Text(raiz,width=18,height=5,font="Arial")
tComentarios.grid(row="6",column="1")
scroll=Scrollbar(raiz,command=tComentarios.yview)
scroll.grid(row="6",column="1",sticky="nse")
tComentarios.config(yscrollcommand=scroll.set)

    
#---------MENU--------
menu=Menu(raiz)
raiz.config(menu=menu)

#MENU BBDD
bbdd=Menu(tearoff=0)
menu.add_cascade(label="BBDD",menu=bbdd)
bbdd.add_command(label="Crear Base",command=Base_Datos.crear_Base)
bbdd.add_command(label="Salir",command=Base_Datos.salir)


#MENU CRUD
crud=Menu(tearoff=0)
menu.add_cascade(label="CRUD",menu=crud)
crud.add_command(label="Crear",command=lambda: Base_Datos.crear(nombre,apellido,password,direccion,tComentarios))
crud.add_command(label="Modificar",command=lambda: Base_Datos.actualizar(nombre,apellido,password,direccion,tComentarios,ident,raiz,panel,lista_id,mostrar_lista))
crud.add_command(label="Borrar",command=lambda: Base_Datos.borrar_registro(panel,lista_id))

#MENU AYUDA
ayuda=Menu(tearoff=0)
menu.add_cascade(label="Ayuda",menu=ayuda)
ayuda.add_command(label="Licencia",command=Funciones_Variadas.licencia)
ayuda.add_command(label="Acerca de...",command=Funciones_Variadas.manual)

#MENU BORRAR
borrar=Menu(tearoff=0)
menu.add_cascade(label="Borrar",menu=borrar)
borrar.add_command(label="Borrar campos",command=lambda: Funciones_Variadas.borrar_campos(nombre,apellido,password,direccion,tComentarios))


#--------------LABELS----------------
Nombre=Label(raiz)
Apellido=Label(raiz)
Password=Label(raiz)
Direccion=Label(raiz)
Comentarios=Label(raiz)
Desplegable=Label(raiz)



Nombre.config(text="Nombre:",justify=CENTER,background="pink",font=13)
Nombre.grid(row="2",column="0",padx=10,pady=10)

Apellido.config(text="Apellido:",justify=CENTER,background="pink",font=13)
Apellido.grid(row="3",column="0",padx=10,pady=10)

Password.config(text="Password:",justify=CENTER,background="pink",font=13)
Password.grid(row="4",column="0",padx=10,pady=10)

Direccion.config(text="Dirección:",justify=CENTER,background="pink",font=13)
Direccion.grid(row="5",column="0",padx=10,pady=10)

Comentarios.config(text="Comentarios:",justify=CENTER,background="pink",font=13)
Comentarios.grid(row="6",column="0",padx=10,pady=10)

Desplegable.config(text="Seleccione un registro:",justify=CENTER,background="pink",font=13)
Desplegable.place(x=400,y=50)

#BOTONES

bCrear=Button(raiz,padx=20,pady=5,width=10)
bCrear.config(text="Crear registro",command=lambda: Base_Datos.crear(nombre,apellido,password,direccion,tComentarios))
bCrear.place(x=20,y=300)


bActu=Button(raiz,padx=20,pady=5,width=10)
bActu.config(text="Modificar registro",command=lambda: Base_Datos.actualizar(nombre,apellido,password,direccion,tComentarios,ident,raiz,panel,lista_id,mostrar_lista))
bActu.place(x=160,y=300)

bBorrar=Button(raiz,padx=20,pady=5,width=10)
bBorrar.config(text="Borrar registro",command=lambda: Base_Datos.borrar_registro(panel))
bBorrar.place(x=300,y=300)
Funciones_Variadas.panel_mostrar(raiz,panel,lista_id,mostrar_lista)

bLeer=Button(raiz,padx=20,pady=5,width=10)
bLeer.config(text="Actualizar base de datos",command=lambda: Base_Datos.leer(raiz,panel,lista_id,mostrar_lista),width=20)
bLeer.place(x=380,y=150)




raiz.mainloop()