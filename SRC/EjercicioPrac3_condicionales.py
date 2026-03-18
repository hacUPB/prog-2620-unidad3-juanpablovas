'''
Diseña un programa que solicite al usuario la distancia en kilómetros del vuelo 
y el consumo de combustible por kilómetro de la aeronave. Luego, el programa debe 
calcular la carga de combustible requerida y mostrarla. Sin embargo, ten en cuenta 
que en vuelos comerciales se suele incluir un margen de seguridad adicional en la 
carga de combustible para afrontar posibles desvíos o retrasos. Por lo tanto, si 
la distancia del vuelo es menor o igual a 1000 km, se añadirá un 10% adicional a 
la carga de combustible calculada. Si la distancia es mayor a 1000 km, se añadirá 
un 15% adicional.
'''

distancia = int(input("Ingresa la distancia en kilometros de la ruta asignada: "))
consumo = float(input("Ingresa el consumo en kg/km de la aeronave: "))

carga_combustible = distancia * consumo

if distancia <= 1000:
    carga_combustible = carga_combustible + (carga_combustible*0.1)
else:
    carga_combustible = carga_combustible + (carga_combustible*0.15)

print(f"La carga de combustible para este vuelo debe ser de {carga_combustible} kg")


