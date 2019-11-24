#Decodificar mensaje encriptado
#el fin de semana realizo actividades como:
#salir a correr temprano
#ir al mercado
#salir con mi familia a real plaza
#dormir temprano

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for numero in msg:
    if numero == "1":
        print("el fin de semana realizo actividades como:")
    if numero == "2":
        print("salir a correr temprano")
    if numero == "3":
        print("ir al mercado")
    if numero == "4":
        print("salir con mi familia a real plaza")
    if numero == "5":
        print("dormir temprano")
#FIN ITERADOR

print("fin del bucle")
