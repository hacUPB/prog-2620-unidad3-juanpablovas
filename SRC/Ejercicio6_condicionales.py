'''
Una compañía de paquetería internacional tiene servicio en algunos países según su zona. 
El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. 
Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados 
por seguridad. Usa la siguiente tabla para resolver el problema:

Zona	Ubicación	    Costo/gramo
1	América del Norte	$11
2	América Central	    $10
3	América del Sur	    $12
4	Europa	            $24
5	Asia	            $27
'''
costo_gramo = 0
Weight = float(input("Ingresa el peso en kilogramos del paquete que deseas enviar>>: "))

Weight = Weight * 1000.0

if Weight <= 5000.0:
    destino = int(input("A donde deseas mandar tu paquete:\n 1) América del Norte.\n 2) Amercia Central.\n 3) America del sur. \n 4) Europa \n 5)Asia\n "))

    if destino == 1:
        costo_gramo = 11
    elif destino == 2:
        costo_gramo = 10
    elif destino == 3:
        costo_gramo = 10
    elif destino == 4:
        costo_gramo = 24
    elif destino == 5:
        costo_gramo = 27
    
    valor_envio = Weight * costo_gramo
    print(f"El valor de tu envio es {valor_envio}$")

else:
    print(f"Por seguridad tu paquete de {Weight} kg no puede ser enviado")