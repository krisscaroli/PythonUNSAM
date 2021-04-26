import random
from collections import Counter
#genera 5 valores de dados
def tirar(numero):
    tirada=[]
    for i in range(numero):
        tirada.append(random.randint(1,6)) 
    print(tirada)
    return tirada

def es_generala(tirada):
    iguales= False
    repeticion=0
    listaRepetida=[]
    dadosFaltantes=0
    c = Counter(tirada)
    valorMaxRepetido=max(c, key=c.get)
    repeticion=tirada.count(valorMaxRepetido)
    print(valorMaxRepetido)
    print(repeticion)
    #tiras 2 ves
    
    listaRepetida.append(valorMaxRepetido)
    dadosFaltantes=5-repeticion
    tiradaDos= tirar(dadosFaltantes)
    c = Counter(tiradaDos)
    valorMaxRepetido=max(c, key=c.get)
    repeticion=tiradaDos.count(valorMaxRepetido)
    print(valorMaxRepetido)
    print(repeticion)
    if listaRepetida
    #tirar 3vez
    dadosFaltantes=5-repeticion
    tiradaDos= tirar(dadosFaltantes)
    c = Counter(tiradaDos)
    valorMaxRepetido=max(c, key=c.get)
    repeticion=tiradaDos.count(valorMaxRepetido)
    print(valorMaxRepetido)
    print(repeticion)
    #

tirada=tirar(5)

#tirada=[1,2,2,3,1] 
es_generala(tirada)

N = 1000000
G = sum([es_generala(tirada for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')