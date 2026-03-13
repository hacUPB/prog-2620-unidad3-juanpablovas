ValorCuenta = float(input("Ingresa el valor de la cuenta: "))

Propina = ValorCuenta * 0.15
TotalPagar = ValorCuenta + Propina
ValorIndividual = TotalPagar / 4

print("El valor de la propina es: ", Propina)
print("El total a pagar es: ", TotalPagar)
print("El valor que debe pagar cada uno es: ", ValorIndividual)

