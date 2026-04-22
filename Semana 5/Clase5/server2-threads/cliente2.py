import socket
import time
import threading
import statistics

# --- CONFIGURACIÓN DEL TEST ---
PORT = 5002  # 5001 para Threading, 5002 para AsyncIO
CONCURRENT_CLIENTS = 30000
# ------------------------------

results = []

def single_client_test(id):
    try:
        start_time = time.perf_counter()
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', PORT))
        sock.sendall(b"Hola")
        _ = sock.recv(1024)
        sock.close()
        
        end_time = time.perf_counter()
        results.append((end_time - start_time) * 1000) # Guardar en ms
    except Exception as e:
        print(f"Error en cliente {id}: {e}")

def run_benchmark():
    print(f"--- Iniciando Test en Puerto {PORT} con {CONCURRENT_CLIENTS} clientes ---")
    threads = []
    
    start_bench = time.perf_counter()
    
    for i in range(CONCURRENT_CLIENTS):
        t = threading.Thread(target=single_client_test, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    end_bench = time.perf_counter()
    
    # Análisis de resultados
    total_time_ms = (end_bench - start_bench) * 1000
    avg_latency = statistics.mean(results)
    
    print("\n" + " RESULTADOS ".center(40, "="))
    print(f"Tiempo total del batch: {total_time_ms:.2f} ms")
    print(f"Latencia promedio:      {avg_latency:.2f} ms")
    print(f"P95 (Peor 5% latencia): {statistics.quantiles(results, n=20)[18]:.2f} ms")
    print("=" * 40)

if __name__ == "__main__":
    run_benchmark()