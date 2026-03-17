# Biblioteca threading -> https://docs.python.org/es/3.14/library/threading.html

import threading
import time

def contar_numeros(nombre, contador):
    for i in range(1, 6):
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        print(f"{nombre} está contando: {contador + i}")
        
hilo1 = threading.Thread(target=contar_numeros, args=("Hilo 1", 0))
hilo2 = threading.Thread(target=contar_numeros, args=("Hilo 2", 5))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
print("¡Contador completo!")        




