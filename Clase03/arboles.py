import csv
from collections import Counter

#Ejercicio 3.18 

def leer_parque(archivo,parque):
    f=open(archivo,encoding="utf8")
    filas= csv.reader(f)
    encabezado=next(f).split(',')
    totalDicc=[]
    
    for fila in filas:
        record=dict(zip(encabezado,fila))      
        if record['espacio_ve']==parque:       
            totalDicc.append(record)       
        else:
            pass
    f.close()
    
    return totalDicc

def especies(lista_arboles):
    especies=[]
    for s in lista_arboles:
        arbol=s['nombre_com']  
        especies.append(arbol)  
        arboles=set(especies)
        
    return arboles

parque= leer_parque('Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")
print(especies(parque))

