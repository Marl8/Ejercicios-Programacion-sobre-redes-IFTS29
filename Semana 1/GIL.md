## GIL - Global Interpreter Lock 

El término GIL corresponde a Global Interpreter Lock (Cerrojo Global del Intérprete). Es, esencialmente, un mecanismo de seguridad que utiliza el intérprete estándar de Python (CPython) para evitar que múltiples hilos ejecuten código de Python al mismo tiempo.

### 1. ¿Cómo funciona exactamente?

Imagina que el intérprete de Python es un micrófono único en una habitación llena de gente (hilos). Aunque haya 10 personas queriendo hablar, solo la que tiene el micrófono puede hacerlo.

- El cerrojo: Solo un hilo puede "poseer" el GIL a la vez.

- La ejecución: El hilo que tiene el GIL ejecuta sus instrucciones.

- El cambio: Después de un breve periodo de tiempo (o cuando el hilo se bloquea por una operación de entrada/salida), el hilo suelta el GIL y otro lo toma.

### 2. ¿Por qué existe el GIL?

Python utiliza un sistema llamado conteo de referencias para la gestión de memoria. Cada objeto tiene un contador que dice cuántas variables lo están usando.
Para evitar que dos hilos aumenten o disminuyan el contador de un objeto al mismo tiempo (lo que causaría errores fatales o fugas de memoria), el GIL actúa como un guardia de seguridad.

***La regla de oro: Aunque tengas un procesador con 16 núcleos, el GIL solo permitirá que Python ejecute instrucciones en un único núcleo a la vez por cada proceso.***

- Si dos hilos intentaran aumentar o disminuir ese contador al mismo tiempo, el valor podría corromperse.

- Esto provocaría fugas de memoria o, peor aún, que Python intente borrar un objeto que todavía está en uso.

El GIL fue la solución más sencilla y eficiente para hacer que Python fuera seguro frente a hilos (thread-safe) sin sacrificar el rendimiento en tareas que usan un solo núcleo.

