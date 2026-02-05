import os

os.system("cls")

print("-----------calculo de sueldo-------------")

sueldo = int(input("\nAnote el sueldo del empleado: $"))

if sueldo< 1000:
    impuesto = 0
else:
    if sueldo>= 1000 and sueldo <= 2000:
    else:
        if sueldo > 2000:
            impuesto = sueldo *.20
            
print("\ne1 impuesto a pagar es: $",impuesto)

sueldo = sueldo - impuesto

print ("\ne1 sueldo neto del empleado es de: $")    