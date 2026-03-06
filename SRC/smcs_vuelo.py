'''
Inicio
    leer Combustible_inicial
    Leer Headwind
    Leer Tailwind
    consumo = 0

    Si Headwing == Si
        Consumo = (Consumo*0.15) + Consumo

    Si Tailwind == Si
        Consumo = Consumo - (Consumo*0.05)
Fin
'''
consumobase = 1.1504
consumo = 0


print("Bienvenido a SMCS del ATR 72 - 500")
Combustible_Inicial = int(input("Ingresa el combustible inicial del vuelo: "))
Headwind = input("¿Tienes viento en contra?: ")
Tailwind = input("¿Tienes viento a favor?:")
waypoints = int(input("¿Cuántos kilometros tiene la ruta: "))


# print(f"Combustible total: {Combustible_Inicial} kg")
# print(f"Viento en contra: {Headwind.lower()}")
# print(f"Viento a favor: {Tailwind.lower()}")

alcance = consumo * waypoints

while Combustible_Inicial >= Combustible_Inicial*0.3:
    if Headwind == "si":
        consumo = (consumobase*0.2) + consumobase





