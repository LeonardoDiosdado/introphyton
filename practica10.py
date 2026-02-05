import os

os.system("cls") 

numero = int(input("Ingresa un número para la altura de la pirámide: "))

print("\npiramide:\n")

for i in range(1, numero + 1):
    print("*" * i)