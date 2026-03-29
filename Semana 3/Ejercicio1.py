# Sistemas distribuidos

'''
Diseño de un Sistema Distribuido para Gestión de Archivos

Imagina que estás diseñando un sistema distribuido para gestionar archivos 

en una red de computadoras. Este sistema debe permitir que los usuarios suban, 

descarguen y compartan archivos entre varios servidores. Los archivos deben ser accesibles desde cualquier servidor y, si un servidor falla, los archivos deben seguir disponibles en otros servidores. 



Requerimientos: 


- Los archivos deben estar distribuidos entre varios servidores. 

- Los usuarios pueden subir y descargar archivos de cualquier servidor. 

- Los servidores deben poder comunicarse entre sí para mantener los archivos 

    sincronizados. 

- El sistema debe ser escalable, permitiendo agregar más servidores si es necesario. 

- Si un servidor falla, los archivos deben seguir disponibles. 

- Diseña un diagrama que muestre la arquitectura de este sistema distribuido,

    incluyendo: 

    1. Usuarios que suben y descargan archivos. 

    2. Servidores que almacenan los archivos distribuidos. 

    3. Comunicación entre servidores para mantener los archivos sincronizados. 

    4. Almacenamiento de archivos distribuido entre los servidores. 

    5. Manejo de fallos para asegurar la disponibilidad de los archivos.
'''



class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = {} # Diccionario donde se guardan los archivos
        self.vecinos = []  # Array de Otros servidores conectados

    def guardar(self, nombre_archivo, contenido):
        # 1. Guarda en sí mismo
        self.archivos[nombre_archivo] = contenido
        print()
        print(f"[{self.nombre}] Archivo '{nombre_archivo}' guardado.")
        
        # 2. Copia automática a los vecinos (Sincronización)
        for v in self.vecinos:
            v.archivos[nombre_archivo] = contenido
            print(f" -> Copia enviada a {v.nombre}")

    def leer(self, nombre_archivo):
        # Si no lo tiene, es porque este servidor "falló" o perdió el dato
        return self.archivos.get(nombre_archivo, "Error: Archivo no encontrado.")

# --- PRUEBA DEL SISTEMA ---

# Creamos 3 servidores
s1 = Nodo("Servidor_A")
s2 = Nodo("Servidor_B")
s3 = Nodo("Servidor_C")

# Los conectamos entre sí
s1.vecinos = [s2, s3]

# Usuario sube un archivo al Servidor A
s1.guardar("foto.jpg", "Contenido binario de la imagen")

# SIMULAMOS FALLO: El Servidor A se rompe y vacía su memoria
s1.archivos = {} 
print("\n--- El Servidor A ha fallado y perdió sus datos ---")

# El usuario intenta leer desde el Servidor B (o C)
# ¡El archivo sigue ahí porque se sincronizó antes!
print(f"Consultando al Servidor B: {s2.leer('foto.jpg')}")


'''
¿Por qué esto resuelve el problema?

1 - Disponibilidad: Si el Servidor_A muere, el archivo está a salvo en B y C.

2 - Escalabilidad: Si necesitas más espacio, creas un s4 = Nodo("Servidor_D") y lo conectas.

3 - Sincronización: El bucle for v in self.vecinos asegura que todos tengan lo mismo.
'''