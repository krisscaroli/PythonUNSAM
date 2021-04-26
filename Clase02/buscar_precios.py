def buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt')
    headers = next(f).split(',')
    precio = 0.0
    encontrado = False
    for line in f:
            row = line.split(',')
            if(row[0] == fruta):
                precio = row[1]
                encontrado = True

    if encontrado ==True:
        print(f"El precio de un cajón de {fruta} es: {precio}")
    else:
        print(f"{fruta} no figura en el listado de precios.")
    f.close()

buscar_precio('Frambuesa')
buscar_precio('Kale')
fruta=input("Ingresa la fruta a buscar: ")
buscar_precio(fruta)
