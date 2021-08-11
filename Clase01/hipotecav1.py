# hipoteca.py
# Archivo de ejemplo
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra=1000
pago_mensual_total=0
while saldo > 0:
    mes=mes+1
    if(mes<=12):
        pago_mensual_total=pago_mensual + pago_extra
    else:
        pago_mensual_total=pago_mensual
        
    saldo = saldo * (1+tasa/12) - (pago_mensual_total)
    total_pagado = total_pagado + pago_mensual_total
    
print("total pagado:",round(total_pagado, 2)," meses:", mes)
# Ejercicio de hipoteca

