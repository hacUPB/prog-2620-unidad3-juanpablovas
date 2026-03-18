'''
Solicite al usuario un número entre 1 y 7, según la opción elegida, 
imprima en pantalla el día de la semana correspondiente. 1 corresponde al lunes.
'''

num = int(input("Ingresa un número del 1 al 7>>: "))

if num >= 1 and num <=7:

    if num == 1:
        print("lunes")
    if num == 2:
        print("martes")
    if num == 3:
        print("miercoles")
    if num == 4:
        print("jueves")
    if num == 5:
        print("viernes")
    if num == 6:
        print("sabado")
    if num == 7:
        print("domingo")
else:
    print("opción no valida")