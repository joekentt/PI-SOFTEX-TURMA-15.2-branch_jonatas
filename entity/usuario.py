from db import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(200), nullable=False)
    email_usuario = db.Column(db.String(100), unique=True, nullable=False)
    senha_usuario = db.Column(db.String(200), nullable=False)
    data_nascimento_usuario = db.Column(db.String(10))
    telefone_usuario = db.Column(db.String(15))

    def to_dict(self):
        return {
            "id": self.id,
            "nome_usuario": self.nome_usuario,
            "email_usuario": self.email_usuario,
            "data_nascimento_usuario": self.data_nascimento_usuario,
            "telefone_usuario": self.telefone_usuario
        }
