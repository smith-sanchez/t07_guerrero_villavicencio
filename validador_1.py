import os

#DECLARAR VARIABLES
cateto1,cateto2,=0.0,0.0

#imput
cateto1=float(os.sys.argv[1])
cateto2=float(os.sys.argv[2])

#processing
import math
hipotenusa=math.sqrt(cateto1**2+cateto2**2)

#VALIDAR LA LONGITUD DE LA HIPOTENUSA

hipotenusa_invalida=True
while(hipotenusa_invalida==True):
    hipotenusa=int(input("ingrese hipotenusa:"))
    hipotenusa_invalida=(hipotenusa !=5)

#fin while
print("fin del bucle")
