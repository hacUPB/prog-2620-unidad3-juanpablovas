
'''

El Ministerio de Salud clasifica las personas según las etapas del ciclo de vida, 
con el fin de tener una idea sobre su vulnerabilidad. Diseñe un algoritmo que pida 
al usuario su edad y la clasifique según la etapa del ciclo de vida que le corresponda. 
Verifique que el usuario no ingrese valores menores a cero. Clasificación etaria de la 
población colombiana:

- Infancia [0-6) años)
- Niñez [6 - 12) años)
- Adolescencia (12 - 20 años)
- Juventud (20 - 25 años)
- Adultez (25- 60 años)
- Ancianidad / Vejez (60 años o más)

'''

edad_ingresada = int(input("Ingresa tu edad>>: "))
print(edad_ingresada)

if edad_ingresada >= 0 and edad_ingresada < 6 :
    print("Te encuentras  en el cilo de vida de infancia.")
elif edad_ingresada >= 6 and edad_ingresada < 12:
    print("Te encuentras en la niñez.")
elif edad_ingresada >= 12 and edad_ingresada < 20:
    print("Te encuentras en la adolescencia.")
elif edad_ingresada >= 20 and edad_ingresada < 25:
    print("Te encuentras en la juventud.")
elif edad_ingresada >= 25 and edad_ingresada < 60:
    print("Te encuentras en la adultez.")    
elif edad_ingresada >= 60:
    print("Te encuentras en la vejez.")   
else:
    print("Edad no valida")

