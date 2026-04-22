import socket
import threading
import time

# Contador para numerar los mensajes
contador_clientes = 0
print_lock = threading.Lock()

def handle_client(conn, addr):
    global contador_clientes
    try:
        data = conn.recv(1024).decode('utf-8')
        
        with print_lock:
            contador_clientes += 1
            print(f"[{contador_clientes}] Cliente dice: {data} (desde {addr})")
        
        time.sleep(0.1) 
        conn.sendall(b"Hola desde el server")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def start_threading_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 5001))
    server.listen(500) # Aumentamos el backlog para 50k
    print("Servidor THREADING corriendo en puerto 5001...")
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    start_threading_server()