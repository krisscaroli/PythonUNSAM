def costo_camion(nombre_archivo):
        f = open(nombre_archivo, 'rt')
        headers = next(f).split(',')
        preciototal = 0.0
        for n_fila, fila in enumerate(f, start=1):
            try:
                row = fila.split(',')
                preciototal= preciototal+ int(row[1])* float(row[2])
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return(preciototal)
        f.close()

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)