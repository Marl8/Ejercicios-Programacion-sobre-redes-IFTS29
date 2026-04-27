import sqlite3

DB_FILE = "notas.db"

def connect_db():
    return sqlite3.connect(DB_FILE)

def init_db():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT NOT NULL
            )
        ''')
        conn.commit()

def agregar_nota(contenido):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notas (contenido) VALUES (?)", (contenido,))
        conn.commit()

def obtener_notas():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, contenido FROM notas")
        return cursor.fetchall()

def eliminar_nota(nota_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notas WHERE id = ?", (nota_id,))
        conn.commit()
