a = int(input("ingresa el primer numero: "))
b = int(input("ingresa el segundo numero: "))
resultado = 0
contador = 0
suma_str = ""

while contador < b:
    resultado += a
    suma_str += str (a)
    if contador < b - 1:
        suma_str += "+"
    contador += 1
    
print(f"{suma_str} = {resultado}")