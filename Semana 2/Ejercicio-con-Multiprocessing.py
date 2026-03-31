"""
En Python hay paralelismo, pero no se logra con hilos (Threads),
sino con procesos (Processes).
El GIL (Global Interpreter Lock). Python permite que varios hilos existan,
pero solo uno ejecuta código de Python a la vez.
Para saltarse el "bloqueo" del GIL y usar varios núcleos de tu CPU al mismo tiempo,
usamos procesos. 
Cada proceso tiene su propia instancia del intérprete de Python y su propia memoria.
Aquí los números se calculan literalmente al mismo milisegundo en núcleos distintos.

"""


import multiprocessing
import time

# 1. Agregamos 'inicio' y 'fin' a los parámetros
def tarea(nombre, inicio, fin):
    for i in range(inicio, fin + 1):
        print(f"Proceso {nombre} en núcleo distinto: {i}")
        time.sleep(0.5)

if __name__ == "__main__":
    # 2. Ahora los argumentos coinciden con la definición de la función
    p1 = multiprocessing.Process(target=tarea, args=("Lógico-1", 1, 5))
    p2 = multiprocessing.Process(target=tarea, args=("Lógico-2", 6, 10))
    
    p1.start()
    p2.start()
    
    # Es buena práctica esperar a que terminen
    p1.join()
    p2.join()
    print("Procesos finalizados.")
    
"""
¿Por qué usamos if __name__ == "__main__":?

Es vital entender esto en Multiprocessing:

En Windows, cuando lanzas un nuevo proceso, Python básicamente "reimporta" 
tu archivo en una instancia nueva del intérprete. Si no tuvieras esa línea, 
el nuevo proceso intentaría crear otros procesos a su vez, creando un bucle 
infinito de procesos que colapsaría tu computadora (una "bomba de fork").

"""