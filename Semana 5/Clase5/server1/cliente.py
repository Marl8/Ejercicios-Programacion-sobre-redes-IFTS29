import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 12345)) # 1 - 65535 -> puertos reservados


pregunta = "¿Cuál es la capital de Rusia?"
print(f"Enviando pregunta: {pregunta}")
cliente.send(pregunta.encode())

respuesta = cliente.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")

#cliente.close()
