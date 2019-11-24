#imprimir los "p" primeros numeros elevados al cubo
import os

#INPUT
p=int(os.sys.argv[1])

#ITERADOR
for i in range(p):
    print(i**3)

#FIN ITERADOR
print("fin del bucle")
