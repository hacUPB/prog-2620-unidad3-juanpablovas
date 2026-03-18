'''
Crear un Menú donde se puedan elegir 
las cinco operaciones aritméticas básicas: + - * / %
'''
operacion = 0

a = int(input("Ingresa un primer número>>: "))
b = int(input("Ingresa un segundo número>>: "))

print("¿Qué operación deseas hacer con estos dos números. \n 1) Suma\n 2) resta\n 3) Multiplicación\n 4) Division decimal\n 5) Modulo\n")
opcion = int(input("ingresa alguna de las opciones anteriores>>: "))

if opcion == 1:
    operacion = a + b
    print(f"{a} + {b} = {operacion}")

elif opcion == 2:
    operacion = a- b
    print(f"{a} - {b} = {operacion}")

elif opcion == 3:
    operacion = a * b
    print(f"{a} x {b} = {operacion}")

elif opcion == 4:
    operacion = a / b
    print(f"{a} / {b} = {operacion}")

elif opcion == 5:
    operacion = a % b
    print(f"{a} % {b} = {operacion}")
else:
    print("Opción no valida")


