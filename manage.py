from app import create_app
from flask_script import Manager
from flask import request


app = create_app()


@app.route('/')
def home():
    print(request)
    return f'Esta app correo en: {request.host}'

if __name__ == "__main__":
    manager = Manager(app)
    manager.run()
