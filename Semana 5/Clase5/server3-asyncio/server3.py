import asyncio

async def handle_async_client(reader, writer):
    data = await reader.read(1024)
    # Simulamos latencia sin bloquear el hilo principal
    await asyncio.sleep(0.1) 
    writer.write(b"Respuesta desde AsyncIO Server")
    await writer.drain()
    writer.close()
    await writer.wait_closed()

async def start_async_server():
    server = await asyncio.start_server(handle_async_client, '0.0.0.0', 5002)
    print("⚡ Servidor ASYNCIO corriendo en puerto 5002...")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_async_server())