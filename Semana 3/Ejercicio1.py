# Sistemas distribuidos

'''
¿Por qué esto resuelve el problema?

1 - Disponibilidad: Si el Servidor_A muere, el archivo está a salvo en B y C.

2 - Escalabilidad: Si necesitas más espacio, creas un s4 = Nodo("Servidor_D") y lo conectas.

3 - Sincronización: El bucle for v in self.vecinos asegura que todos tengan lo mismo.
'''



class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.archivos = {} # Aquí se guardan los archivos
        self.vecinos = []  # Otros servidores conectados

    def guardar(self, nombre_archivo, contenido):
        # 1. Guarda en sí mismo
        self.archivos[nombre_archivo] = contenido
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