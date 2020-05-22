def calularcondiferentessignosRMSA():
    #datos de entrada 
    unidad1=int(input("ingrese su primer numero:"))
    unidad2=int(input("ingrese su segundo numero:"))
    tiposdesignos=int(input("ingrese su numero de signo que desea:"))
    #proceso 
    if tiposdesignos==1:
	        respuesta = unidad1+unidad2
    elif tiposdesignos==2:
	        respuesta = unidad1-unidad2
    elif tiposdesignos==3:
	        respuesta = unidad1/unidad2
    elif tiposdesignos==4:
 	        respuesta = unidad1*unidad2
    elif tiposdesignos==5:
	        respuesta = unidad1^unidad2
    else:
            respuesta=0
	# datos de salida   
    print(f"el problema sale:{ respuesta }")


calularcondiferentessignosRMSA()