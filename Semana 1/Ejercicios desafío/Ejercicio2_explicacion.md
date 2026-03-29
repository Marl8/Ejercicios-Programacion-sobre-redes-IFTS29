## Ejecución Condicional con Hilos

🔑 Idea clave primero

El ``with condicion``: no depende del orden en el archivo, sino de cuándo se ejecuta en tiempo real.

👉 En concurrencia (hilos), el orden del código escrito ``≠`` orden de ejecución.

🧠 Qué está pasando realmente

Tenés 3 actores:

- Hilo principal
- Hilo 1
- Hilo 2

⏱️ Orden real de ejecución

1. Se crean y arrancan los hilos

````python
hilo1.start()
hilo2.start()
````

👉 En este momento, los hilos empiezan a correr en paralelo.

2. El hilo principal entra al with condicion

````python
with condicion:
    while hilos_terminados < 2:
        condicion.wait()
````

👉 Acá pasa algo MUY importante:

``wait():``
🔒 Libera el lock
😴 Se queda dormido esperando un notify()

3. Los hilos trabajan (con sleep)

````python
for i in range(1, 6):
    time.sleep(1)
````

👉 Cada hilo tarda ~5 segundos

4. Cuando un hilo termina

Ejecuta esto:

````python
with condicion:
    hilos_terminados += 1
    print(...)
    condicion.notify()
````

👉 Esto hace:

- Toma el lock
- Incrementa contador
- 🔔 Hace ``notify()`` → despierta al hilo principal

🔄 Flujo correcto (resumen mental)

````text
Principal:
    entra a wait → se duerme

Hilo 1:
    termina → notify → despierta principal

Principal:
    revisa condición → sigue esperando

Hilo 2:
    termina → notify → despierta principal

Principal:
    sale del while → imprime "¡Contador completo!"
````    