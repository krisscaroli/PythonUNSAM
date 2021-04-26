def tiene_uno(expresion):
    cadena = str(expresion)
    n = len(cadena)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if cadena[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)