import socket

# Configuración del servidor (misma que en server.py)
HOST = "localhost"
PORT = 1234

# Crear el socket TCP

# El WITH es mejor que el try/chatch ya que provoca el cierre automático cuando termina la ejecución
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    # Conectar al servidor
    s.connect((HOST, PORT))
    print(f"Conectado al servidor {HOST}:{PORT}")

    # Enviar una pregunta
    pregunta = input("Escribe tu pregunta: ")
    s.sendall(pregunta.encode("utf-8")) # Sendall es una solución de más alto nivel que el send

    # Recibir la respuesta
    respuesta = s.recv(1024).decode("utf-8")
    print(f"Respuesta del servidor: {respuesta}")