import csv
from pprint import pprint

#f = open('../Data/camion.csv')
#filas = csv.reader(f)
#encabezados = next(filas)
#fila = next(filas)
#list(zip(encabezados, fila))
#record = dict(zip(encabezados, fila))

def costo_camion(nombre_archivo):
        f = open(nombre_archivo, 'rt',encoding="utf-8")
        filas = csv.reader(f)
        encabezados = next(filas)
        costototal = 0.0
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                costototal += ncajones * precio
                print(f"{costototal}")
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return(costototal)
        f.close()

costo = costo_camion('Data/fecha_camion.csv')
print('Costo total:', costo)