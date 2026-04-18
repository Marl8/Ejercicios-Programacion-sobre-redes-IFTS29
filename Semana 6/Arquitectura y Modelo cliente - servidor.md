## Diferencia entre la Arquitectura Cliente - Servidor y el Modelo Cliente - Servidor

### 1. El Modelo Cliente-Servidor (El "Qué")

El modelo es el diseño lógico o el esquema conceptual. Define una relación donde las tareas se reparten entre los proveedores de un recurso o servicio (servidores) y los demandantes (clientes).

- **Es una abstracción:** No te dice qué cables usar ni qué procesador comprar, sino cómo fluye la información.

- **Roles definidos:** El cliente siempre inicia la comunicación (petición) y el servidor espera a que alguien le hable para responder.

- **Protocolo:** Se centra en las reglas de interacción (como el protocolo HTTP para navegar por la web).

### 2. La Arquitectura Cliente-Servidor (El "Cómo")

La arquitectura es la plasmación física y técnica de ese modelo. Es la estructura real de hardware y software que permite que el modelo funcione.

- **Es la implementación:** Aquí hablamos de redes, bases de datos, servidores físicos en la nube (como AWS) y dispositivos finales.

- **Niveles (Tiers):** La arquitectura define si el sistema es de 2 capas (cliente y base de datos directa), 3 capas (cliente, servidor de aplicaciones y base de datos) o N-capas.

- **Infraestructura:** Incluye la topología de red, el balanceo de carga y la seguridad.

![Arquitecuta y Modelo](../Semana%202/Imagines/Arquitectura%20y%20Modelo.png)