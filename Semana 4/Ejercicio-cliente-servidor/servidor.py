import socket

# Base de datos simple
datos = {
    "Francia": "París",
    "España": "Madrid",
    "Mexico": "Ciudad de México",
    "Argentina": "Buenos Aires",
    "Colombia": "Bogotá"
}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5000))
server.listen(1)

print("Servidor de capitales listo...")

while True:
    conn, addr = server.accept()
    # Recibimos el país, lo limpiamos y pasamos a minúsculas
    pais = conn.recv(1024).decode().strip().capitalize()
    
    # Buscamos en el diccionario
    respuesta = datos.get(pais, "No tengo ese país en mi base de datos.")
    
    conn.send(respuesta.encode())
    conn.close()