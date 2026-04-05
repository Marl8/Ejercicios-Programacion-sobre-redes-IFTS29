## ¿Qué es una Primitiva?

En el contexto de la biblioteca threading de Python, una primitiva (o primitiva de sincronización) es un objeto básico de bajo nivel diseñado para gestionar la comunicación y la interacción entre múltiples hilos.

Piénsalas como las "reglas de tránsito" del código. Sin ellas, si dos hilos intentan modificar el mismo dato al mismo tiempo, podrías terminar con un caos llamado condición de carrera (race condition).

### ¿Por qué se les llama "primitivas"?

Se les llama así porque son los bloques de construcción fundamentales. No puedes dividirlas en operaciones más pequeñas que sean seguras para hilos; son atómicas. Sobre estas piezas simples, puedes construir arquitecturas de software mucho más complejas y seguras.


Las principales primitivas que encontrarás:

### 1. Lock (Candado)

Es la primitiva más simple. Solo tiene dos estados: bloqueado o desbloqueado. Si un hilo adquiere el candado, cualquier otro hilo que intente obtenerlo tendrá que esperar hasta que el primero lo suelte.

- Uso principal: Proteger el acceso a una variable o recurso compartido.

### 2. RLock (Reentrant Lock)

Es una variante del Lock que permite que el mismo hilo adquiera el candado varias veces sin bloquearse a sí mismo. Es útil en funciones recursivas donde un hilo necesita re-entrar en una sección protegida que ya posee.

### 3. Semaphore (Semáforo)

A diferencia del Lock, un semáforo tiene un contador interno. Permite que un número específico de hilos accedan a un recurso simultáneamente.

- Si el contador llega a cero, los hilos siguientes deben esperar.

- Uso principal: Limitar el acceso a recursos con capacidad finita (como conexiones a una base de datos).

### 4. Event (Evento)

Funciona como una señal de comunicación simple. Un hilo espera a que ocurra algo (wait) y otro hilo activa la señal (set).

- Uso principal: Notificar a otros hilos que una tarea específica ha terminado o que pueden comenzar a trabajar.

### 5. Condition (Condición)

Es una primitiva más avanzada que combina un Lock con la capacidad de esperar a que ocurra un cambio específico en el estado del programa.

- Permite que un hilo se "ponga a dormir" hasta que otro hilo lo despierte porque algo importante cambió.

- Uso principal: El clásico problema del Productor-Consumidor.

