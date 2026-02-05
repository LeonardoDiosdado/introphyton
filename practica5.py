import os

os.system("cls")

print("---------------calculo promedio-------------")

#pedir al usuario 5 calificaciones, despues de pedirlas, imprimir el promedio

i = 1
suma = 0

while i <= 5:
    calf = int(input("\nAnote la calificacion{}:".format(i)))
    i = i + 1
    suma = suma + calf
    
prom = suma / 5
print("\nEl promedio del alumno es: ",prom)
