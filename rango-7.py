#imprimir los p primeros numeros elevados a 1/2
import os

#INPUT
p=int(os.sys.argv[1])

#ITERADOR
for i in range(p):
    print(i**(1/2))

#FIN ITERADOR
print("fin del bucle")
