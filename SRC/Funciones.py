'''
def factorial(numero):
    if numero >= 0:
        acumulador = 1
        for factor in range(1, numero+1):
            acumulador *= factor
    else:
        acumulador = f"no esta defnido el factorial de {numero}"

    return acumulador 

resultado = factorial(-1)
print(resultado)
---------------------------------------------------------------------

mensaje = "Universidad"
# print(type(mensaje))
#print(dir(str))
msj2 = mensaje.capitalize()
print(msj2)
'''

# Función menu: imprime un menu y retorna la opcion elegida  por el usuarior.

def menu():
    opcion = 0
    while opcion <1  or opcion > 4:
        print("1.suma\n2. Resta\n3 .Multiplicación\n4. Division")
        opcion = int(input("Seleccione una opción: "))

        if opcion <1 or opcion>4:
            print("Operación no valida...\n")
    return opcion

operacion = menu()
print(f"El usuario eligió la opción {operacion}")

if operacion == 1:
    pass
elif operacion == 2:
    pass
elif operacion == 3:
    pass
elif operacion == 4:
    pass