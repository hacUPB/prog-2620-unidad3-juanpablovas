print("Ingresa lo datos solicitados para conocer si se te otorgará una beca")
promedio = int(input("Ingresa tu promedio: "))
nivel_soc = int(input("Ingresa tu nivel socioeconómico: "))

First_Cond = promedio >= 9
Second_Cond = nivel_soc == 1 and promedio > 8
Decision = First_Cond or Second_Cond

print("Se te dará la beca: ", Decision)
