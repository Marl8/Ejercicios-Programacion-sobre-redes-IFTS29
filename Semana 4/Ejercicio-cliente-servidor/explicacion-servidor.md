## Servidor

### 1. Configuración del "Escuchador"

````python
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
````

Al igual que en el cliente, creamos el socket con IPv4 y TCP.

```python
server.bind(('localhost', 5000))
```

Esta línea es fundamental. ``bind`` (vincular) le dice al sistema operativo: "Resérvame el puerto ``5000`` en esta máquina; cualquier dato que llegue ahí es para mí".

````python
server.listen(1)
````

Pone al servidor en modo "espera". El número 1 indica el tamaño de la cola; es decir, cuántas conexiones pueden esperar en fila mientras el servidor atiende la actual.

### 2. El Ciclo de Vida (El Bucle Infinito)

````python
while True:
````
Un servidor normalmente no se apaga después de una respuesta. Este bucle permite que, tras atender a un cliente, el servidor vuelva arriba y espere al siguiente.

````python
conn, addr = server.accept()
````

- Punto de bloqueo: El programa se detiene aquí hasta que un cliente se conecta.

- Cuando alguien se conecta, accept() devuelve dos cosas:

    - ``conn``: Un nuevo socket específico para hablar con ese cliente.

    - ``addr``: La dirección IP y el puerto del cliente que se conectó.


### 3. Procesamiento de la Información

````python
pais = conn.recv(1024).decode().strip().capitalize()
````
Aquí sucede la magia de la limpieza de datos:

- ``recv(1024).decode()``: Recibe los bytes y los pasa a texto.

- ``.strip()``: Elimina espacios en blanco accidentales al inicio o final.

- ``.capitalize()``: Convierte el texto (ej: "mexico") a formato de título ("Mexico") para que coincida con las llaves del diccionario.

````python
respuesta = datos.get(pais, "No tengo ese país en mi base de datos.")
````
Usamos ``.get()`` en lugar de acceso directo para evitar que el programa falle si el país no existe. Si no lo encuentra, devuelve la frase de error por defecto.

### 4. Respuesta y Cierre

````python
conn.send(respuesta.encode())
````

Envía la capital (o el error) de vuelta al cliente, convertida en bytes.

````python
conn.close()
````
Corta la comunicación con ese cliente específico. El servidor sigue vivo gracias al ``while True``, pero la "llamada telefónica" con ese usuario ha terminado.