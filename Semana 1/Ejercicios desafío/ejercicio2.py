import threading
import time

hilos_terminados = 0
condicion = threading.Condition() # Generamos la condición

def contar_numeros_hilo(nombre):
    
    # Para hacer operaciones de escritura de una variable creada fuera de la función en Python debemos usar global.
    global hilos_terminados
    
    for i in range(1, 6):
        time.sleep(1)  # Simula un trabajo que toma tiempo (1 segundo por número)
        print(f"{nombre} está contando: {i}")
    
    # Al terminar, usamos la condición para avisar
    with condicion:
        hilos_terminados += 1
        print(f"--- {nombre} HA TERMINADO ---")
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