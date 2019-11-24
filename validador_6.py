import os

#DECLARACION DE VARIABLES

base_mayor,base_menor=0,0

#imput
base_mayor=int(os.sys.argv[1])
base_menor=int(os.sys.argv[2])
#processing
base_media=float((base_menor+base_menor)//2)

#VALIDAR LA LONGITUD DE LA BASE MEDIA

base_media_invalida=True
while(base_media_invalida):
    base_media = float(input("ingrese base media:"))
    base_media_invalida = (base_media !=7.5)


#fin while
print("fin del bucle")
