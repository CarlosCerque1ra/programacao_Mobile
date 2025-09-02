# 📱 Flet-01-Carlos

Este repositório reúne uma série de aplicativos desenvolvidos em Python com o framework Flet, mostrando a evolução do aprendizado em interfaces gráficas e programação mobile.

---

## ✨ Evolução dos Códigos

Cada arquivo representa um passo na jornada de aprendizado, começando pelo básico e avançando para desafios mais complexos e aplicações completas.

### 1. `1_primeiro_app.py` — Primeiros Passos
- **Descrição:** Criação de uma janela simples com texto centralizado. Introduz os conceitos básicos do Flet, como configuração da página e adição de elementos.
- **Evolução:** Serve como base para entender a estrutura de um app Flet.

### 2. `2_botao_simples.py` — Interatividade
- **Descrição:** Adiciona um botão que, ao ser clicado, altera o texto exibido. Introduz eventos e manipulação de estado.
- **Evolução:** Mostra como responder a ações do usuário.

### 3. `3_campo_texto.py` — Entrada de Dados
- **Descrição:** Permite ao usuário digitar seu nome e exibe uma mensagem personalizada. Apresenta validação de entrada e feedback visual.
- **Evolução:** Explora interação mais dinâmica e validação.

### 4. `4_lista_cores.py` — Seleção e Estilo
- **Descrição:** Usuário escolhe uma cor em um dropdown e uma caixa muda de cor. Demonstra uso de listas, dicionários e atualização visual.
- **Evolução:** Introduz componentes de seleção e manipulação de estilos.

### 5. `5_layout_basico.py` — Organização Visual
- **Descrição:** Exemplo de layouts com Column e Row, organizando botões e caixas coloridas. Ensina sobre alinhamento e espaçamento.
- **Evolução:** Foca em design responsivo e organização de elementos.

### 6. `5a_desafio1.py` — Formulário Interativo
- **Descrição:** Desafio prático: formulário para cadastro de perfil, com validação, feedback de erro e cartão visual do perfil.
- **Evolução:** Integra vários conceitos anteriores em uma aplicação mais completa.

### 7. `6_contador.py` — Estado e Controle
- **Descrição:** Contador com botões de incremento, decremento e reset. Mostra como manipular variáveis de estado e atualizar a interface.
- **Evolução:** Prática de controle de estado e feedback visual.

### 8. `7_calculadora.py` — Lógica e Operações
- **Descrição:** Calculadora funcional com operações básicas e tratamento de erros (ex: divisão por zero). Apresenta lógica condicional e funções.
- **Evolução:** Exercício de lógica matemática e interface amigável.

### 9. `8_painel_conf.py` — Personalização
- **Descrição:** Painel para configurar estilo de texto (negrito, itálico, sublinhado, cor, tamanho). Explora switches, sliders e dropdowns.
- **Evolução:** Demonstra personalização avançada de componentes.

### 10. `9_galeria_cards.py` — Listas e Filtros
- **Descrição:** Galeria de cards de animais, com filtros por categoria e tamanho. Usa GridView, Dropdown e TextField para busca.
- **Evolução:** Apresenta manipulação de listas, filtros dinâmicos e layout em grade.

### 11. `10_app_multipagina.py` — Navegação
- **Descrição:** App com navegação entre páginas (Home, Perfil, Configurações, Sobre), barra de navegação inferior e estado global.
- **Evolução:** Introduz navegação, gerenciamento de múltiplas telas e estado compartilhado.

### 12. `10a_desafio2.py` — Aplicação Final: Loja Virtual
- **Descrição:** Mini loja virtual com produtos, carrinho de compras, cálculo de total, filtros e notificações. Integra todos os conceitos aprendidos.
- **Evolução:** Demonstra domínio de componentes, lógica, estado, filtros e interface completa.

---

## 🗂️ Imagens Ilustrativas

A pasta `Códigos/` contém imagens de cada projeto, facilitando a visualização dos resultados.

---

## 🚀 Como Executar

1. Instale o Python 3.10+ e o pacote Flet:
   ```powershell
   pip install flet
   ```
2. Execute o arquivo desejado:
   ```powershell
   python nome_do_arquivo.py
   ```

---

## 📦 Códigos Fonte

### 1_primeiro_app.py
```python
import flet as ft

def main(page: ft.Page):
	"""
	Função principal que será executada quando o app iniciar.
	O parâmetro 'page' representa a tela/página do nosso app.
	"""

	# Configurações básicas da página
	page.title = "Meu Primeiro App Flet"  # Título que aparece na aba do navegador
	page.padding = 20  # Espaçamento interno da página

	# Criando nosso primeiro elemento: um texto
	meu_texto = ft.Text(
		value="👋 Hello world! (Primeiro app com Flet!)",  # O texto que será exibido
		size=24,  # Tamanho da fonte
		color=ft.Colors.BLUE,  # Cor do texto
		weight=ft.FontWeight.BOLD,  # Texto em negrito
		text_align=ft.TextAlign.CENTER  # Centralizar o texto
	)

	# Adicionando o texto à nossa página
	page.add(meu_texto)

	# Vamos adicionar mais alguns elementos para tornar mais interessante
	page.add(
		ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=16),
		ft.Text("Com Flet, você pode criar apps incríveis! 🚀", size=16, color=ft.Colors.GREEN)
	)

# Esta linha inicia nosso aplicativo, chamando a função main
ft.app(target=main)
```

### 2_botao_simples.py
```python
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
```

### 3_campo_texto.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Texto"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)  # Padding superior para área segura

    # Criando um campo onde o usuário pode digitar
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",  # Texto de orientação
        width=300,  # Largura do campo
        border_color=ft.Colors.BLUE  # Cor da borda
    )

    # Texto que mostrará a resposta
    resposta = ft.Text(
        value="",  # Inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER
    )

    def processar_nome(evento):
        """
        Função que pega o texto digitado pelo usuário e faz algo com ele.
        """
        # Pegando o valor digitado no campo
        nome_digitado = campo_nome.value

        # Verificando se o usuário realmente digitou algo
        if nome_digitado == "" or nome_digitado is None:
            resposta.value = "⚠️ Por favor, digite seu nome!"
            resposta.color = ft.Colors.RED
        elif len(nome_digitado) < 2:
            resposta.value = "⚠️ Nome muito curto!"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f"✅ Olá, {nome_digitado}! Prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN

        # Atualizando a interface
        page.update()

    # Botão para processar o nome
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150
    )

    # Adicionando elementos à página
    page.add(
        ft.Text("Vamos nos conhecer! 😊", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta
    )

ft.app(target=main)
```

### 4_lista_cores.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Seleção de Cores"
    page.padding = 20

    # Dicionário de cores
    cores = {
        "Vermelho": ft.Colors.RED,
        "Verde": ft.Colors.GREEN,
        "Azul": ft.Colors.BLUE,
        "Amarelo": ft.Colors.YELLOW,
        "Ciano": ft.Colors.CYAN,
        "Magenta": ft.Colors.MAGENTA
    }

    # Caixa que mudará de cor
    caixa_cor = ft.Container(
        width=200,
        height=200,
        bgcolor=ft.Colors.GRAY_200,
        border_radius=10,
        alignment=ft.Alignment.CENTER,
        content=ft.Text("Minha Cor Favorita!", size=16, weight=ft.FontWeight.BOLD)
    )

    # Dropdown para seleção de cor
    dropdown_cores = ft.Dropdown(
        label="Escolha uma cor",
        options=[ft.dropdown.Option(nome) for nome in cores.keys()],
        width=300
    )

    def mudar_cor(e):
        """Muda a cor da caixa com base na seleção do dropdown."""
        cor_selecionada = dropdown_cores.value
        if cor_selecionada:
            caixa_cor.bgcolor = cores[cor_selecionada]
            caixa_cor.content = ft.Text(f"Você escolheu {cor_selecionada}!", size=16, weight=ft.FontWeight.BOLD)
        else:
            caixa_cor.bgcolor = ft.Colors.GRAY_200
            caixa_cor.content = ft.Text("Minha Cor Favorita!", size=16, weight=ft.FontWeight.BOLD)
        page.update()

    # Evento para mudança no dropdown
    dropdown_cores.on_change = mudar_cor

    # Adicionando elementos à página
    page.add(
        ft.Text("Selecione uma cor da lista:", size=22, weight=ft.FontWeight.BOLD),
        dropdown_cores,
        caixa_cor
    )

ft.app(target=main)
```

### 5_layout_basico.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Layout Básico com Flet"
    page.padding = 20

    # Cabeçalho
    page.add(
        ft.AppBar(
            title=ft.Text("Minha Aplicação"),
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE
        )
    )

    # Conteúdo principal
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.icons.HOME, tooltip="Início"),
                        ft.IconButton(ft.icons.INFO, tooltip="Sobre"),
                        ft.IconButton(ft.icons.CONTACT_MAIL, tooltip="Contato")
                    ],
                    alignment="spaceAround"
                ),
                ft.Container(
                    ft.Text("Bem-vindo à minha aplicação!", size=24),
                    alignment=ft.Alignment.CENTER,
                    padding=20
                ),
                ft.Row(
                    [
                        ft.ElevatedButton("Botão 1", width=120),
                        ft.ElevatedButton("Botão 2", width=120),
                        ft.ElevatedButton("Botão 3", width=120)
                    ],
                    alignment="center",
                    spacing=10
                )
            ],
            alignment="center",
            spacing=20
        )
    )

    # Rodapé
    page.add(
        ft.Footer(
            content=ft.Text("Meu Rodapé - Todos os direitos reservados", size=12),
            bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE,
            height=50
        )
    )

ft.app(target=main)
```

### 5a_desafio1.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Desafio: Formulário Interativo"
    page.padding = 20

    # Função para validar e enviar o formulário
    def enviar_formulario(e):
        nome = campo_nome.value
        email = campo_email.value
        senha = campo_senha.value

        # Validação simples
        if not nome or not email or not senha:
            resultado.value = "⚠️ Por favor, preencha todos os campos!"
            resultado.color = ft.Colors.RED
        else:
            resultado.value = f"✅ Bem-vindo, {nome}! Seu cadastro foi realizado com sucesso."
            resultado.color = ft.Colors.GREEN

        # Atualiza a página para mostrar a mensagem de resultado
        page.update()

    # Campos do formulário
    campo_nome = ft.TextField(label="Nome completo", width=300)
    campo_email = ft.TextField(label="E-mail", width=300)
    campo_senha = ft.TextField(label="Senha", width=300, password=True)

    # Botão de envio
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_formulario)

    # Área para mostrar o resultado
    resultado = ft.Text("", size=16, text_align=ft.TextAlign.CENTER)

    # Adiciona os elementos à página
    page.add(
        ft.Text("Cadastro de Usuário", size=24, weight=ft.FontWeight.BOLD),
        campo_nome,
        campo_email,
        campo_senha,
        botao_enviar,
        resultado
    )

ft.app(target=main)
```

### 6_contador.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Contador Simples"
    page.padding = 20

    # Variável para armazenar o estado do contador
    contador = 0

    # Função para atualizar o valor exibido do contador
    def atualizar_contador():
        texto_contador.value = f"Contador: {contador}"
        page.update()

    # Função chamada ao clicar no botão de incrementar
    def incrementar(e):
        nonlocal contador
        contador += 1
        atualizar_contador()

    # Função chamada ao clicar no botão de decrementar
    def decrementar(e):
        nonlocal contador
        contador -= 1
        atualizar_contador()

    # Texto que exibe o valor do contador
    texto_contador = ft.Text(f"Contador: {contador}", size=32, weight=ft.FontWeight.BOLD)

    # Botões para controlar o contador
    botao_incrementar = ft.ElevatedButton("Incrementar", on_click=incrementar)
    botao_decrementar = ft.ElevatedButton("Decrementar", on_click=decrementar)

    # Adiciona os elementos à página
    page.add(
        ft.Text("Controle de Contador", size=24, weight=ft.FontWeight.BOLD),
        texto_contador,
        ft.Row(
            [botao_incrementar, botao_decrementar],
            alignment="center",
            spacing=10
        )
    )

ft.app(target=main)
```

### 7_calculadora.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora Simples"
    page.padding = 20

    # Inicializa o estado da calculadora
    operacao = ""
    valor_atual = "0"

    # Atualiza o display da calculadora
    def atualizar_display():
        display.value = valor_atual
        page.update()

    # Adiciona um dígito ao valor atual
    def adicionar_digito(digito):
        nonlocal valor_atual
        if valor_atual == "0":
            valor_atual = digito
        else:
            valor_atual += digito
        atualizar_display()

    # Define a operação a ser realizada
    def definir_operacao(op):
        nonlocal operacao
        operacao = op
        adicionar_digito(" ")

    # Calcula o resultado da operação
    def calcular():
        try:
            nonlocal valor_atual
            # Avalia a expressão matemática
            resultado = eval(valor_atual)
            valor_atual = str(resultado)
        except:
            valor_atual = "Erro"
        atualizar_display()

    # Botões numéricos
    botoes_numericos = [
        ft.Button(str(i), on_click=lambda e, i=i: adicionar_digito(str(i)), width=60, height=60)
        for i in range(10)
    ]

    # Layout da calculadora
    display = ft.TextField(value=valor_atual, width=280, height=60, text_align="right", readonly=True)
    botoes_operacao = [
        ft.Button(op, on_click=lambda e, op=op: definir_operacao(op), width=60, height=60)
        for op in ["+", "-", "*", "/"]
    ]
    botao_calcular = ft.Button("=", on_click=lambda e: calcular(), width=60, height=60)
    botao_limpar = ft.Button("C", on_click=lambda e: adicionar_digito(""), width=60, height=60)

    # Adiciona os elementos à página
    page.add(
        ft.Row([display]),
        ft.Column(
            [
                ft.Row(botoes_numericos[1:4]),
                ft.Row(botoes_numericos[4:7]),
                ft.Row([botoes_numericos[0], botao_calcular]),
                ft.Row([botoes_operacao[0], botoes_operacao[1]]),
                ft.Row([botoes_operacao[2], botoes_operacao[3]]),
                ft.Row([botao_limpar])
            ],
            alignment="center",
            spacing=10
        )
    )

ft.app(target=main)
```

### 8_painel_conf.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Painel de Configuração"
    page.padding = 20

    # Função para atualizar o texto de exemplo
    def atualizar_texto(e):
        texto_exemplo.value = campo_texto.value
        page.update()

    # Campo de texto para entrada do usuário
    campo_texto = ft.TextField(
        label="Digite algo",
        placeholder="Texto de exemplo",
        width=300
    )

    # Texto que será atualizado com a entrada do usuário
    texto_exemplo = ft.Text(
        value="",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE
    )

    # Adiciona os elementos à página
    page.add(
        ft.Text("Configuração de Texto", size=28, weight=ft.FontWeight.BOLD),
        campo_texto,
        ft.ElevatedButton("Atualizar Texto", on_click=atualizar_texto),
        texto_exemplo
    )

ft.app(target=main)
```

### 9_galeria_cards.py
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Galeria de Imagens"
    page.padding = 20

    # Dados das imagens (substitua pelos seus)
    imagens = [
        {"titulo": "Imagem 1", "caminho": "https://via.placeholder.com/150"},
        {"titulo": "Imagem 2", "caminho": "https://via.placeholder.com/150/0000FF"},
        {"titulo": "Imagem 3", "caminho": "https://via.placeholder.com/150/008000"},
        {"titulo": "Imagem 4", "caminho": "https://via.placeholder.com/150/FF0000"}
    ]

    # Cria os cards para cada imagem
    for img in imagens:
        card = ft.Card(
            content=ft.Column(
                [
                    ft.Image(src=img["caminho"], fit=ft.ImageFit.COVER),
                    ft.Text(img["titulo"], size=16, weight=ft.FontWeight.BOLD)
                ]
            ),
            elevation=4,
            margin=10
        )
        page.add(card)

ft.app(target=main)
```

### 10_app_multipagina.py
```python
import flet as ft

# Função para construir a página inicial
def pagina_inicial(page):
    page.title = "Página Inicial"
    page.add(ft.Text("Bem-vindo à Página Inicial!"))

# Função para construir a página sobre
def pagina_sobre(page):
    page.title = "Sobre"
    page.add(ft.Text("Esta é a página sobre o aplicativo."))

# Função principal que será executada ao iniciar o aplicativo
def main(page: ft.Page):
    # Configurações iniciais da página
    page.title = "Meu App Multi-Página"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Cria uma barra de navegação na parte inferior
    page.add(
        ft.BottomNavigation(
            [
                ft.BottomNavigationItem(
                    icon=ft.icons.HOME,
                    label="Início",
                    on_click=lambda e: pagina_inicial(page)
                ),
                ft.BottomNavigationItem(
                    icon=ft.icons.INFO,
                    label="Sobre",
                    on_click=lambda e: pagina_sobre(page)
                )
            ]
        )
    )

    # Chama a função para construir a página inicial
    pagina_inicial(page)

# Inicia o aplicativo Flet
ft.app(target=main)
```

### 10a_desafio2.py
```python
import flet as ft

# Simula um banco de dados de produtos
produtos = [
    {"id": 1, "nome": "Produto A", "preco": 10.0},
    {"id": 2, "nome": "Produto B", "preco": 15.0},
    {"id": 3, "nome": "Produto C", "preco": 20.0}
]

# Função principal do aplicativo
def main(page: ft.Page):
    page.title = "Loja Virtual"
    page.padding = 20

    # Exibe a lista de produtos
    def exibir_produtos():
        for produto in produtos:
            page.add(
                ft.Card(
                    content=ft.Column(
                        [
                            ft.Text(produto["nome"], size=20, weight=ft.FontWeight.BOLD),
                            ft.Text(f"Preço: R$ {produto['preco']:.2f}"),
                            ft.ElevatedButton(
                                "Adicionar ao Carrinho",
                                on_click=lambda e, p=produto: adicionar_ao_carrinho(p)
                            )
                        ]
                    ),
                    elevation=4,
                    margin=10
                )
            )

    # Adiciona um produto ao carrinho (simulação)
    def adicionar_ao_carrinho(produto):
        page.add(ft.SnackBar(ft.Text(f"{produto['nome']} adicionado ao carrinho!")))
        page.update()

    # Exibe a lista de produtos ao iniciar o aplicativo
    exibir_produtos()

# Inicia o aplicativo Flet
ft.app(target=main)
```
