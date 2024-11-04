#from flask import Flask
#from config import Config


from db import db
import os
#import init_db
#from controller.usuario_controller import usuario_bp


# Verifica se o banco de dados já foi criado
def init_db(app):
    db_file = app.config['SQLALCHEMY_DATABASE_URI'].replace('postgresql://', '')

    # Se o arquivo do banco de dados não existir, ele será criado
    if not os.path.exists(db_file):
        print("Creating database...")
        with app.app_context():
            db.create_all()
        print("Database created!")
    else:
        print("Database already exists!")

if __name__ == '__main__':
    init_db()

"""
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
init_db.init_db(app)

# Registrar o blueprint para as rotas de usuário
app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')

if __name__ == "__main__":
    app.run(debug=True)
"""