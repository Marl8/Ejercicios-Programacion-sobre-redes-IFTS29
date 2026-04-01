# Semáforos

'''
En Python, un Semáforo es una primitiva de sincronización que se utiliza

para limitar el acceso a un recurso compartido. 

A diferencia de un Lock (que es como un cerrojo único), un Semaphore permite

que un número específico de hilos trabajen simultáneamente.

Piénsalo como un estacionamiento con cupos limitados: si hay 5 lugares, entran 5

autos; el sexto debe esperar a que uno salga.

Se usa por ejemplo para limitar el número de conexiones simultaneas una base de datos.
'''

import threading
import time
import random

# Creamos un semáforo que permite máximo 3 hilos a la vez
semaforo = threading.Semaphore(3)

def conectar_servidor(id_hilo):
    print(f"Hilo {id_hilo} intentando conectar...")
    
    with semaforo: # Esto equivale a llamar a acquire() al entrar y release() al salir
        print(f"--- Hilo {id_hilo} HA ENTRADO (Conexión activa) ---")
        time.sleep(random.uniform(1, 3)) # Simulando trabajo
        print(f"--- Hilo {id_hilo} saliendo y liberando espacio ---")

# Lanzamos 6 hilos
hilos = []
for i in range(6):
    thread = threading.Thread(target=conectar_servidor, args=(i,))
    hilos.append(thread)
    thread.start()


'''
¿Qué sucede aquí?

Los primeros 3 hilos entrarán de inmediato.

Los hilos 4, 5 y 6 se quedarán "congelados" en la línea del with semaforo.

En cuanto el hilo 1 termine y haga el release, el hilo 4 entrará automáticamente.
    
'''