import os

os.system("cls")

while True:
    try:
        entrada = input("Ingrese un número para ver su tabla: ")
        numero = int(entrada)
        break
    except ValueError:
        print("¡Error! Debes ingresar un número entero (ej: 5, 10, 2).")

print(f"\n Tabla del {numero} \n")

for i in range(1, 100):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado:3}")