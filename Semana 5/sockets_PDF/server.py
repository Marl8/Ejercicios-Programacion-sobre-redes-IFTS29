import socket

# Crear un socket TCP (SOCK_STREAM) :

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket a una dirección IP y puerto:

server_socket.bind(('localhost', 8080))

# Escuchar por conexiones entrantes

server_socket.listen(1)
print("Esperando conexión de un cliente...")

# Aceptar la conexión

client_socket, client_address = server_socket.accept()
print(f"Conexión establecida con {client_address}")

# Enviar un mensaje al cliente

client_socket.send(b"Hola, cliente! Bienvenido al servidor.")

# Recibir datos del cliente

data = client_socket.recv(1024)
print(f"Recibido del cliente: {data.decode()}")

# Cerrar la conexión

client_socket.close()
server_socket.close()