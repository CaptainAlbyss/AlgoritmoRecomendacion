from tkinter import *
import numpy as np
import sys
#------Distancia de hamming codigo por: Andrew Dalke usuario de activestate------
def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return(sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2)))
#------------------------------------------------------------------------------
compatible=""
guardar=0
vector=[]
vector2=[]
archivo2=open('canciones.txt','r')
for lineas2 in archivo2:
    linea2 = lineas2.strip().split('\n')
    vector2.append(linea2[0])
archivo2.close()
        
#--------------Funciones botones---------------------------------------------

def actualizar():
    lstGustos.delete(0,END)
    lstCanciones.delete(0,END)
    for i in range (0,len(vector2)):
        lstCanciones.insert(END,vector2[i])

        
def recomendar():
    #-----------------Elementos ventana de recomendaciones----------
    minimo=sys.maxsize
    ventana2=Tk()
    ventana2.geometry("325x345+50+50")
    ventana2.title("Canciones Recomendadas")
    lstRecomendadas=Listbox(ventana2,width=50,height=20)
    lstRecomendadas.place(x=10,y=10)
    #--------------------------------------------------------------
    archivo=open('votaciones.txt','r')
    for lineas in archivo:
        linea= lineas.strip().split(',')
        valor=""
        for i in range(0,len(linea)):
            valor+= linea[i]
        vector.append(valor)
    r=len(vector)
    matriz=(r,r)
    a=np.zeros(matriz)
    for i in range(0,r):
        for j in range(0,r):
            if(i!=j):
                a[i][j]=hamming_distance(vector[i],vector[j])
    print(a)
    for i in range(0,r):
        if(a[r-1][i]<minimo and r-1!=i):
            minimo=a[r-1][i]
            print(minimo)
            compatible=vector[i]
    usuario=vector[r-1]
    print("usuario")
    print(usuario)
    print("compatible")
    print(compatible)
    for i in range(0,len(usuario)):
        if(usuario[i]!=compatible[i]):
            if(usuario[i]=="0" and compatible[i]=="1"):
                lstRecomendadas.insert(END,vector2[i])
    archivo.close()
    


def gustar():
    lstGustos.delete(0,END)
    gustadas=[]
    tupla=lstCanciones.curselection()
    for i in range (0, len(tupla)):
        gustadas.append(tupla[i])
    for i in range(0,len(gustadas)):
        temp=lstCanciones.get(gustadas[i])
        lstGustos.insert(END,temp)
    archivo=open('votaciones.txt','at')
    var=""
    agregar=[]
    lon = lstCanciones.size()
    for i in range(0,int(lon)):
        agregar.append(0)
    for i in range (0,len(gustadas)):
        agregar[int(gustadas[i])]=1
    for i in range(0,len(agregar)):
        var+= str(agregar[i]) + ","
    lon2=len(var)
    var=var[:lon2-1]
    archivo.write(var+'\n')
    archivo.close()
    
    
    


#------------------------
#Ventana
ventana=Tk()
ventana.geometry("695x500+0+0")
ventana.title("Canciones Populares")
#Elementos

lblEmisora=Label(ventana,font=("Arial",40),text="Emisora Estacion V").place(x=110,y=10)
lblCanciones=Label(ventana,text="Canciones").place(x=125,y=100)
lblGustos=Label(ventana,text="Gustaron").place(x=510,y=100)
lstCanciones=Listbox(ventana,selectmode=MULTIPLE,width=50,height=20)
lstCanciones.place(x=10,y=120)
lstGustos=Listbox(ventana,width=50,height=20)
lstGustos.place(x=380,y=120)
btnActualizar=Button(ventana,text="Actualizar",height=1,width=10,command=actualizar).place(x=100,y=460)
btnGustar=Button(ventana,text=">>",height=1,width=5,command=gustar).place(x=325,y=250)
btnRecomendar=Button(ventana,text="recomendar",height=1,width=10,command=recomendar).place(x=10,y=460)
barraMenu=Menu(ventana)
#Menus
mnuArchivo=Menu(barraMenu)
mnuEdicion=Menu(barraMenu)
mnuAyuda=Menu(barraMenu)
#Archivo
mnuArchivo.add_command(label="Abrir")
mnuArchivo.add_command(label="Nuevo")
mnuArchivo.add_command(label="Guardar")
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Salir")
#Edicion
mnuEdicion.add_command(label="Deshacer")
mnuEdicion.add_command(label="Rehacer")
#Ayuda
mnuAyuda.add_command(label="Sobre Nosotros")
mnuAyuda.add_separator()
mnuAyuda.add_command(label="Creditos")
#incluir menus
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
barraMenu.add_cascade(label="Edicion",menu=mnuEdicion)
barraMenu.add_cascade(label="Ayuda",menu=mnuAyuda)


ventana.config(menu=barraMenu)



ventana.mainloop()
