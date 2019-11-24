#Decodificar mensaje encriptado
#los dias que mas disfruto en la universidad son
#lunes
#jueves
#viernes

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for letra in msg:
    if letra == "U":
        print("los dias que mas disfruto en la universidad son:")
    if letra == "L":
        print("lunes")
    if letra == "J":
        print("jueves")
    if letra == "V":
        print("viernes")
#FIN ITERADOR

print("fin del bucle")
