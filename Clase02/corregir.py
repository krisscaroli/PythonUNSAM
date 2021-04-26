# Geringoso
# Ejemplo Anterior
#cadena = "Geringoso"
#for c in cadena:
#    if c == 'o':
#       print('caracter:', c)

# implemento geringoso

hizoa = 0
hizoe = 0
hizoi = 0
hizoo = 0
hizou = 0

cadena = input('Ingrese una cadena: ')

for c in cadena:
    if c in 'aeiou':
        if c == 'a' and not hizoa:
          cadena1 = cadena.replace('a','apa')
          print(cadena1) 
          cadena = cadena1
          hizoa = 1
        elif c == 'e' and not hizoe:
          cadena1 = cadena.replace('e','epe')
          print(cadena1) 
          cadena = cadena1
          hizoe = 1
        elif c == 'i' and not hizoi:
          cadena1 = cadena.replace('i','ipi')
          print(cadena1) 
          cadena = cadena1
          hizoi = 1
        elif c == 'o' and not hizoo:
          cadena1 = cadena.replace('o','opo')
          print(cadena1) 
          cadena = cadena1
          hizoo = 1
        elif c == 'u' and not hizou:
          cadena1 = cadena.replace('u','upu')
          print(cadena1) 
          cadena = cadena1
          hizou = 1
print(cadena1)