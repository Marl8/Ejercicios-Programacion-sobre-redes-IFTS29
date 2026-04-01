# Usando Lock

'''
Cuando usas hilos (threads), todos comparten la misma memoria. 

Si dos hilos intentan modificar la misma variable al mismo tiempo,

ocurre una condición de carrera (race condition) y los datos se corrompen. 

El Lock asegura que solo un hilo a la vez ejecute una sección crítica de código.
'''

import threading
import time

lock = threading.Lock()

def contar_numeros_hilo(nombre):
    for i in range(1, 6):  
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        with lock:
            print(f"{nombre} está contando: {i}")      

# 1. Capturamos el tiempo de inicio
inicio = time.perf_counter()

# El metodo estático Thread recibe como ARG dos parámetros con la (,) le decimos que el segundo param está vacio       
hilo1 = threading.Thread(target=contar_numeros_hilo, args=("Hilo 1",))
hilo2 = threading.Thread(target=contar_numeros_hilo, args=("Hilo 2",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

# 2. Capturamos el tiempo de fin
fin = time.perf_counter()

# 3. Calculamos la diferencia
tiempo_total = fin - inicio

print("-" * 30)
print(f"¡Contador completo!")
print(f"Tiempo de ejecución: {tiempo_total:.2f} segundos")       


'''
Cuando pones el time.sleep(1) dentro del with lock:, el hilo que tiene el candado se va a dormir "abrazado" a él.

El otro hilo se queda esperando en la puerta y no puede hacer nada. Esto anula la ventaja de usar hilos, ya que 

terminan trabajando uno por uno en fila.

Para que trabajen en paralelo pero impriman de forma ordenada, debemos bloquear solo la acción crítica (imprimir)

y dejar el time.sleep(1) afuera.

Cuando ejecutas el código, verás que el tiempo total es de aproximadamente 5 segundos.

Si fuera secuencial (sin hilos): Tardaría 10 segundos (5+5).

Con hilos: Como ambos hacen el sleep(1) al mismo tiempo, el reloj "global" solo avanza 5 segundos mientras

ambos hilos terminan sus tareas.

'''
