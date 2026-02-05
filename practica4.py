import os

os.system("cls")

print("------------calificaciones----------")

calf = int(input("\nAnote su calificacion: "))

if calf>= 7:
    if calf >= 9:
        print("\nexcelente")
    else:
        print("\nAprobado")
else:
    print("\nReprobado")
    