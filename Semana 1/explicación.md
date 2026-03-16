## Explicación

Este código es un ejemplo clásico de programación concurrente. La idea principal es que el programa no hace una cosa después de la otra de forma lineal, sino que lanza "sub-procesos" (hilos) que trabajan al mismo tiempo.

Aquí tienes el desglose paso a paso:

1. Preparación de las herramientas

````python
import threading
import time

````
**threading:** Es la librería que nos permite crear y gestionar hilos (threads). Sin ella, Python solo podría hacer una tarea a la vez.

**time:** La usamos específicamente por la función sleep, que nos sirve para pausar la ejecución y simular que el procesador está "trabajando" en algo.


2. Definición de la tarea (contar_numeros)

````Python
def contar_numeros(nombre, contador):
    for i in range(1, 6):
        time.sleep(1)
        print(f"{nombre} está contando: {contador + i}")
````

Esta es la "receta" que seguirán los hilos.

Cada hilo contará 5 números (del 1 al 5).

``time.sleep(1):`` Esta línea es clave. Hace que el hilo se detenga 1 segundo. En ese segundo de "descanso", el procesador aprovecha para darle turno al otro hilo. Por eso en la salida ves que se intercalan.

3. Creación de los hilos

````python
var hilo1 = threading.Thread(target=contar_numeros, args=("Hilo 1", 0))
var hilo2 = threading.Thread(target=contar_numeros, args=("Hilo 2", 5))
````

Aquí defines los objetos, pero aún no se están ejecutando:

**target:** Le dices qué función debe ejecutar.

**args:** Son los argumentos que le pasas a esa función. Nota que el hilo1 empieza desde 0 y el hilo2 desde 5.

4. El Gran Inicio

````Python
hilo1.start()
hilo2.start()
````

Al llamar a ``.start()``, Python le dice al sistema operativo: "Oye, ejecuta estas funciones en paralelo". A partir de aquí, el hilo1 y el hilo2 corren de forma independiente al programa principal.

5. La espera ordenada ``(join)``

````Python
hilo1.join()
hilo2.join()
print("¡Contador completo!")
````
``.join()`` es como un semáforo en rojo para el programa principal. Le dice: "No pases a la siguiente línea (el print final) hasta que este hilo haya terminado su trabajo".

Si no pusieras los ``.join()``, verías el mensaje "¡Contador completo!" al principio de todo, porque el programa principal terminaría antes que los hilos.

¿Por qué la salida sale intercalada?

Imagina que el procesador es un cocinero.

- El Hilo 1 empieza a cocinar (contar) pero se detiene 1 segundo a esperar que hierva el agua (sleep).

- El cocinero no se queda quieto; aprovecha ese segundo para atender al Hilo 2.

- El Hilo 2 también se detiene a esperar, y el cocinero vuelve al Hilo 1.