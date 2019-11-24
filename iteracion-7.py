#Decodificar mensaje encriptado
#hoy en la tarde habra partido en el estadio
#ira bastante gente
#la entrada es libre
#ire con dos amigas
#si gustas vamos

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for letra in msg:
    if letra == "E":
        print("hoy en la tarde habra partido en el estadio")
    if letra == "G":
        print("ira bastante gente")
    if letra == "L":
        print("la entrada es libre")
    if letra == "A":
        print("ire con dos amigas")
    if letra == "V":
        print("si gustas vamos")
#FIN ITERADOR

print("fin del bucle")

