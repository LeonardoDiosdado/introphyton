import os

os.system("cls")

sueldos = []

cont = 0

print("--- Ingreso de Sueldos ---\n")

while cont < 5:
    try:
        entrada = float(input(f"Dame el sueldo {cont + 1}: "))
        
        sueldos.append(entrada)
        
        cont += 1 
        
    except ValueError:
        print("¡Error! Por favor ingresa un número válido.")

print("\n------------------------------")
print("Lista completa:", sueldos)


sueldo_alto = max(sueldos)  
sueldo_bajo = min(sueldos)  
suma_total  = sum(sueldos)  
promedio    = suma_total / len(sueldos) 

print(f"\nResumen:")
print(f"Sueldo más alto: {sueldo_alto}")
print(f"Sueldo más bajo: {sueldo_bajo}")
print(f"Suma total:      {suma_total}")
print(f"Promedio:        {promedio}")