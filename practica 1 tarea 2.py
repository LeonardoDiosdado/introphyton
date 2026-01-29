import math, os

os.sytem("cls")
print("operaciones:\n1.- triangulo\n2.- cuadrado\n3.-circulo\n4.-pentagono\n5.-salir\n")

opcion = int(input("seleccione alguna de las opciones (anteriores): "))

if opcion == 1:
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))
    area = num1 * num2/2
    print ("el resultado de la area: ",area)
    
if opcion == 2:
    num1 = int (input("ingrese el primer numero: "))
    num2 = int (input("ingrese el segundo numero: "))
    area = num1 * num2/2
    print ("el resultado de la area es: ", area)
    
if opcion == 3:
    num1 = int(input("ingrese el primer numero: "))
    area = 3.1416 * num1*num1
    print ("el resultado de la area es: ", area)
    
if opcion == 4:
    num1 = int(input("ingrese el primer numero:"))
    num2 = int(inout("ingresa el segundo numero: "))
    area = num1 * num2/2
    print("el resultado de la area es: ", area)
    
if opcion == 5:
    int(input("salir: "))
    opcion = int(input("seleccione alguna de las opciones (anteriores): "))
    