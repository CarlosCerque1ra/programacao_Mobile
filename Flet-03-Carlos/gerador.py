import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Gerador de Senhas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 350
    page.window_height = 600
    page.padding = 20

    # Paleta de cores
    azul_claro = "#e3f2fd"  # fundo claro
    azul = "#2196f3"        # azul principal
    azul_escuro = "#1565c0" # azul escuro
    # Variável de tema já definida acima
    preto = "#000000"

    is_dark = False
    def get_bg():
        return "#e3f2fd" if not is_dark else "#000000"
        # Os componentes precisam ser definidos antes de serem usados na função de tema
        # Por isso, a função de alternância de tema será definida após todos os componentes
    def get_fg():
        return "#1565c0" if not is_dark else "#ffffff"
    def get_btn_bg():
        return "#2196f3" if not is_dark else "#ffffff"
    def get_btn_fg():
        return "#ffffff" if not is_dark else "#000000"

    senha_atual = ""
    def gerar_senha(e):
        nonlocal senha_atual
        comprimento = int(slider.value)
        caracteres = ""
        if upper_switch.value:
            caracteres += string.ascii_uppercase
        if lower_switch.value:
            caracteres += string.ascii_lowercase
        if numbers_switch.value:
            caracteres += string.digits
        if symbols_switch.value:
            caracteres += string.punctuation

        if caracteres:
            senha = "".join(random.choice(caracteres) for _ in range(comprimento))
            senha_output.value = senha
            senha_atual = senha
            # Mostra o botão de copiar explícito
            copiar_btn.visible = True
        else:
            senha_output.value = "Selecione ao menos um tipo de caractere."
            senha_atual = ""
            copiar_btn.visible = False
    page.update()

    def mostrar_senha_copiada(e):
        nonlocal senha_atual
        if senha_atual:
            # Exibir mensagem de feedback usando text_display
            text_display.value = f"Senha copiada: {senha_atual}"
            text_display.visible = True
            page.update()
            # Opcional: tentar usar os métodos de clipboard disponíveis
            try:
                page.set_clipboard(senha_atual)
            except:
                pass # Ignora se falhar

    # Função de alternância de tema será definida após a criação do theme_button

    is_dark = False

    def togle_theme(e):
        nonlocal is_dark
        is_dark = not is_dark
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        theme_button.icon = ft.Icons.DARK_MODE if is_dark else ft.Icons.LIGHT_MODE
        senha_output.bgcolor = get_bg()
        senha_output.color = get_fg()
        text_display.color = get_fg()
        copiar_btn.bgcolor = get_btn_bg()
        copiar_btn.color = get_btn_fg()
    # gerar_button já recebe as cores na criação
        preferencias_container.bgcolor = get_bg()
        page.bgcolor = get_bg()
        page.update()

    theme_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        on_click=togle_theme
    )

    title_switch_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Gerador de Senhas", size=28, weight="bold", color=get_fg()),
            theme_button
        ]
    )

    title_switch_container = ft.Container(
        content=title_switch_row,
        padding=ft.padding.only(top=50),
        bgcolor=get_bg(),
    )

    senha_output = ft.TextField(
        value="",
        label="Senha Gerada",
        read_only=True,
        width=280,
        bgcolor=get_bg(),
        color=get_fg(),
    )

    # Campo de texto para exibir feedback quando a senha for "copiada"
    text_display = ft.Text(
        value="",
        color=get_fg(),
        visible=False
    )

    # Botão explícito para copiar
    copiar_btn = ft.ElevatedButton(
        text="COPIAR SENHA",
        on_click=mostrar_senha_copiada,
        color=get_btn_fg(),
        bgcolor=get_btn_bg(),
        visible=False
    )

    slider = ft.Slider(
        min=8,
        max=20,
        value=12,
        divisions=12,
        label="CARACTERES: {value}"
    )

    upper_switch = ft.Switch(label="Letras maiúsculas")
    lower_switch = ft.Switch(label="Letras minúsculas", value=True)
    numbers_switch = ft.Switch(label="Incluir números")
    symbols_switch = ft.Switch(label="Incluir símbolos")

    preferencias_column = ft.Column(
        [
            ft.Text("PREFERÊNCIAS", size=16, weight="bold", color=get_fg()),
            upper_switch,
            lower_switch,
            numbers_switch,
            symbols_switch,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    preferencias_container = ft.Container(
        content=preferencias_column,
        padding=ft.padding.all(20),
        alignment=ft.alignment.top_left,
        border=ft.border.all(2, "#e3f2fd")
    )
    gerar_button = ft.ElevatedButton(
        text="GERAR SENHA",
        on_click=gerar_senha,
        color=get_btn_fg(),
        bgcolor=get_btn_bg()
    )

    page.bgcolor = get_bg()
    page.add(
        ft.Column(
            [
                title_switch_container,
                senha_output,
                text_display,
                copiar_btn,
                slider,
                preferencias_container,
                gerar_button,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )

ft.app(
    target=main,
    assets_dir="assets"
)