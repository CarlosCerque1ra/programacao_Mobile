import flet as ft

def main(page: ft.Page):
    page.title = "Meu Primeiro Botão"
    page.padding = 20

    # Criando um texto que será modificado

    mensagem = ft.Text(
        value="Clique no botão abaixo!",
        size=24,
        color=ft.Colors.BLUE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        """Função que será chamada quando o botão for clicado.
        O parâmetro 'evento' contém informações sobre o evento de clique.
        """
        # Mudando o texto da mensagem 
        mensagem.value = "Parabens! Você clicou no botão! 🎉"
        mensagem.color = ft.Colors.GREEN

        # IMPORTANTE: Sempre que modificamos um componente, precisamos chamar o método page.update() para que as mudanças apareçam na tela.
        page.update()

    # Criando nosso botão
    meu_botao = ft.ElevatedButton(
        text="Clique no botão!", # Texto do botão
        on_click=botao_clicado, # Função que será chamada quando o botão for clicado
        width=200, # Largura do botão
        height=50, # Altura do botão
        bgcolor=ft.Colors.BLUE, # Cor de fundo do botão
        color=ft.Colors.WHITE # Cor do texto do botão
        )

    # Adicionando o texto e o botão à página
    page.add(mensagem)
    page.add(meu_botao)

ft.app(target=main)