import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("secretkey"),
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        PROPAGATE_EXCEPTIONS=True,
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    from app import auth
    app.register_blueprint(auth.bp)

    from app import main
    app.register_blueprint(main.bp)

    return app


db.create_all(app=create_app())