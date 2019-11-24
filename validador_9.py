import os

#DECLARACION DE VARIABLES

fuerza,distancia=0.0,0.0

#imput
fuerza=float(os.sys.argv[1])
distancia=float(os.sys.argv[2])
#processing
trabajo=float(fuerza*distancia)

#VALIDAR LA MAGNITUD FUERZA

trabajo_invalido=True
while(trabajo_invalido):
    trabajo=int(input("ingrese trabajo:"))
    trabajo_invalido=(trabajo !=90)

#fin while
print("fin del bucle")
