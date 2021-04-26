f = open('../Data/precios.csv', 'rt')
headers = next(f).split(',')
precio = 0.0
encontrado = False
for line in f:
        row = line.split(',')
        if(row[0] == "Naranja"):
            precio = row[1]
            encontrado = True
        
        

if encontrado ==True:
    print("El precio de la naranja es: " +precio)
else:
    print("El precio de la naranja no se encontro")

int('N/A')    

f.close()