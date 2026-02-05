import os

os.system("cls")

print("---- Comparacion de Edades ----")


edad1 = int(input("Ingrese la edad de la primer persona: "))
edad2 = int(input("Ingrese la edad de la segunda persona: "))

print("\nResultado:")

suma = edad1 > edad2
print("La primera persona es mayor.")
suma = edad2 < edad1
print("La segunda persona es menor.")

print("ya no supe que hacer.")