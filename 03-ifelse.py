'''
Docstring for 03-ifelse
la sentencia 1f-else es una estructura de control que permite ejecutar
diferentes bloquesmde codigo en funcion de una condicion 
'''


import math, os



os.system("cls")
print("---- Grupos ico201-9")



num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero"))

suma = num1 + num2
print("la suma de {} y {} es {}".format(num1, num2, suma))
    
resta = num1 - num2
print("la resta de {} y {} es {}".format(num1, num2, resta))
      
multiplicacion = num1 * num2
print("la multiplicacion de {} y {} es {}".format(num1, num2, multiplicacion))

divicion = num1 / num2
print("la divicion de {} y {} es {}".format(num1, num2, divicion))

potencia = num1 ** num2
print("la potencia de {} y {} es {}".format(num1, num2, potencia))   

print("operaciones basicas:\n1,- suma\n2,- resta-\n3,- multiplicacion\n4,- division\n")
    
opcion=input("ingrese la operacion al realizar (1/2/3/4):")

val1 = 3
val2 = 5
    
temp = val1 > val2
print("el valor de la comparacion es:", temp)

temp = val1 > val2 #false
temp = val1 == val2 #false
temp = val1 < val2 #true
temp = val1 >= val2 #false
temp = val1 <= val2 #true
temp = val1 != val2 #true

temp = not(val1 > val2)#true
print("el valor de la comparacion:", temp)
temp2 = not (val1 > val2) and (val1 < val2) #true
            #not(false)             #true
