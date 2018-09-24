# Proyecto Unir para archivos de ventas y alícuotas de AFIP

import os.path

try:
    if os.path.isfile('ventas.txt') and os.path.isfile('alicuotas.txt'):
    	fichaventas = open('ventas.txt','r')
    	fichaalicuotas = open('alicuotas.txt','r')
    	fichasalida = open('salida.txt','w')
except:
    print('No están todos los archivos')
else:
    ceros='000000000000000'+'0004'+'000000000000000'
    salida=''
    sal1='  '
    sal2=fichaalicuotas.readline()
    sal3=''
    numfact=sal2[8:28]   #lee desde la posición 8 y toma 20 caracteres - lee el número de factura
    while True:
    	sal1=fichaventas.readline()
    	salida=sal1[:-2]
    	numerocad=sal1[16:36]
    	while numfact==numerocad:
    		numalic=sal2[43:47]
    		if numalic=='0005':
    			if len(sal3)<30:
    				sal3=ceros+sal2[28:62]
    			else:
    			    sal3+=sal2[28:62]
    		else:
    			sal3=sal2[28:62]
    		sal2=fichaalicuotas.readline()
    		numfact=sal2[8:28]
    		if sal2=='':
    			break
    	if sal2 !='':
    		if len(sal3)<40:
    		    sal3+='0000000000000000005000000000000000' # porque solo tienen alicuota 0004 
    		salida+=sal3+'\n'
    		fichasalida.write(salida)
    	sal3=''
    	if sal1 == '':
    		print('Break!!')
    		break
    if os.path.isfile('salida.txt'):
    	print('\nMisión cumplida!!')
    fichaventas.close()
    fichaalicuotas.close()
    fichasalida.close()
