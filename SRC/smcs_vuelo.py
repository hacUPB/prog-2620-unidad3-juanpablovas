consumobase = 1.1504
consumo_headwind = consumobase + (consumobase*0.15)
consumo_tailwind = consumobase - (consumobase*0.03)
reserva_legal = 466 

def calcular_consumo_tramo(distancia, viento):

    if viento == "en contra":
        print("Condición detectada: viento en contra")
        consumo = consumo_headwind * distancia

    elif viento == "a favor":
        print("Condición detectada: viento a favor")
        consumo = consumo_tailwind * distancia

    elif viento in ["cruzado","nulo"]:
        print("Condición detectada: viento cruzado o nulo")
        consumo = consumobase * distancia

    else:
        print("PRECAUCIÓN: Condición no válida, se asume viento nulo")
        consumo = consumobase * distancia

    return consumo

print("Bienvenido al SMCS del ATR 72 - 500")
combustible_inicial= int(input("Ingresa el combustible inicial del vuelo: "))
distancia = int(input("¿Cuántos kilometros tiene la ruta: "))

waypoints = distancia // 50

combustible_actual = combustible_inicial

while combustible_actual > reserva_legal and waypoints > 0:

    waypoints -= 1
    distancia -= 50

    viento = input("Condición del viento (en contra / a favor / cruzado / nulo):  ").lower()

    consumo = calcular_consumo_tramo(50, viento)

    combustible_actual -= consumo
    
    if distancia < 0:
        distancia = 0
    
    print(f"El combustible restante es: {combustible_actual} Kg")
    print(f"Faltan {distancia} km")

if distancia == 0:
    print("vuelo terminado")

elif combustible_actual <= reserva_legal:
    print(f"EMERGENCIA: el combustible restante es {combustible_actual} Kg, a falta de {distancia} Km para llegar al destino, debes desviarte al aeropuerto más cercano")








