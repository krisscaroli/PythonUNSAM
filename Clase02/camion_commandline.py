# costo_camion.py
import csv
import sys
def costo_camion(nombre_archivo):
        f = open(nombre_archivo, 'rt')
        rows = csv.reader(f)
        headers = next(rows)
        preciototal = 0.0
        for row in rows:
                preciototal= preciototal+ int(row[1])* float(row[2])
        return(preciototal)
        f.close()
        
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)