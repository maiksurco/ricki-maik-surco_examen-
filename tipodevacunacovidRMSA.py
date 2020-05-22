def tipodevacunacovidRMSA():
    #datos de entrada
    edad=int(print("ingrese su edad"))
    sexo=int(print("ingrese su sexo"))
    #proceso
    if edad>=70:
        print("se le aplica la vacuna C")
    elif edad>=16 and edad<=69 and sexo==1:
        print("se le aplica la vacuna B")
    elif edad>=16 and edad<=69 and sexo==2:
        print("se le palica la vacuna A")
    elif edad<16:
        print("se le aplica la vacuna A")
    else: 
        print("no se le aplica nada")
    #datos de salida
    print(f"si usted tiene: {edad}")
    print(f"años y su sexo es: {sexo}")
    
tipodevacunacovidRMSA()               