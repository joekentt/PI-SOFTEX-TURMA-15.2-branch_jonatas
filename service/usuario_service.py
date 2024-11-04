from repository.usuario_repository import UsuarioRepository
from entity.usuario import Usuario

class UsuarioService:

    @staticmethod
    def buscar_por_id(id):
        usuario = UsuarioRepository.get_by_id(id)
        if not usuario:
            raise ValueError("Usuário não encontrado")
        return usuario

    @staticmethod
    def buscar_todos():
        usuarios = UsuarioRepository.get_all()
        return [usuario.to_dict() for usuario in usuarios]
    
    @staticmethod
    def autenticar_usuario(email, senha):
        usuario = UsuarioRepository.get_by_email(email)
        if not usuario or usuario.senha_usuario != senha:
            raise ValueError("Credenciais incorretas")
        return usuario

    @staticmethod
    def cadastrar_usuario(usuario):
        usuario_existente = UsuarioRepository.get_by_email(usuario.email_usuario)
        if usuario_existente:
            raise ValueError("Email já cadastrado")
        if len(usuario.nome_usuario) < 3:
            raise ValueError("Nome do usuário deve ter pelo menos 3 caracteres")
        
        return UsuarioRepository.create(usuario)
