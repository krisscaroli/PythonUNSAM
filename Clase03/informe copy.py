#2.18 informe.py
import csv
from pprint import pprint

def leer_camion(archivo):
    camion = []
    total = 0.0
    with open(archivo, 'rt',encoding="utf-8") as f:
        rows = csv.reader(f)
        next(f)
        for row in rows:
            cajon = {}
            cajon['nombre']=row[0]
            cajon['cajones']= int(row[1])
            cajon['precio']= float(row[2])
            camion.append(cajon)

    return camion

def leer_precios(archivo):
    listado = {}
    with open(archivo, 'rt',encoding="utf-8") as f:
        for line in f:
            row= line.split(',')
            try:
                print(float(row[1]))
                listado[row[0]] = float(row[1])
            except:
                pass

    return listado

def informe(precio_pagado, precio_venta):
    costo = 0.0
    venta = 0.0
    diferencia = 0.0

    for lista in precio_pagado:
        costo += lista['cajones']*lista['precio']
        for dicc in precio_venta:
            if lista['nombre'] in dicc:
                venta+= lista['cajones']*precio_venta[dicc]
    diferencia = venta -costo 

    if diferencia > 0:
        balance = f' Recaudo de la venta: ${venta} \n Costo camión: ${costo}\n Ganancia: ${round(diferencia,2)}'
    else:
        balance = f' Recaudo de la venta: ${venta} \n Costo camión: ${costo}\n Perdida: ${round(diferencia,2)}'
    
    return balance


camiones = leer_camion('Data/camion.csv')
precios = leer_precios('Data/precios.csv')
print(camiones)
print(precios)
balance = informe(camiones, precios)

print(balance)