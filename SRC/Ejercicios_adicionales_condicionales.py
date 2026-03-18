contraseña = int(input("Ingresa la contraseña: "))

password = 12345

if contraseña == password:
    print("Contraseña correcta")
    print("acceso permitido")

    nota = float(input("Ingresa tu nota: "))

    if nota >= 0 and nota < 3:
        print("Has perdido la asignatura: Tu nota es BAJA")
    elif nota >= 3 and nota < 4:
        print("Has ganado la asignatura: Tu nota es BASICO")
    elif nota >= 4 and nota < 4.5:
        print("Has ganado la asignatura: Tu nota es ALTO")
    elif nota >= 4.5 and nota <= 5:
        print("Has ganado la asignatura: Tu nota es Superior")

else:
    while True:
        contraseña = int(input("Ingresa de nuevo la contraseña: "))

        password = 12345

        if contraseña != password:
            print("Contraseña incorrecta")
        else: 
            break

    print("Contraseña correcta")
    print("acceso permitido")

    nota = float(input("Ingresa tu nota: "))

    if nota >= 0 and nota < 3:
        print("Has perdido la asignatura: Tu nota es BAJA")
    elif nota >= 3 and nota < 4:
        print("Has ganado la asignatura: Tu nota es BASICO")
    elif nota >= 4 and nota < 4.5:
        print("Has ganado la asignatura: Tu nota es ALTO")
    elif nota >= 4.5 and nota <= 5:
        print("Has ganado la asignatura: Tu nota es Superior")
         
