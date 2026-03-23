## API con Flask y SQLite

### Estructura Principal

````text

mi_api/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── db.py
│
│   ├── models/
│   │   └── user.py
│
│   ├── repositories/
│   │   └── user_repository.py
│
│   ├── services/
│   │   └── user_service.py
│
│   ├── routes/
│   │   └── user_routes.py
│
├── run.py
└── database.db

````

### Pasos

**1.** 🧠 Punto de entrada → ``run.py``

```Python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

🔍 Qué pasa acá:
- Importás la función ``create_app()``
- Creás la app de Flask
- Ejecutás el servidor

👉 Este archivo es solo el arranque, no tiene lógica.

**2.** 🏗️ Factory → __init__.py

````Python
from flask import Flask
from app.db import close_db, init_db
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp)

    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()

    return app
````

🔹 ``app = Flask(__name__)``

Crea la aplicación web.

🔹 ``register_blueprint``

````python
app.register_blueprint(user_bp)
````

👉 Le dice a Flask:

"Usá las rutas que están en otro archivo"

Esto evita tener todo en un solo archivo gigante.

🔹 ``teardown_appcontext``

````python
app.teardown_appcontext(close_db)
````

👉 Esto es MUY importante:

Se ejecuta al final de cada request
Cierra la conexión a la DB

✔ Evita fugas de memoria
✔ Evita conexiones abiertas

🔹 ``app.app_context()``

````python
with app.app_context():
    init_db()
````

👉 Crea un contexto temporal para poder usar cosas internas de Flask.

Se usa para:

- inicializar la base de datos

**3.** 🗄️ Base de datos → db.py

````python
import sqlite3
from flask import g
from app.config import Config
````

🧠 ¿Qué es ``g``?

Flask tiene un objeto especial llamado ``g``.

👉 Es un espacio temporal por request

- vive solo durante una petición
- se destruye al terminar

🔌 ``get_db()``

````python
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(Config.DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db
````

🔍 Qué hace:
- Si no hay conexión → la crea
- La guarda en g
- La reutiliza durante el request

🔹 row_factory

````python
g.db.row_factory = sqlite3.Row
````

👉 Permite acceder así:

user["name"]

🔚 ``close_db()``

````python
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db
        .close()
````

👉 Cierra la conexión al final del request.

🏗️ ``init_db()``

````python
def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    db.commit()
````
👉 Crea la tabla si no existe.