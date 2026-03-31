'''
Tú dijiste

Dado el siguiente bloque de código,¿ que otras buenas practicas de programación podríamos sumar (sin perder perfomance)?

import threading
import time

stock = 10
lock = threading.Lock()

def comprar(nombre, cantidad):
    global stock
    print(f"{nombre} intenta comprar {cantidad} unidades...")

    if stock >= cantidad:
        time.sleep(0.1)
        stock -= cantidad
        print(f"{nombre} compró {cantidad} unidades. Stock restante: {stock}")
    else:
        print(f"{nombre} no pudo comprar, stock insuficiente ({stock})")


cliente1 = threading.Thread(target=comprar, args=("Cliente 1", 7))
cliente2 = threading.Thread(target=comprar, args=("Cliente 2", 7))

cliente1.start()
cliente2.start()
cliente1.join()
cliente2.join()

print(f"Stock final: {stock}") 

'''
# Solución:

'''
Usar el Lock para bloquear el hilo y que solo un hilo acceda al stock
a la vez. De esta forma nos aseguramos evitar errores al calcular el stock. 

'''


import threading
import time

stock = 10
lock = threading.Lock()

def comprar(nombre, cantidad):
    global stock
    print(f"{nombre} intenta comprar {cantidad} unidades...")

    with lock:
        if stock >= cantidad:
            time.sleep(0.1)
            stock -= cantidad
            print(f"{nombre} compró {cantidad} unidades. Stock restante: {stock}")
        else:
            print(f"{nombre} no pudo comprar, stock insuficiente ({stock})")


cliente1 = threading.Thread(target=comprar, args=("Cliente 1", 7))
cliente2 = threading.Thread(target=comprar, args=("Cliente 2", 7))

cliente1.start()
cliente2.start()
cliente1.join()
cliente2.join()

print(f"Stock final: {stock}") 