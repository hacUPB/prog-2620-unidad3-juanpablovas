'''
Escribe un programa que solicite al usuario ingresar un número entero positivo n. 
Luego, utiliza un bucle for con la función range() para calcular la suma de todos 
los números pares desde 1 hasta n. Finalmente, muestra el resultado de la suma en pantalla.
'''

n = int(input("Ingresa un número entero positivo: "))
sum = 0

if n > 0:
    for n in range(1, n+1):
        mod = n % 2

        if mod == 0:
            sum = sum + n
    print(sum)