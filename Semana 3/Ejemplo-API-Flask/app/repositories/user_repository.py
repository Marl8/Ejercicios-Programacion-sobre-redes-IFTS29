from app.db import get_db
from app.models.user import User

def create_user(name, email):
    db = get_db()
    cursor = db.execute(
        'INSERT INTO users (name, email) VALUES (?, ?)',
        (name, email)
    )
    db.commit()
    return cursor.lastrowid

def get_all_users():
    db = get_db()
    rows = db.execute('SELECT * FROM users').fetchall()
    return [User(r["id"], r["name"], r["email"]) for r in rows]

def get_user_by_id(user_id):
    db = get_db()
    row = db.execute(
        'SELECT * FROM users WHERE id = ?', (user_id,)
    ).fetchone()

    if row:
        return User(row["id"], row["name"], row["email"])
    return None

def update_user(user_id, name, email):
    db = get_db()
    db.execute(
        'UPDATE users SET name = ?, email = ? WHERE id = ?',
        (name, email, user_id)
    )
    db.commit()

def delete_user(user_id):
    db = get_db()
    db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()