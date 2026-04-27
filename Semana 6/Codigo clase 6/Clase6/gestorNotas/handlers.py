from aiohttp import web
import db

async def listar_notas_handler(request):
    try:
        notas = db.obtener_notas()
        notas_formateadas = [{"id": nota[0], "contenido": nota[1]} for nota in notas]
        return web.json_response({"notas": notas_formateadas})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

async def agregar_nota_handler(request):
    try:
        data = await request.json()
        contenido = data.get("contenido")
        if not contenido:
            return web.json_response({"error": "Contenido requerido"}, status=400)
        db.agregar_nota(contenido)
        return web.json_response({"mensaje": "Nota agregada"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

async def eliminar_nota_handler(request):
    try:
        nota_id = int(request.match_info['id'])
        db.eliminar_nota(nota_id)
        return web.json_response({"mensaje": "Nota eliminada"})
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)
    
async def ping(request):
    return web.json_response({"Code": 200,
            "Message": "APP working!"})
