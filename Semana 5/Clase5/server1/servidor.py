import socket

# Diccionario de preguntas y respuestas
base_de_conocimiento = {
    "¿Cuál es la capital de Francia?": "París",
    "¿Cuál es la capital de Argentina?": "Buenos Aires",
    "¿Cuál es la capital de Italia?": "Roma"
}

# Crear socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("localhost", 12345))
servidor.listen(1)

print("Servidor escuchando en puerto 12345...")

while True:
    conexion, direccion = servidor.accept()
    print(f"Conexión desde {direccion}")

    pregunta = conexion.recv(1024).decode()
    print(f"Cliente pregunta: {pregunta}")

    respuesta = base_de_conocimiento.get(pregunta, "Lo siento, no conozco la respuesta.")
    conexion.send(respuesta.encode())

    conexion.close()
