from flask import Flask
from app.apis import api_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    return app

app = create_app()