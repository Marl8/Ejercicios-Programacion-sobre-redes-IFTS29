import socket
import threading
import time

def handle_client(conn, addr):
    try:
        data = conn.recv(1024)
        # Simulamos una pequeña latencia de procesamiento
        time.sleep(0.1) 
        conn.sendall(b"Respuesta desde Threading Server")
    finally:
        conn.close()

def start_threading_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 5001))
    server.listen(100)
    print(" Servidor THREADING corriendo en puerto 5001...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_threading_server()