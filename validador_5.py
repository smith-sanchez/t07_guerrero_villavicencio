import os

#DECLARACION DE VARIABLES

velocidad,tiempo=0.0,0.0

#imput
velocidad=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])
#processing
distancia=float(velocidad*tiempo)

#VALIDAR LA DISTANCIA

distancia_invalida=True
while(distancia_invalida):
    distancia=float(input("ingrese distancia:"))
    distancia_invalida=(distancia !=67.2)

#fin while
print("fin del bucle")
