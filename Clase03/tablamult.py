
Numeros=[0,1,2,3,4,5,6,7,8,9] 
print (f'  {Numeros[0]:>4} {Numeros[1]:^5} {Numeros[2]:^2} {Numeros[3]:^3} {Numeros[4]:^3} {Numeros[5]:^3} {Numeros[6]:^3} {Numeros[7]:^3} {Numeros[8]:^3} {Numeros[9]:^3}')
print( f'-------------------------------------------')

x=0
for k,i in enumerate(Numeros): 
    indiceTabla=0
    fila=[]
    x=Numeros[i] 
    #añado el primer valor multiplo de 0 
    fila.append(indiceTabla) 
    #Anado el  segundo valor multiplo de 1 que es el mismo numero
    fila.append(x) 
    while indiceTabla<9:         
        x=x+i #sumo hasta conseeguir el multilplo
        indiceTabla=indiceTabla+1
        fila.append(x)  
    print(f'{k:<3}:{fila[0]:^3} {fila[1]:^3} {fila[2]:^3} {fila[3]:^3} {fila[4]:^3} {fila[5]:^3} {fila[6]:^3} {fila[7]:^3} {fila[8]:^3} {fila[9]:^3}')
