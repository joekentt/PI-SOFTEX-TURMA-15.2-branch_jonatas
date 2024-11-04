import flet as ft
import requests

BASE_URL = "http://127.0.0.1:5000/api/usuarios"

def tela_login(page):
    page.clean()
    email_usuario = ft.TextField(label="E-mail do Usuário", text_align=ft.TextAlign.LEFT)
    senha_usuario = ft.TextField(label="Senha", text_align=ft.TextAlign.LEFT, password=True, can_reveal_password=True)
    
    def autenticar_usuario(e):
        response = requests.post(f"{BASE_URL}/login", json={
            "email": email_usuario.value,
            "senha": senha_usuario.value
        })
        if response.status_code == 200:
            page.snack_bar = ft.SnackBar(ft.Text("Login bem-sucedido!"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Credenciais incorretas!"), open=True)
        page.update()

    botao_login = ft.ElevatedButton("Login", on_click=autenticar_usuario)
    botao_cadastrar = ft.TextButton("Cadastrar", on_click=lambda e: tela_cadastro(page))
    page.add(email_usuario, senha_usuario, botao_login, botao_cadastrar)

def tela_cadastro(page):
    page.clean()
    nome_usuario = ft.TextField(label="Nome do Usuário")
    email_usuario = ft.TextField(label="E-mail")
    senha_usuario = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    data_nascimento_usuario = ft.TextField(label="Data de Nascimento", text_align=ft.TextAlign.LEFT)
    telefone_usuario = ft.TextField(label="Telefone", text_align=ft.TextAlign.LEFT)

    def cadastrar_usuario(e):
        response = requests.post(f"{BASE_URL}/cadastro", json={
            "nome_usuario": nome_usuario.value,
            "email_usuario": email_usuario.value,
            "senha_usuario": senha_usuario.value,
            "data_nascimento_usuario": data_nascimento_usuario.value,
            "telefone_usuario": telefone_usuario.value

        })
        if response.status_code == 201:
            page.snack_bar = ft.SnackBar(ft.Text("Cadastro bem-sucedido!"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Erro no cadastro!"), open=True)
        page.update()

    botao_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar_usuario)
    page.add(nome_usuario, email_usuario, senha_usuario, data_nascimento_usuario, telefone_usuario, botao_cadastrar)


def main(page: ft.Page):
    page.title = "App Login/Cadastro"
    page.clean()

    # Escolhe qual tela inicializar (ex: tela de login)
    tela_login(page)

if __name__ == "__main__":
    ft.app(target=main)  # Inicializa a aplicação Flet separadamente