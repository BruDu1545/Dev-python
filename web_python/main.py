# Tela inicial
    # Titulo
    # Botao: iniciar chat
        # quando clicar no boral
        # abrir um pupup
            # titulo: bem vindo ao chat
            # caixa de texto: escreva seu nome
            # Botao: entrar no chat
                # quando clicar no botao
                # sumir com o titulo
                # sumir com o botao iniciar chat
                    # carregar o chat
                    # carregar o campo de enviar mensagem
                    # botao enviar
                        # quando clicar
                        # enviar a mensagem para o chat
                        # limpa da caixa de mensagem
# Usaremos a biblioteca Flet
# Importar o flet
import flet as ft

# Criar uma função principal para rodar o seu aplicativo
def main(page):
    # Titulo
    title = ft.Text("Suport Chat")
    page.add(title)

    def tunnel_menssage(menssage):
        text = ft.Text(menssage)
        chat.controls.append(text)
        # atualizar a pagina
        page.update()

    page.pubsub.subscribe(tunnel_menssage)


    def send_menssage(event):
        # pegar o nome do usuario
        name = name_box.value
        # pega o texto do usuario
        menssage = box_menssage.value
        text = (f"{name}: {menssage}")
        # adiciona a mensagem ao chat
        page.pubsub.send_all(text)
        # limpar a caixa de mensagem
        box_menssage.value = ""
        # atualizar a pagina
        page.update()

    box_menssage = ft.TextField(label="Type your menssage", on_submit=send_menssage)
    send_buttom = ft.ElevatedButton("Send", on_click=send_menssage)
    send_row = ft.Row([box_menssage, send_buttom])

    chat = ft.Column([])

    def enter_chat(event):
        # Fechar o popup
        popup.open = False
        # tirar o titulo
        page.remove(title)
        # tirar o botão
        page.remove(buttom)
        # caregar o chat
        page.add(chat)
        # carregar o campo de enviar mensagem
        page.add(send_row)
        # mensagem "" entrou no chat
        name = name_box.value
        menssge = (f"{name} entrou no chat")
        page.pubsub.send_all(menssge)
        # atualizar a pagina
        page.update()

    
    # Criar um popup
    title_popUp = ft.Text("Welcome to suport chat!")
    name_box = ft.TextField(label="Type your name", on_submit=enter_chat)
    enter_buttom = ft.ElevatedButton("Enter the chat", on_click=enter_chat)
    popup = ft.AlertDialog(title=title_popUp, content=name_box, actions=[enter_buttom])

    def open_popUp(event):
        page.dialog = popup
        popup.open = True
        page.update()
        

    # Botão para iniciar o chat
    buttom = ft.ElevatedButton("Start chat", on_click=open_popUp)
    page.add(buttom)

# Executar essa função com o flet
ft.app(main, view=ft.WEB_BROWSER)