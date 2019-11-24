#Decodificar mensaje encriptado
#es verano!
#vamos a la playa
#vamos dandose tiempo este fin de semana
#llevare mi carro para llevar un poco de gente

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for letra in msg:
    if letra == "V":
        print("es verano!")
    if letra == "P":
        print("vamos a la playa")
    if letra == "F":
        print("vamos dandose tiempo este fin de semana")
    if letra == "L":
        print("llevare mi carro para llevar un poco de gente")
#FIN ITERADOR

print("fin del bucle")
