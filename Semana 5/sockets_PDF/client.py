import socket

# Crear un socket TCP (SOCK_STREAM) :

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección IP y puerto:

client_socket.connect(('localhost', 8080))

# Recibir un mensaje del servidor

message = client_socket.recv(1024)
print(f"Recibido del servidor: {message.decode()}")

# Enviar datos al servidor

client_socket.send(b"Hola, servidor! Soy el cliente.")

# Cerrar la conexión

client_socket.close()