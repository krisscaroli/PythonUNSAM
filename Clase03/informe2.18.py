#2.18 informe.py
import csv
from pprint import pprint

def leer_camion(archivo):
    camion = []
    total = 0.0
    with open(archivo, 'rt') as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            cajon = {}
            cajon['nombre']=row[0]
            cajon['cajones']= int(row[1])
            cajon['precio']= float(row[2])
            camion.append(cajon)
            total += cajon['cajones']*cajon['precio']

    return camion

def leer_precios(archivo):
    listado = {}
    with open(archivo, 'rt') as f:
        for line in f:
            row= line.split(',')
            try:
                listado[row[0]] = float(row[1])
            except:
                pass

    return listado

def informe(precio_pagado, precio_venta):
    balance = 0
    costo_camion = 0
    #recaudacion = 0

    for row in precio_pagado:
        costo_camion += row['cajones']*row['precio']

        print(f"costo: {costo_camion}")
        return balance


camiones = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
print(camiones)
print(precios)
balance = informe(camiones, precios)

print(balance)