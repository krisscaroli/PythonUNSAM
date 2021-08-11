# hipoteca.py
# Archivo de ejemplo
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=1
pago_extra=1000

while saldo > 0:
    if(mes<=12):
        pago_mensual=pago_mensual + pago_extra
    
    saldo = saldo * (1+tasa/12) - (pago_mensual)
    total_pagado = total_pagado + (pago_mensual)
    mes=mes+1
print(round(total_pagado, 2), mes)
# Ejercicio de hipoteca

