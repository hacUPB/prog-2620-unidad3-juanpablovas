edad_usuario = int(input("Ingresa tu edad: ")) 
saldo_billetera = float(input("Ingresa el saldo en tu billetera")) 
Suscripcion = int(input("Si eres premium presiona 1, de lo contrario presiona 2: "))
Valor_juego = 60

First_Cond = edad_usuario >= 17
Second_Cond = saldo_billetera >= Valor_juego
Three_Cond = Suscripcion == 1

Compra_exitosa = First_Cond and Second_Cond 
Descuento = Valor_juego * 0.10

Compra_total = Compra_exitosa and Three_Cond

Valor_total = Valor_juego - Descuento

print("Tu compra fue exitosa?: ", Compra_exitosa)
print("Tuviste descuento?", Compra_total)
print("El valor de tu compra es: ", Valor_total)

