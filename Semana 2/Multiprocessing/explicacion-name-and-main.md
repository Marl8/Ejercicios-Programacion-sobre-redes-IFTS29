## Que es el __name__ == "__main__" En Python?


Esta es una de las dudas más comunes en Python porque tiene que ver con cómo el lenguaje "lee" tus archivos y cómo el sistema operativo gestiona la memoria.

Para entenderlo, primero debemos saber qué hace Python cuando abres un script.

### 1. El significado de ``__name__``

Cada vez que Python ejecuta un archivo, le asigna una variable especial llamada ``__name__``.

- Si tú ejecutas el archivo directamente (ej. python mi_script.py), Python le asigna el valor ``"__main__"``.

- Si el archivo es importado por otro (ej. import mi_script), el valor de ``__name__`` será el nombre del archivo ("mi_script").

La línea ``if __name__ == "__main__"``: es un interruptor que dice: "Solo ejecuta lo que sigue si este archivo es el protagonista, no si alguien lo está importando".

### 2. El problema específico con multiprocessing

Aquí es donde se pone interesante. Como mencionamos, los hilos (threads) comparten la misma memoria, pero los procesos son independientes.

Dependiendo de tu sistema operativo, la creación de un proceso funciona distinto:

- ***En Linux/Mac:*** Se usa un método llamado **fork**. El sistema hace una "fotocopia" exacta del estado actual del programa. El nuevo proceso ya sabe qué hacer y no necesita volver a leer el archivo desde el principio.

- ***En Windows:*** Se usa un método llamado **spawn**. Windows no puede hacer una fotocopia del proceso actual. En su lugar, arranca una instancia nueva y vacía de Python y le dice: "Oye, lee este archivo .py de nuevo para que sepas qué funciones tienes disponibles".

### 3. La "Bomba de Procesos" (El bucle infinito)

Imagina que tienes este código SIN el ``if __name__ == "__main__":`` en Windows:

````Python
import multiprocessing

def tarea():
    print("Hola")

# ESTO VA A FALLAR
p1 = multiprocessing.Process(target=tarea)
p1.start()
````

Esto es lo que sucede paso a paso:

- **Proceso Principal**: Lee el archivo, llega a la línea p1.start() y le dice a Windows: "Crea un nuevo proceso".

- Proceso **Hijo 1**: Se inicia. Como es Windows, tiene que re-importar (leer) el archivo para conocer la función tarea.

- Al leer el archivo, el **Hijo 1** llega de nuevo a la línea p1.start().

- **Hijo 1** dice: "Oh, tengo que crear un nuevo proceso", y crea al **Hijo 2**.

- **Hijo 2** se inicia, lee el archivo, llega a ``p1.start()`` y crea al Hijo 3.

- **Resultado:** En milisegundos, tu computadora intenta abrir cientos de procesos de Python hasta que se congela o se agota la RAM.

### 4. La solución: El muro de contención

Al poner ``if __name__ == "__main__":``, creas una barrera:

- **Proceso Principal**: Su nombre es ``"__main__"``, así que entra al if y lanza el proceso hijo.

- Proceso Hijo: Al re-importar el archivo para prepararse, su nombre ya no es ``"__main__"`` (Python lo trata como un módulo importado).

- El Hijo llega al if, la condición es falsa, y se salta la orden de crear más procesos.

- El Hijo queda libre para ejecutar únicamente la función que le pediste (target=tarea).
