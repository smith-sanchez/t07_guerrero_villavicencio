#imprimir los "n" primeros numeros divididos entre 4 y multiplicados por 5
import os

#INPUT
n=int(os.sys.argv[1])

#ITERADOR
for i in range(n):
    print(i*(5/4))

#FIN ITERADOR
print("fin del bucle")
