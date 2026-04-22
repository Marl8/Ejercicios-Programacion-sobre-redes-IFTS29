import asyncio

contador_clientes = 0

async def handle_async_client(reader, writer):
    global contador_clientes
    addr = writer.get_extra_info('peername')
    
    try:
        data = await reader.read(1024)
        mensaje = data.decode('utf-8')
        
        contador_clientes += 1
        print(f"[{contador_clientes}] Cliente dice: {mensaje} (desde {addr})")
        
        await asyncio.sleep(0.1) 
        writer.write(b"Hola desde el server")
        await writer.drain()
    finally:
        writer.close()
        await writer.wait_closed()

async def start_async_server():
    server = await asyncio.start_server(handle_async_client, '0.0.0.0', 5002)
    print("⚡ Servidor ASYNCIO corriendo en puerto 5002...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_async_server())