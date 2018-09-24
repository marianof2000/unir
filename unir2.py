# Proyecto Unir para archivos de ventas y alícuotas de AFIP
import os.path

try:
    if os.path.isfile('ventas.txt') and os.path.isfile('alicuotas.txt'):
    	fichaventas = open('ventas.txt','r')
    	fichaalicuotas = open('alicuotas.txt','r')
    	fichasalida = open('salida2.txt','w')
except:
    print('No están todos los archivos')
else:
    ceros='000000000000000'+'0004'+'000000000000000'
    salida=''
    sal2=fichaalicuotas.readline()
    sal3=''
    #lee desde la posición 8 y toma 20 caracteres - lee el número de factura
    for sal1 in fichaventas:
    	salida=sal1[:-2]
    	while sal2[8:28] == sal1[16:36]:
    		if sal2[43:47]=='0005': # revisa el número de alícuota si es 0005 o 0004
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
    
    if os.path.isfile('salida2.txt'):
    	print('\nMisión cumplida!!')
    else:
    	print('\nNo se pudo crear el archivo de salida!!')
    fichaventas.close()
    fichaalicuotas.close()
    fichasalida.close()
