import os

#DECLARACION DE VARIABLES

trabajo,tiempo=0.0,0.0

#imput
trabajo=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])
#processing
potencia=float(trabajo//tiempo)

#VALIDAR LA MAGNITUD POTENCIA

potencia_invalida=True
while(potencia_invalida):
    potencia=int(input("ingrese potencia:"))
    potencia_invalida=(potencia !=13)

#fin while
print("fin del bucle")
