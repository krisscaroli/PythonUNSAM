def costo_camion(nombre_archivo):
        f = open(nombre_archivo, 'rt')
        headers = next(f).split(',')
        preciototal = 0.0
        for line in f:
                row = line.split(',')
                preciototal= preciototal+ int(row[1])* float(row[2])
        return(preciototal)
        f.close()

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)