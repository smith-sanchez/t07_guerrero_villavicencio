import os

#DECLARACION DE VARIABLES

base,altura=0,0

#imput
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])
#processing
area=int(base*altura//2)

#VALIDAR EL AREA DEL TRIANGULO

area_invalida=True
while(area_invalida):
    area=int(input("ingrese area del triangulo:"))
    area_invalida=(area !=9)

#fin while
print("fin del bucle")
