'''
Problema 1: contando en paralelo

Escribe un programa en Python que cree dos hilos. 

El primer hilo debe contar los números del 1 al 5, 

mientras que el segundo hilo debe contar los números del 6 al 10. 

Los números de cada hilo deben imprimirse de forma concurrente, 

pero no necesariamente en el mismo orden.
'''


import threading
import time

def contar_numeros_hilo1(nombre):
    for i in range(1, 6):
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        print(f"{nombre} está contando: {i}")

def contar_numeros_hilo2(nombre):
    for i in range(6, 11):
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        print(f"{nombre} está contando: {i}") 
        
# El metodo estático Thread recibe como ARG dos parámetros con la (,) le decimos que el segundo param está vacio       
hilo1 = threading.Thread(target=contar_numeros_hilo1, args=("Hilo 1",))
hilo2 = threading.Thread(target=contar_numeros_hilo2, args=("Hilo 2",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
print("¡Contador completo!")        