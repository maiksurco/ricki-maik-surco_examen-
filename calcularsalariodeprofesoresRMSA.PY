def calcularsalariodeprofesoresRMSA():
    #datos de entrada
    salario=int(print("ingrese el salario"))
    puntos=int(print("infrese los puntos obtenidos"))
    #proceso
    if puntos>=20 and puntos<=100:
        premio=salario/10
    elif puntos>=101 and puntos<=200:
            premio=salario/2
    elif puntos>=201:
                premio=salario
    else:
                    print("no hay ningun dinero")
    #datos de salida
    print(f"si el salario es: {salario}")
    print(f"y tienes {puntos}")
    print(f"recibiras el premio de: $ {premio}")

calcularsalariodeprofesoresRMSA()