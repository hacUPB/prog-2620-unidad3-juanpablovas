'''
Crea un menú de opciones (por ejemplo, 1: "Sumar", 2: "Restar", 3: "Salir").
'''

while True:
    print("== ¿Qué operación deseas hacer el día de hoy? ==")
    print("1) Sumar")
    print("2) Restar")
    print("3) Salir")
    opcion = int(input("Ingresa alguna de las anteriores opciones: "))

    match opcion:
        case 1:
            a = int(input("Ingresa un primer numero: "))
            b = int(input("Ingresa un segundo numero: "))
            operacion = a + b
            print(f"{a} + {b} = {operacion}")

        case 2:
            a = int(input("Ingresa un primer numero: "))
            b = int(input("Ingresa un segundo numero: "))
            operacion = a -b
            print(f"{a} - {b} = {operacion}")

        case 3:
            print("Saliendo del programa...")
            break
        case _:
            print("Opción invalida --- saliendo del programa")
            break