import flet as ft
import requests

BASE_URL = "http://127.0.0.1:5000/api/usuarios"

def tela_login(page):
    email_usuario = ft.TextField(label="E-mail do Usuário")
    senha_usuario = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    
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
    page.add(email_usuario, senha_usuario, botao_login)

def tela_cadastro(page):
    nome_usuario = ft.TextField(label="Nome do Usuário")
    email_usuario = ft.TextField(label="E-mail")
    senha_usuario = ft.TextField(label="Senha", password=True)
    
    def cadastrar_usuario(e):
        response = requests.post(f"{BASE_URL}/cadastro", json={
            "nome_usuario": nome_usuario.value,
            "email_usuario": email_usuario.value,
            "senha_usuario": senha_usuario.value
        })
        if response.status_code == 201:
            page.snack_bar = ft.SnackBar(ft.Text("Cadastro bem-sucedido!"), open=True)
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Erro no cadastro!"), open=True)
        page.update()

    botao_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar_usuario)
    page.add(nome_usuario, email_usuario, senha_usuario, botao_cadastrar)
