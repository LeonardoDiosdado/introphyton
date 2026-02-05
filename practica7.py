import os

os.system("cls")

print("------------------------- conteo binario-----------------")

v = False
while v = True:
    num = int(input("\nIngrese un numero del 1 al 100: "))
    if num < 1 or num > 100:
        os.system("cls")
        print("\numero fuera del rango, intente de nuevo")
    else:
        v = true

print("\numero valido: ",num)

bin = ""
i = num

while i > 0:
    bin = str(i % 2) + bin
    i -i // 2
    
print("el valor biinario es: ",bin)
        