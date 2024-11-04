"""
##  Versão 1.1 do suaGarantia
##  Para o correto funcionamento do sistema é preciso seguir os passos abaixo:
##  Instale "pip install flet"
##  Instale "pip install sqlalchemy"
##  Atenção! O projeto está usando a versão do SQLite. Inicialmente desenvolvido nesse modelo para testes.
##  Nas próximas versões possívelmente estará com banco POSTGRES e framework FLASK
"""
# from flask import Flask
# from config import Config
# from db import db
# import init_db
# from controller.usuario_controller import usuario_bp #controller.usuario_controller import usuario_bp

# app = Flask(__name__)
# app.config.from_object(Config)

# db.init_app(app)
# init_db.init_db(app)

# # Registrar o blueprint para as rotas de usuário
# app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')

# if __name__ == "__main__":
#     app.run(debug=True)

# app.py

from flask import Flask
from config import Config
from db import db
import init_db
from controller.usuario_controller import usuario_bp
import flet as ft
from frontend import main as flet_main  # Função Flet principal do frontend

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
init_db.init_db(app)

# Registrar o blueprint para as rotas de usuário
app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')

# Função para iniciar o frontend
def iniciar_frontend():
    ft.app(target=flet_main)

if __name__ == "__main__":
    from threading import Thread
    # Iniciar o servidor Flask em uma thread
    flask_thread = Thread(target=lambda: app.run(debug=True))
    flask_thread.start()

    # Iniciar o frontend Flet em outra thread
    iniciar_frontend()
