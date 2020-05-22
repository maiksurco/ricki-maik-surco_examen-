def notafinaldelestudianteRMSA():       
	# datos de entrada
	unidad1=int(print("ingrese nota de la unidad 1"))
	unidad2=int(print("ingrese nota de la unidad 2"))
	unidad3=int(print("ingrese nota de la unidad 3"))
	unidad4=int(print("ingrese nota de la unidad 4"))
	# proceso
	notafinal = ((unidad1*15)/100)+((unidad2*20)/100)+((unidad3*25)/100)+((unidad4*40)/100)
	# datos de salida
	print(f"tu nota final es: {notafinal}")

notafinaldelestudianteRMSA() 