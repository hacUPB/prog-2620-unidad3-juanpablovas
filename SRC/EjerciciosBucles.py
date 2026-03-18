'''
Primer ejercicio

numero = 1

while numero <=5:
    print(numero)
#   numero = numero + 1
    numero += 1


# Ejercicio 2: Imprime los numeros del 5 al 50, pero de 5 en 5
numero = 5

while numero <=50:
    print(numero)
    numero += 5


#Ejercicio 3 Ir del 100 al 0
numero = 100

while numero >50:
    res = numero % 2
    if res == 1:
        print(numero)
    numero -= 1


numero = 5
while numero > 0:  
    print(numero)
    numero += 1



# Solicitar dos numeros e imprimir los valores pares que hay entre dichos números


n1 = int(input("Ingrese un primer numero: "))
n2 = int(input("Ingrese un segundo numero: "))

if n1 > n2:
    mayor = n1
    menor = n2
else:
    mayor = n2
    menor = n1

while mayor >= menor:
    res = mayor % 2

    if res == 0:
        print(mayor)
    mayor -=1
---

password = "Juan02"

intpassword = input("Ingresa la contraseña: ")

while password != intpassword:
    print("CONTRASEÑA INCORRECTA")
    intpassword = input("Ingresa de nuevo la contraseña: ")

print ("ACCESO PERMITIDO")


for i in range(10):
    print(i)
    i += 1
# primer numero desde donde, el segundo hastas donde sin incluirlo y el tercero sera el incremento

'''

for i in range(1, 11):
    print(f"5 x {i} = {5*i}")
    i += 1