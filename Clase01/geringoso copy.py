

def geringoso(cadena):
    capadepenapa = ''
    for c in cadena:
        if c in'aeiou':
            capadepenapa = capadepenapa + c + "p"+ c
        else:
            capadepenapa = capadepenapa + c 
    return(capadepenapa)


palabras=["Banana","manzana","mandarina"]
d ={}
for palabra in palabras:
    d[palabra]=geringoso(palabra)
print(d


