import pytest
from datetime import datetime
from app import create_app
from app.schema import User, Profile
from app.utlis import create_token
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def app():
    config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///../instance/test-api.db"
    }
    app = create_app(config)
    return app

@pytest.fixture
def db(app):
    db = app.db
    return db

@pytest.fixture
def client(app, db):
    db.create_all(app=app)
    yield app.test_client()
    db.drop_all(app=app)

@pytest.fixture
def client_user(app, db):
    # db = app.db
    hashed_pass = generate_password_hash("123456") 
    user = User(email="test@email.com", password=hashed_pass)
    with app.app_context():
        db.create_all()
        # db.create_all(app=app)
        db.session.add(user)
        db.session.commit()
        yield app.test_client()
        db.drop_all(app=app)

@pytest.fixture
def token():
    return create_token({"id": "1"})

@pytest.fixture
def client_profile(app, db):
    profile = {
        "name": "Test User",
        "gender": "Male",
        "dob": datetime.fromisoformat("2000-04-06"),
        "user_id": 1
    }
    pro = Profile(**profile)

    hashed_pass = generate_password_hash("123456") 
    user = User(email="test@email.com", password=hashed_pass)
    with app.app_context():
        db.create_all()
        # db.create_all(app=app)
        db.session.add(user)
        db.session.add(pro)
        db.session.commit()
        yield app.test_client()
        db.drop_all(app=app)

