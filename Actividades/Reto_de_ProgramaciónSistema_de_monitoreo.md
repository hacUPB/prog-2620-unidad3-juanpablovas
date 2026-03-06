# Reto de Programación: Sistema de Monitoreo Combustible y Seguridad en Ruta (SMCS) ✈️

## Idea General
En la aviación comercial, la gestión del combustible es un factor crítico de seguridad y eficiencia. Un avión no solo debe llevar combustible para llegar a su destino, sino también reservas legales para emergencias, desvíos por clima y tiempos de espera. Las condiciones de ruta, como el viento en contra o a favor, alteran dinámicamente el consumo.

## Pregunta inicial
¿Cómo podemos utilizar la lógica computacional para predecir el consumo de combustible de una aeronave en tiempo real y tomar decisiones de desvío automático que garanticen la seguridad del vuelo?

**Respuesta Propuesta**  

La logica computacional se puede usar para predecir el consumo de combustible de una aeronave en tiempo real. En un primer lugar, es importante conocer los datos o infomación de la aeronave, posición, altitud, actitud, velocidad, aceleración, entre otros datos. También, es importante conocer las condiciones atmosfericas para conocer dirección del viento o demás aspectos que afecten el vuelo. Todo esto como datos de entrada para hacer una serie de analisis y tomar decisiones que garanticen la seguridad operacional del vuelo. 

## Desafío
Eres el ingeniero aeronáutico encargado de programar el **SMCS**, un sistema básico a bordo de un bimotor comercial. El avión tiene una ruta programada que consta de **un número de tramos (waypoints)**. Tu programa debe simular el vuelo, calculando el combustible restante después de cada tramo y tomando decisiones críticas si las reservas se ven comprometidas.

**Reglas del Sistema:**

1. **Capacidad Inicial:** El avión despega con un valor de combustible en el tanque en kilogramos.  

2. **Consumo Base:** investiga cuál podría ser un consumo estándar en kilogramos por kilómetro.  

3. **Efecto del Viento:**
    - Si hay viento en contra (Headwind), el consumo aumenta en “digamos” un 20%. Este valor, lo debes investigar tú y lo debes justificar. No puede ser el mismo de los otros grupos.
    - Si hay viento a favor (Tailwind), el consumo se reduce en `otro valor` que investigarás también.
    - Si el viento es cruzado o nulo, el consumo es el base.  

4. Reserva Legal: El avión nunca puede bajar de un valor de combustible (este será el límite que tú debes definir). Si al proyectar el siguiente tramo el combustible caerá por debajo de este límite, el sistema debe emitir una alerta crítica, abortar la ruta y aterrizar en el aeropuerto alterno más cercano

# Bitácora

Tabla de entrada
Tabla de salidas
Tabla de Constantes y Variables de Control

Inicio
    leer Combustible_inicial
    Leer Headwind
    Leer Tailwind
    consumo = 0

    Si Headwing == Si
        Consumo = (Consumo*0.15) + Consumo

    Si Tailwind == Si
        Consumo = Consumo - (Consumo*0.05)
Fin

    


Segun: https://www.globalmilitary.net/es/aircraft/atr-72/

---

ATR 72 - 500
650 kg de combustible por hora
565 km/h 

(650 kg/h) / (565 Km/h) = 1.1504 Kg/km

Consumo base = 1.1504
