import random

#genera 5 valores de dados
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    iguales= False
    for x in range(0,len(tirada)):
        if x == 0:
            valor =  tirada[x]
        
        if tirada[x] == valor:
            iguales = True
        else:
            iguales= False
            return iguales
    return iguales
#N=1000
N = 1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

