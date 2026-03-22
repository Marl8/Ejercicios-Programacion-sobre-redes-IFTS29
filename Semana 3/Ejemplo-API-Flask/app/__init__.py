from flask import Flask
from app.db import close_db, init_db
from app.routes.user_route import user_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(user_bp)
    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()

    return app