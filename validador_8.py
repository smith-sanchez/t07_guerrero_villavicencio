import os

#DECLARACION DE VARIABLES

peso,volumen=0.0,0.0

#imput
peso=float(os.sys.argv[1])
volumen=float(os.sys.argv[2])
#processing
peso_especifico=float(peso//volumen)

#VALIDAR LA MAGNITUD PESO ESPECIFICO

peso_especifico_invalida=True
while(peso_especifico):
    peso_especifico=int(input("ingrese peso especifico:"))
    peso_especifico_invalida=(peso_especifico !=10)

#fin while
print("fin del bucle")
