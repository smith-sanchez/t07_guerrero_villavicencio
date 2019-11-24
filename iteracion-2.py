#Decodificar mensaje encriptado
#los cursos que llevo en la universidad son:
#programacion I
#matematica basica
#analisis matematico I
#tecnicas de estudio
#introduccion a la universidad
#quimica

import os
#INPUT
msg=os.sys.argv[1].upper()

#BUCLE
for letra in msg:
    if letra == "X":
        print("los cursos que llevo en la universidad son:")
    if letra == "P":
        print("programacion I")
    if letra == "B":
        print("mate,atica basica")
    if letra == "M":
        print("analisis matematico I")
    if letra == "T":
        print("tecnicas de estudio")
    if letra == "I":
        print("introduccion a la universidad")
    if letra == "Q":
        print("quimica")
#FIN ITERADOR

print("Fin del bucle")
