#Decodificar mensaje encriptado
#Vamos saliendo en la noche
#Paso por ti
#Nos vamos a comer algo
#Nos vamos a caminar al parque

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for letra in msg:
    if letra == "A":
        print("vamos saliendo en la noche")
    if letra == "B":
        print("paso por ti")
    if letra == "C":
        print("nos vamos a comer algo")
    if letra == "D":
        print("nos vamos a caminar al parque")
#FIN ITERADOR

print("fin del bucle")
