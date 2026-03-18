'''
Una tienda ofrece una promocción, por la compra de 3 articulos, el costo del 
elemento de menor valor tiene un descuento del 50%
'''

articulo1 = int(input("Ingrese el precio del articulo 1: "))
articulo2 = int(input("Ingrese el precio del articulo 2: "))
articulo3 = int(input("Ingrese el precio del articulo 3: "))

mayor = 0
menor = 0
inter = 0


if articulo1 > articulo2 and articulo1 > articulo3:
    mayor = articulo1

else:
    menor = articulo1

if articulo2 > articulo1 and articulo2 > articulo3:
    mayor = articulo2

else:
    menor = articulo2

if articulo3 > articulo1 and articulo3 > articulo2:
    mayor = articulo3

else:
    menor = articulo3


Valormenor = menor - (menor*0.5)

if mayor == articulo1 and menor == articulo2:
    inter = articulo3

if mayor == articulo2 and menor == articulo3:
    inter = articulo1

if mayor == articulo1 and menor == articulo3:
    inter = articulo2

valortotal = mayor + Valormenor + inter

print(f"El valor del articulo menor es ${menor}")
print(f"El total a pagar es ${valortotal}")
print(inter)
