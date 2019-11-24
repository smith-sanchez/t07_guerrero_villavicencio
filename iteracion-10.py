#Decodificar mensaje encriptado
#algunos distritos de chiclayo son
#la victoria
#monsefu
#chongoyape
#pimentel
#picsi

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for numero in msg:
    if numero == "6":
        print("algunos distritos de chiclayo son:")
    if numero == "1":
        print("la victoria")
    if numero == "3":
        print("monsefu")
    if numero == "5":
        print("chongoyape")
    if numero == "7":
        print("pimentel")
    if numero == "9":
        print("picsi")
#FIN ITERADOR

print("fin del bucle")
