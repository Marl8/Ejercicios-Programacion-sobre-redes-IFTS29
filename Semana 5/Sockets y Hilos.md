## Socket y Hilos

Entender cómo se gestionan los File Descriptors (FD) cuando mezclamos sockets, hilos y asincronía es clave para construir servidores escalables. Vamos por partes, desde lo físico hasta lo lógico.

### 1. El Socket y el File Descriptor (FD)

En sistemas tipo Unix (Linux/macOS), todo es un archivo. Cuando creas un socket en Python con ``socket.socket()``, el Sistema Operativo (SO) te devuelve un número entero pequeño llamado File Descriptor.

- Este FD es el índice en una tabla que apunta a una estructura de datos en el kernel.

***Importante: El puerto (ej. 8080) es un recurso de red, mientras que el FD es el "mango" que usa tu programa para agarrar ese recurso.***

### 2. Escenario A: Multi-threading (Hilos)

Cuando usas la librería threading, todos los hilos comparten el mismo espacio de memoria y la misma tabla de File Descriptors del proceso padre.

#### ¿Cómo funciona la asignación?

- ``Socket de Escucha``: Creas un socket principal (FD 3, por ejemplo) que hace bind al puerto y listen.

- El ``Bucle accept()``: Corres un bucle que llama a conn, addr = server_socket.``accept()``.

- ``Nuevo FD``: Cada vez que un cliente se conecta, el SO genera un nuevo File Descriptor (FD 4, FD 5, etc.) para esa conexión específica. El puerto de origen del servidor sigue siendo el mismo, pero el FD es único.

- ``Delegación``: Pasas el objeto conn (que contiene el FD) a un nuevo hilo: ``threading.Thread(target=handler, args=(conn,)).start()``.

#### El problema de los hilos:

Aunque cada hilo maneja su propio FD, el GIL (Global Interpreter Lock) de Python impide que los hilos ejecuten código Python en paralelo. Sin embargo, para sockets esto no es tan grave porque las operaciones de red son I/O bound y liberan el GIL mientras esperan datos.

### 3. Escenario B: Agregando Asincronía (asyncio)

Aquí es donde la magia cambia. En lugar de tener muchos hilos esperando, tienes un Event Loop en un solo hilo.

#### ¿Cómo cambia la gestión?

En lugar de bloquear un hilo esperando un FD, asyncio utiliza mecanismos del ``kernel`` como ``epoll`` (Linux) o ``kqueue`` (macOS).

- **Registro**: Le dices al kernel: "Avísame cuando el FD 4 tenga datos".

- **No Bloqueo**: El programa sigue haciendo otras cosas.

- **Callback/Future**: Cuando llegan bits al puerto, el kernel despierta al Event Loop, que sabe exactamente a qué corrutina entregarle los datos basándose en el número de FD.

#### ¿Qué pasa si combinas ambos?

Si ejecutas sockets asíncronos pero necesitas hilos (por ejemplo, para procesar datos pesados sin bloquear el loop), usas ``loop.run_in_executor()``.

- El socket recibe los datos de forma asíncrona (FD gestionado por el Loop).

- Los datos se pasan a un hilo del pool para cálculo intenso.

- El hilo devuelve el resultado al loop para enviarlo de vuelta por el socket.

![](./../Semana%202/Imagines/Diferencias%20Sockets%20con%20hilos%20y%20asincronismo.png)

***Dato curioso: Si no cierras correctamente el socket con ``.close()``, el File Descriptor se queda "abierto" en la tabla del proceso, lo que eventualmente causa el error ``OSError: [Errno 24] Too many open files``.***`

### 4. ¿Como sucede el bloqueo del hilo?

La línea de tiempo del bloqueo

#### 4.1. El Estado de Espera (Bloqueo en accept):

- Tu hilo principal está ejecutando ``conn, addr = server_socket.accept()``. Aquí el hilo está bloqueado. No está consumiendo CPU, simplemente está "dormido" esperando que el SO le avise que alguien golpeó la puerta (el puerto).

#### 4.2. La Asignación del FD:

- En cuanto un cliente se conecta, el SO crea el FD nuevo y el hilo principal se despierta. Inmediatamente, creas un hilo secundario y le pasas ese FD.

#### 4.3. El Bloqueo en la Lectura (recv):

- Aquí es donde ocurre el bloqueo que mencionas. El hilo secundario hace ``data = conn.recv(1024)``.

    - Si el cliente no ha enviado nada aún: El hilo se detiene ahí mismo. No puede avanzar a la siguiente línea de código.

    - ¿Qué pasa con el FD? El FD sigue ocupado y asignado a ese hilo. El SO sabe que ese hilo está "interesado" en lo que pase en ese número de archivo.

#### 4.4. El Procesamiento y Cierre:

Una vez que llegan los datos, el hilo se despierta, trabaja y finalmente ejecuta ``conn.close()``.

- **Liberación:** En ese instante, el SO borra la entrada en la tabla de File Descriptors y el número (ej. el FD 5) queda disponible para ser usado por otra conexión nueva.

### 5. ¿Cómo lo soluciona la asincronía?

Imagina un restaurante (el servidor).

- **Con Hilos** (``Threading``): Cada mesa (FD) tiene un camarero (Hilo) asignado. Si los clientes de la mesa 5 están leyendo el menú y no piden nada, el camarero se queda ahí parado mirándolos, bloqueado, sin hacer nada más. No puede atender a nadie más hasta que esa mesa se vaya o pida.

- **Con Asincronía** (``asyncio``): Hay un solo camarero para todo el restaurante. El camarero va a la mesa 5, les da el menú y les dice: "Hagan ruido cuando estén listos". El camarero se retira y atiende otras 10 mesas. El "hilo" nunca se queda parado mirando a una mesa vacía.

### 6. En resumen:

- **En Hilos**: El hilo se libera solo cuando termina su función (normalmente después del ``close()``), pero mientras espera datos ``(recv)``, el hilo está desperdiciado (bloqueado).

- **En Asincronía**: El "hilo" (Event Loop) nunca se bloquea. Si un FD no tiene datos, el loop salta al siguiente FD que sí tenga algo que decir.

El ``File Descriptor`` siempre se libera con el ``close()``, pero la diferencia es qué hace tu programa mientras ese FD está abierto y en silencio.