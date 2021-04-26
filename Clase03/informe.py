#2.18 informe.py
import csv
from pprint import pprint

def leer_camion(archivo):
    camion = []
    total = 0.0
    f = open(archivo, 'rt',encoding="utf-8") 
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                cajon = {}
                cajon['nombre']=record['nombre']
                cajon['cajones']= int(record['cajones'])
                cajon['precio']= float(record['precio'])
                camion.append(cajon)
                total += cajon['cajones']*cajon['precio']
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return camion
    f.close()

def leer_precios(archivo):
    listado = {}
    with open(archivo, 'rt',encoding="utf-8") as f:
        for line in f:
            row= line.split(',')
            try:
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


camiones = leer_camion('Data/fecha_camion.csv')

precios = leer_precios('Data/precios.csv')

balance = informe(camiones, precios)

print(balance)