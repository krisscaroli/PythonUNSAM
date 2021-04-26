#Ejercicio 5.2
import random
from collections import Counter
#genera 5 valores de dados
def tirar(numero):
    tirada=[]
    for i in range(numero):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    generala=False
    listaRepetida=[]
    listaRepetida2=[]
    generala=max(tirada) == min(tirada)
    if generala != True:
        #1tirada
        c = Counter(tirada)
        valorMaxRepetido=max(c, key=c.get)
        repeticion=tirada.count(valorMaxRepetido)
        #se guarda los valores repetidos en una lista
        for i in range(repeticion):
            listaRepetida.append(valorMaxRepetido)
        #2tirada
        tirada2=tirar(5-repeticion)
        #se guarda los valores repetidos en la lista
        for i in tirada2:
             listaRepetida.append(i)
        #sacar el maximo  valor repetido de la lista repeticiones2
        c = Counter(listaRepetida)
        valorMaxRepetido=max(c, key=c.get)
        repeticion=listaRepetida.count(valorMaxRepetido)
        #se guarda los valores repetidos en una nueva lista nueva de repeticiones2 debido a que la anterior se lleno
        for i in range(repeticion):
            listaRepetida2.append(valorMaxRepetido)
        #3tirada
        tirada3=tirar(5-repeticion)
        #se guarda los valores repetidos en una nueva lista nueva de repeticiones2 debido a que la anterior se lleno
        for i in tirada3:
            listaRepetida2.append(i)
        #se valida si la cantidad del maximo y minimo es igula seria generala
        generala=max(listaRepetida2) == min(listaRepetida2)

    

    return generala
tirada = [1,2,3,4,5]
es_generala(tirada)
N = 10000
G = sum([es_generala(tirar(5)) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
