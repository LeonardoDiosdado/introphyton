import math

while true:
    
print("menu de opciones")
print("1. triangulo")
print("2. cuadrado")
print("3. circulo")
print("4. pentagono")
print("5. salir del menu")

opcion = input("selecciona una opcion")

if opcion=="1":
    print("1 selecionado: triangulo")
    base = float (input("ingresar la base:"))
    altura = float(input("ingresa la altura: "))
    area = (base * altura) /2 
    print("el area del triangulo es:")
    
elif opcion == "2":
    print("2 seleccionado: cuadrado")
    lado = float(input("ingrese el lado: "))
    area = lado * 2
    print("el area del cuadrado")
    
elif opcion == 3:
    print("2 seleccionado:circulo")
    radio = float (input("ingrese el radio:"))
    area = pi*radio ** 2
    print("el area del circulo es:")
    
elif opcion == 4:
    print("4 seleccionado: pentagono")
    perimetro = float(input("ingrese el perimetro:"))
    apotema = float(input("ingresa el apotema:"))
    area = ( perimetro * apotema) / 2
    print("el area del pentagono es:")
    
elif opcion == 5:
    print("saliendo a menu...")
    
Else
print("opcion no valida"):