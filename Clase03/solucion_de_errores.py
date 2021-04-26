#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era devolver return false cuando no encontraba la letra lo que hacia que ya no se recorrá la cadena y  debia ubicarse el retun false no en el else sino fuera del while
#    Lo corregí cambiando return False afuera del while
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i =i+ 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintaxis donde no tenia ":" después de la función, wuhile e if que no tenia ":" y le faltaba el doble igual, junto a la palabra Falso que no es boleano.
#Lo corregí agregando ":", "=" y el Boolean False
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n :
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de por el tipo de dato que se esperaba era un string y se estaba mandando en el tercer párametro un entero.
#Lo corregí convirtiendo la expresión en string.
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
