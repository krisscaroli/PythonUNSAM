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
    generala=False
    listaRepetida=[]
    generala=max(tirada) == min(tirada)
    if generala != True:
        #1tirada
        c = Counter(tirada)
        valorMaxRepetido=max(c, key=c.get)
        repeticion=tirada.count(valorMaxRepetido)
        listaRepetida.append([valorMaxRepetido]* repeticion)
        #2
        #3
    return generala


def es_generala(tirada):
    generala=False
    generala=max(tirada) == min(tirada)
    if generala != True:
        listaRepetida=[]
        dadosLanzar=0
        #[2,2,3,4,5]
            c = Counter(tirada)
            valorMaxRepetido=max(c, key=c.get)
            repeticion=tirada.count(valorMaxRepetido)
            print(valorMaxRepetido)
            print(repeticion)
            listaRepetida = [valorMaxRepetido]* repeticion
            dadosLanzar=5-repeticion
            ##SEGUNDA PARTIDA
            tirada2= tirar(dadosFaltantes)
            #[2
            # ,4,4]
            #BUSCAR EL VALOR repetido de la primera tirada
            c = Counter(tirada2)
            valorMaxRepetido2=max(c, key=c.get)
            repeticion2=tirada2.count(valorMaxRepetido2)
            dadosLanzar=5-repeticion2
            #comprabamos si la cantidadcompleta lo necesario par 5
            if valorMaxRepetido == repeticion == dadosLanzar:
                generala=True
            else:
                #comparamos el numero de repeticion si es mayor nos que la primera partida nosquedamos con el sino
                if repeticion2 >= repeticion1:
                    listaRepetida=[valorMaxRepetido]* repeticion
                    dadosLanzar=5-repeticion2
            ##TERCERA PARTIDAD
                tirada3=tirar(dadosLanzar)
                c = Counter(tirada3)
                valorMaxRepetido=max(c, key=c.get)
                repeticion=tirada3.count(valorMaxRepetido)



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
    #tirar 2 veces
    listaRepetida.append(valorMaxRepetido)
    dadosFaltantes=5-repeticion
    tiradaDos= tirar(dadosFaltantes)
    c = Counter(tiradaDos)
    valorMaxRepetido=max(c, key=c.get)
    repeticion=tiradaDos.count(valorMaxRepetido)
    print(valorMaxRepetido)
    print(repeticion)
    #tirar 3vez
    dadosFaltantes=5-repeticion
    tiradaDos= tirar(dadosFaltantes)
    c = Counter(tiradaDos)
    valorMaxRepetido=max(c, key=c.get)
    repeticion=tiradaDos.count(valorMaxRepetido)
    print(valorMaxRepetido)
    print(repeticion)

tirada=tirar(5)

#tirada=[1,2,2,3,1] 
print(es_generala(tirada))

