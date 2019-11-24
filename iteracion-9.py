#Decodificar mensaje encriptado
#Mis hermanos se llaman:
#Nicole
#David
#Viviana
#Ellos son muy importante para mi

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for numero in msg:
    if numero == "1":
        print("mis hermanos se llaman")
    if numero == "2":
        print("Nicole")
    if numero == "3":
        print("David")
    if numero == "4":
        print("Viviana")
    if numero == "5":
        print("ellos son muy importantes para mi")
#FIN ITERADOR

print("fin del bucle")
