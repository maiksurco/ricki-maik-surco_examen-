def salariode6añosdelprofesorRMSA():
    contadordeaños=1
    salario_inicial=1400
    #datos de entrada y proceso
    while   contadordeaños <=6:
            Valordel_10decada_año=int(input(f"ingrese los porcientos de (10%) de cada año {contadordeaños}:"))
            salario_inicial=salario_inicial+Valordel_10decada_año
            contadordeaños=contadordeaños+1            
    #datos de salida 
    print(f"la suma de los porcentajes de los 6 años es : {salario_inicial}")
    print("salario del primer año es 140 $")
    print("salario del segundo año es 154 $")
    print("salario del terce año es 169 $")
    print("salario de  cuarto año es 186 $")
    print("salario del quinto año es 204 $")
    print("salario del sexto año es 225 $")    
    
    
salariode6añosdelprofesorRMSA()