## File Description

Para entender qué es un Descriptor de Archivo (File Descriptor o FD), imagina que el sistema operativo es un gran bibliotecario. En lugar de darte el libro físico (el archivo) cada vez que quieres leer una página, el bibliotecario te da un ticket con un número (por ejemplo, el número 5).

Cuando quieras leer o escribir en ese libro, solo le dices al bibliotecario: "Oye, quiero hacer algo con el ticket número 5". El bibliotecario sabe exactamente a qué libro se refiere ese número.

### 1. ¿Qué es exactamente un Descriptor de Archivo?

Es simplemente un número entero positivo (0, 1, 2, 3...). Es un identificador que usa un proceso (un programa en ejecución) para interactuar con cualquier recurso de entrada/salida (I/O). En Linux/Unix, casi todo se trata como un archivo: documentos, carpetas, teclados, monitores e incluso conexiones de red (sockets).

### 2. Los tres descriptores estándar

Cada vez que abres una terminal o inicias un programa, el sistema operativo le asigna automáticamente tres números:

- ``0`` (Standard Input - ``stdin``): Por donde el programa recibe datos (usualmente el teclado).

- ``1`` (Standard Output - ``stdout``): Por donde el programa envía los resultados (usualmente la pantalla).

- ``2`` (Standard Error - ``stderr``): Por donde el programa envía mensajes de error (también la pantalla, pero por un canal separado).

### 3. ¿Cómo funciona por dentro? (La estructura de 3 capas)

El sistema utiliza tres tablas para que esto funcione:

- ***Tabla de Descriptores del Proceso:*** Cada programa tiene su propia lista de números. El número 3 en tu navegador puede apuntar a algo distinto que el número 3 en tu editor de texto.

- ***Tabla de Archivos Abiertos (Global):*** El sistema operativo mantiene una lista de todos los archivos que están siendo usados en todo el sistema. Aquí se guarda en qué parte del archivo vas (el "offset" o puntero de lectura/escritura).

- ***Tabla de Inodos (V-nodes en AIX):*** Es la capa que conoce la realidad física del archivo en el disco duro (su tamaño, quién es el dueño y dónde están guardados sus datos reales).

### 4. Conceptos claves

- ***Creación de descriptores:*** Obtienes nuevos números usando funciones como ``open()`` (abrir un archivo), ``creat()`` (crearlo) o ``pipe()`` (crear un túnel de datos). Estos métodos son funciones de la Librería Estándar de ``C``, pero con un matiz importante: son llamadas al sistema (system calls).

    #### El puente entre C y el Kernel

    Cuando tú usas ``open()`` en ``C``, no estás simplemente ejecutando una función que vive dentro de tu programa. Estás tocando la puerta del Kernel (el núcleo del sistema operativo) para decirle: "Oye, necesito acceso a este recurso físico".

    - **C (Nivel de usuario)**: Tú escribes ``int fd = open("archivo.txt", O_RDONLY);``.

    - **Kernel (Nivel de sistema)**: El sistema operativo recibe la petición, verifica si tienes permisos, busca el archivo en el disco, crea la entrada en la Tabla de Archivos Abiertos y te devuelve el número del descriptor.

- ***Herencia (Fork):*** Cuando un programa crea un "hijo" (un proceso derivado), el hijo hereda todos los descriptores del padre. Por eso, si el padre estaba escribiendo en un archivo, el hijo puede seguir haciéndolo en el mismo lugar.

- ***Redirección:*** Cuando usas comandos como comando > archivo.txt, lo que haces es decirle al sistema: "Cierra el descriptor 1 (pantalla) y reemplázalo por el descriptor de este archivo de texto".

- ***Límites:*** El artículo de IBM menciona que no son infinitos. Existe un límite (controlado por ulimit o OPEN_MAX) sobre cuántos "tickets" o descriptores puede tener abiertos un programa a la vez.

### 5. Resumen para recordar:

- **Descriptor:** El número que tú (el programa) usas.

- **Tabla de archivos:** Donde el sistema anota en qué línea del archivo te quedaste.

- **Inodo:** La información técnica del archivo en el disco duro.

Si un programa no cierra sus descriptores cuando termina de usarlos, ocurre lo que se llama una "fuga de descriptores", y eventualmente el programa no podrá abrir más archivos porque se quedó sin números disponibles.