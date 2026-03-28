'''
Sincronización de hilos 

Crea un programa que simule dos hilos sumando números.

Ambos hilos deben sumar números del 1 al 5, pero no deben imprimir el 

resultado de la suma hasta que ambos hayan completado la suma de los 5 números. 

Utiliza una variable de condición para asegurar que los resultados solo se 

impriman una vez que ambos hilos hayan terminado su tarea.
'''


import threading
import time

hilos_terminados = 0
condicion = threading.Condition() # Generamos la condición

def contar_numeros_hilo(nombre):
    
    # Para hacer operaciones de escritura de una variable creada fuera de la función en Python debemos usar global.
    global hilos_terminados
    suma_total = 0
    
    for i in range(1, 6):
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        suma_total += i
        print(f"{nombre} sumando: {i} (Total parcial: {suma_total})")
    
    # Al terminar, usamos la condición para avisar
    with condicion:
        hilos_terminados += 1
        print(f"--- {nombre} finalizó con un total de: {suma_total} ---")
        # Notificamos a quien esté esperando (el hilo principal)
        condicion.notify()    

# El metodo estático Thread recibe como ARG dos parámetros con la (,) le decimos que el segundo param está vacio       
hilo1 = threading.Thread(target=contar_numeros_hilo, args=("Hilo 1",))
hilo2 = threading.Thread(target=contar_numeros_hilo, args=("Hilo 2",))

hilo1.start()
hilo2.start()

# El hilo principal espera aquí
with condicion:
    while hilos_terminados < 2:
        condicion.wait()  # Se bloquea hasta recibir un notify()

print("¡Contador completo!")        


'''
El desglose paso a paso

Para visualizarlo mejor, mira cómo se va acumulando la variable suma_total
en cada vuelta del bucle for:

Iteración	Valor de i	Operación	Suma Acumulada
    1ª	          1	       0+1	         1
    2ª	          2	       1+2	         3
    3ª	          3	       3+3	         6
    4ª	          4	       6+4	         10
    5ª	          5	       10+5          15
'''
