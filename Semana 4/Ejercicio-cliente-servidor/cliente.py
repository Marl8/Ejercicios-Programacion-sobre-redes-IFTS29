import socket

# 1. Configuración de conexión
try:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(('localhost', 5000))

    # 2. Entrada por consola
    pais = input("Escribe el nombre de un país para saber su capital: ")
    
    # 3. Envío y Recepción
    cliente.send(pais.encode())
    respuesta = cliente.recv(1024).decode()

    print(f"--- Respuesta del servidor: {respuesta} ---")

except ConnectionRefusedError:
    print("Error: El servidor no está encendido. Ejecuta primero servidor.py")
finally:
    cliente.close()