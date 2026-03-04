'''
Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis 
para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. 
Solicite al usuario el valor de la compra y calcule el valor total a pagar.
'''

compra = int(input("Ingresa el valor de la compra: "))
envio = 0

if compra < 100000:
    envio = 9000
    total = compra + envio

print(f"El valor a pagar es ${total}")


