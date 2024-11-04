# import flet as ft
# from models import Usuario, session

# def autenticar_usuario(page, email_usuario, senha):
#     # Verifica se o login existe no banco de dados
#     usuario = session.query(Usuario).filter_by(email_usuario=email_usuario, senha_usuario=senha).first()
#     if usuario:
#         page.clean()
        
#         txt_titulo = ft.Text("LOGIN COM SUCESSO", size=30)
#         botao_voltar = ft.TextButton("Voltar para Login", on_click=lambda e: tela_login(page))
#         page.snack_bar = ft.SnackBar(ft.Text("Login bem-sucedido!"), open=True)
        
#         page.add(
#             txt_titulo,
#             botao_voltar
#         )
#         # Aqui o usuário será direcionado para outra tela após o login
#     else:
#         page.snack_bar = ft.SnackBar(ft.Text("Credenciais incorretas!"), open=True)
#         page.update()

# def cadastrar_usuario(page, nome_usuario, email_usuario, senha_usuario, data_nascimento_usuario, telefone_usuario):
#     # Função para cadastrar um novo usuário
#     novo_usuario = Usuario(
#         nome_usuario=nome_usuario.value, 
#         email_usuario=email_usuario.value,
#         senha_usuario=senha_usuario.value, 
#         data_nascimento_usuario=data_nascimento_usuario.value, 
#         telefone_usuario=telefone_usuario.value
#     )
#     session.add(novo_usuario)
#     session.commit()
#     page.clean()
#     page.snack_bar = ft.SnackBar(ft.Text("Usuário cadastrado com sucesso!"), open=True)
#     tela_login(page)

# def tela_login(page):
#     page.clean()
#     email_usuario = ft.TextField(label="E-mail do Usuário", text_align=ft.TextAlign.LEFT)
#     senha_usuario = ft.TextField(label="Senha", text_align=ft.TextAlign.LEFT, password=True, can_reveal_password=True)
    
#     def login_controlador(e):
#         autenticar_usuario(page, email_usuario.value, senha_usuario.value)

#     botao_login = ft.ElevatedButton("Login", on_click=login_controlador)
#     botao_cadastrar = ft.TextButton("Cadastrar", on_click=lambda e: tela_cadastro(page))
    
#     page.add(email_usuario, senha_usuario, botao_login, botao_cadastrar)

# def tela_cadastro(page):
#     page.clean()
#     nome_usuario = ft.TextField(label="Nome do Usuário", text_align=ft.TextAlign.LEFT)
#     email_usuario = ft.TextField(label="E-mail", text_align=ft.TextAlign.LEFT)
#     senha_usuario = ft.TextField(label="Senha", text_align=ft.TextAlign.LEFT, password=True, can_reveal_password=True)
#     data_nascimento_usuario = ft.TextField(label="Data de Nascimento", text_align=ft.TextAlign.LEFT)
#     telefone_usuario = ft.TextField(label="Telefone", text_align=ft.TextAlign.LEFT)

#     def cadastrar_controlador(e):
#         cadastrar_usuario(page, nome_usuario, email_usuario, senha_usuario, data_nascimento_usuario, telefone_usuario)

#     botao_cadastrar = ft.ElevatedButton("Cadastrar", on_click=cadastrar_controlador)
#     botao_voltar = ft.TextButton("Voltar para Login", on_click=lambda e: tela_login(page))
    
#     page.add(
#         nome_usuario, email_usuario, senha_usuario, 
#         data_nascimento_usuario, telefone_usuario, 
#         botao_cadastrar, botao_voltar
#     )
