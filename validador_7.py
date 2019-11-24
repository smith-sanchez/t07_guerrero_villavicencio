import os

#DECLARACION DE VARIABLES

masa,aceleracion=0.0,0.0

#imput
masa=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
#processing
fuerza=float(masa*aceleracion)

#VALIDAR LA MAGNITUD FUERZA

fuerza_invalida=True
while(fuerza_invalida):
    fuerza=float(input("ingrese fuerza:"))
    fuerza_invalida=(fuerza !=63)

#fin while
print("fin del bucle")
