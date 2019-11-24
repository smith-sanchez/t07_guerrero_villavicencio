#Decodificar mensaje encriptado
#Nuestra facultad esta de aniversario
#el viernes iremos las pirkas
#que dices, vamor?
#te pago tu pasaje
#lo vamos a pasar super divertido
#sera algo inolvidable

import  os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for letra in msg:
    if letra == "N":
        print("Nuestra facultad esta de aniversario")
    if letra == "I":
        print("el viernes iremos a las pirkas")
    if letra == "D":
        print("que dices,vamos?")
    if letra == "P":
        print("te pago tu pasaje")
    if letra == "S":
        print("lo vamos a pasar super divertido")
    if letra == "A":
        print("sera algo inlvidable")
#FIN ITERADOR

print("fin del bucle")
