# Unir archivos de AFIP - unir-afip.pyw
from tkinter import *
import os.path

raiz=Tk()
raiz.title("Unir archivos de ventas y alicuotas - AFIP")
raiz.resizable(0,0)
raiz.geometry("420x250")

frame1=Frame(raiz, width="470",height="315")
frame1.pack()

etiqueta1=Label(frame1, text="Ventas.txt", font=("Arial",14))
etiqueta1.place(x=50,y=30)
etiqueta4=Label(frame1, text="OK", font=("Arial",14))
etiqueta4.place(x=200,y=30)

etiqueta2=Label(frame1, text="Alicuotas.txt", font=("Arial",14))
etiqueta2.place(x=50,y=60)
etiqueta5=Label(frame1, text="OK", font=("Arial",14))
etiqueta5.place(x=200,y=60)

etiqueta3=Label(frame1, text="Salida.txt", font=("Arial",14))
etiqueta3.place(x=50,y=90)
etiqueta6=Label(frame1, text="OK", font=("Arial",14))
etiqueta6.place(x=200,y=90)

etiqueta7=Label(frame1, text="", font=("Arial",14), fg="red")
etiqueta7.place(x=50,y=150)

def unir():
	# Proyecto Unir para archivos de ventas y alicuotas de AFIP
	try:
	    #if os.path.isfile('ventas.txt') and os.path.isfile('alicuotas.txt'):
	    fichaventas = open('VENTAS.txt','r')
	    fichaalicuotas = open('ALICUOTAS.txt','r')
	    fichasalida = open('salida.txt','w')
	except:
	    etiqueta7.config(text="No estan todos los archivos")
	else:
	    ceros='000000000000000'+'0004'+'000000000000000'
	    salida=''
	    sal2=fichaalicuotas.readline()
	    sal3=''
	    #lee desde la posicion 8 y toma 20 caracteres - lee el numero de factura
	    for sal1 in fichaventas:
	    	salida=sal1[:-2]
	    	while sal2[8:28] == sal1[16:36]:
	    		if sal2[43:47]=='0005': # revisa el numero de alicuota si es 0005 o 0004
	    			if len(sal3)<30:
	    				sal3=ceros+sal2[28:62]
	    			else:
	    			    sal3+=sal2[28:62]
	    		else:
	    			sal3=sal2[28:62]
	    		sal2=fichaalicuotas.readline()
	    		if sal2=='':
	    			break
	    	if sal2 !='':
	    		if len(sal3)<40:
	    		    sal3+='0000000000000000005000000000000000' # porque solo tienen alicuota 0004 
	    		salida+=sal3+'\n'
	    		fichasalida.write(salida)
	    	sal3=''
	    
	    if os.path.isfile('salida.txt'):
	    	etiqueta7.config(text="Mision cumplida!!")
	    else:
	    	etiqueta7.config(text="No se pudo crear el archivo de salida!!")
	    fichaventas.close()
	    fichaalicuotas.close()
	    fichasalida.close()

boton1=Button(frame1, text="Unir archivos", font=("Arial",14), command=unir)
boton1.place(x=250,y=190)

raiz.mainloop() 
