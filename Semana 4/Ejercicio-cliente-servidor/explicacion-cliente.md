## Cliente

### 1. Preparación del Socket

````python
import socket
````

Importa la librería estándar de Python para comunicaciones en red. Sin esto, no podrías crear "enchufes" (sockets) para conectar programas.

````python
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
````

Aquí creas el objeto socket.

- ``socket.AF_INET`` indica que usarás direcciones IPv4.

- ``socket.SOCK_STREAM`` indica que usarás el protocolo TCP, que es confiable y asegura que los datos lleguen en orden.

````python
cliente.connect(('localhost', 5000))
````
El cliente intenta se conecta con el servidor a través del ``localhost`` en el pueto ``5000``.


### 2. Interacción con el usuario

````python
pais = input("Escribe el nombre de un país para saber su capital: ")
````

Detiene el programa un momento para que escribas un texto por teclado y lo guarda en la variable pais.

### 3. Comunicación (Envío y Recepción)

````python
cliente.send(pais.encode())
````

Envío: Envía el texto al servidor.

***Nota: Los sockets solo envían bytes, no texto plano. Por eso usamos .encode(), que convierte el String en un formato que el cable pueda transportar (UTF-8 por defecto).***

````python
respuesta = cliente.recv(1024).decode()
````

Recepción: El programa se queda esperando a que el servidor responda.

- ``1024`` es el tamaño del "buffer" (cuánta información máxima puede recibir de golpe).

- ``.decode()`` hace lo contrario al paso anterior: convierte los bytes recibidos de vuelta a texto legible para humanos.

````python
print(f"--- Respuesta del servidor: {respuesta} ---")
````

Muestra en tu pantalla lo que el servidor te contestó.


### 4. Gestión de errores y Cierre

````python
except ConnectionRefusedError:
````

Si intentas conectarte pero el servidor no existe o no está encendido en el puerto 5000, Python lanzará esta excepción específica y ejecutará el mensaje de error en lugar de "romperse".

````python
finally:
````
Este bloque se ejecuta siempre, pase lo que pase (haya error o no).

````python
cliente.close()
````
Cierra la conexión. Es una buena práctica para liberar los recursos de red y no dejar puertos "colgados".