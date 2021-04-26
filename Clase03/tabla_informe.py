###2.16 Lista de diccionarios########
import sys
import csv
def leer_camion(archivo):
    camion = []
    total = 0.0
    f = open(archivo, 'rt',encoding="utf-8") 
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            camion.append(record)    
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

def tabla_informe(camion, precios):
    informe=[]
    tupla=()
    for s in camion:
        name=s['nombre']
        cajones=int(s['cajones'])   
        precio=float(precios[name]) 
        preciocompra=float(s['precio'])  
        cambio=precio-preciocompra
        tupla=(name,cajones,precio,cambio)
        informe.append(tupla)
    return informe


headers=('Nombre', 'Cajones', 'Precio', 'Cambio')
 #imprimir encabezados
print (f'{headers[0]:>10} {headers[1]:>10} {headers[2]:>10} {headers[3]:>10}')
print(f'   --------  ---------  ----------  ---------')  
camion= leer_camion('Data/fecha_camion.csv')                      
precios=leer_precios('Data/precios.csv')
informe= tabla_informe(camion, precios)
peso='$'

for nombre, cajones, precio, cambio in informe: #imprimir por fila
    print(f'{nombre:>10s} {cajones:>10d}   {peso:^3}{precio:<10.2f} {cambio:>2.2f}')


