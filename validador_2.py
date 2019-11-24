import os

#DECLARACION DE VARIABLES

radio,pi=0,0.0

#imput
radio=int(os.sys.argv[1])
pi=float(os.sys.argv[2])
#processing
area=float(radio**2*pi)

#VALIDAR EL AREA DEL CIRCULO

area_invalida=True
while(area_invalida):
    area=float(input("ingrese area del circulo:"))
    area_invalida=(area !=12.565)

#fin while
print("fin del bucle")
