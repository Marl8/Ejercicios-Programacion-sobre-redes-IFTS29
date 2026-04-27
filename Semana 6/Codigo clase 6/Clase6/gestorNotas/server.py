from aiohttp import web
import db
import handlers

def crear_app():
    app = web.Application()
    app.router.add_get('/notas', handlers.listar_notas_handler)
    app.router.add_post('/notas', handlers.agregar_nota_handler)
    app.router.add_delete('/notas/{id}', handlers.eliminar_nota_handler)
    app.router.add_get('/ping', handlers.ping)
    return app

if __name__ == "__main__":
    db.init_db()
    app = crear_app()
    web.run_app(app, port=8080)
