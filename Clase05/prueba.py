def tirar():
    dados = []
    max_counts = [0, 0] #primer indice es cuantas veces aparece
                        #el numero mas repetido, segundo indice
                        #es cual es el numero que aparece esas veces
    tiradas = 0
    #for i in range(5):
    #    dados.append(random.randint(1, 6))
    dados = [3, 3, 3, 2, 2]
    for dado in dados:
        if dados.count(dado) > max_counts[0]:
            max_counts[0] = dados.count(dado) 
            max_counts[1] = dado
    return dados, max_counts

##Ejercicio 5.2, generala no necesariamente servida
def generala():
    import random
    tirada_1 = tirar(5)
    from collections import Counter
    mas_repetido = Counter(tirada_1).most_common()[0][0]
    n_repetido = Counter(tirada_1).most_common()[0][1]
    for i in tirada_1:
        if i != mas_repetido:
            tirada_1.remove(i)
    tirada_2 = tirar((5-len(tirada_1)))
    n_repetido_2 = Counter(tirada_2).most_common()[0][1]
    if  n_repetido_2 > n_repetido : #Esto me previene que en la segunda tirada un valor haya salido mas veces que en la pimera
        mas_repetido = Counter(tirada_2).most_common()[0][0]
        tirada_1 = [mas_repetido]*n_repetido_2 #Siempre me voy a quedar con tirada 1 y aca le indico que ponga el numero repetido tantas veces como aparecio a tirada_2
    else:
        for i in tirada_2:
            if i in tirada_1:
                tirada_1.append(i)
    tirada_3 = tirar((5-len(tirada_1)))
    n_repetido_3 = Counter(tirada_3).most_common()[0][1]
    if  n_repetido_3 > n_repetido and n_repetido_3 > n_repetido_2  : #Esto me previene que en la 3ra. tirada un valor haya salido mas veces que en la pimera
        mas_repetido = Counter(tirada_3).most_common()[0][0]
        tirada_1 = [mas_repetido]*n_repetido_3
    else:
        for i in tirada_3:
            if i in tirada_1:
                tirada_1.append(i)
    return tirada_1
a = generala()
N = 10000000
G = sum([len(generala())==5 for i in range(N)])
prob = G/N
print(f'Jugué {N} manos, de las cuales {G} saqué generala.')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')