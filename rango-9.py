#imprimir los "b" primeros numeros multiplicados por menos 1/2
import os

#INPUT
b=int(os.sys.argv[1])

#ITERADOR
for i in range(b):
    print(i*(-1/2))

#FIN ITERADOR
print("fin del bucle")
