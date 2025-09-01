import flet as ft

def main(page: ft.Page):
    # Configurações iniciais
    page.title = "Loja Virtual Mini"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_50

    # Estado do carrinho
    carrinho = []
    total_carrinho = 0.0

    # Elementos da interface
    area_produtos = ft.GridView(
        expand=1,
        runs_count=2,
        max_extent=180,
        child_aspect_ratio=0.9,
        spacing=15,
        run_spacing=15
    )
    contador_carrinho = ft.Text("Carrinho (0)", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_700)
    total_texto = ft.Text("Total: R$ 0,00", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
    lista_carrinho = ft.ListView(height=150, spacing=5)
    notificacao = ft.Text(size=14, color=ft.Colors.BLUE_600, text_align=ft.TextAlign.CENTER)

    # Lista de produtos
    produtos = [
        {"nome": "Masserati", "preco": 150000.00, "categoria": "Esportivo", "emoji": "🏎️", "cor": ft.Colors.RED_400},
        {"nome": "Honda Civic", "preco": 80000.00, "categoria": "Sedan", "emoji": "🚗", "cor": ft.Colors.BLUE_400},
        {"nome": "Civic VTI", "preco": 45000.00, "categoria": "Hatch", "emoji": "🚙", "cor": ft.Colors.GREEN_400},
        {"nome": "Mustang Fastback", "preco": 120000.00, "categoria": "Coupe", "emoji": "🚘", "cor": ft.Colors.PURPLE_400},
        {"nome": "AUDI RS6", "preco": 70000.00, "categoria": "Whagon", "emoji": "🚐", "cor": ft.Colors.ORANGE_400},
        {"nome": "Dodge Demon", "preco": 200000.00, "categoria": "Dragster", "emoji": "🏁", "cor": ft.Colors.YELLOW_700},
        {"nome": "Up TSI", "preco": 95000.00, "categoria": "Turbo", "emoji": "💨", "cor": ft.Colors.CYAN_400},
        {"nome": "Ranger", "preco": 30000.00, "categoria": "Aspirado", "emoji": "🛻", "cor": ft.Colors.BROWN_400},
        {"nome": "X6 ", "preco": 60000.00, "categoria": "Familia", "emoji": "🚚", "cor": ft.Colors.PINK_400},
        {"nome": "Passat", "preco": 250000.00, "categoria": "Sedan", "emoji": "🚖", "cor": ft.Colors.BLACK},
        {"nome": "Opala ", "preco": 40000.00, "categoria": "Sedan", "emoji": "🚕", "cor": ft.Colors.GREY_700},
        {"nome": "Fusca ", "preco": 35000.00, "categoria": "Hatch", "emoji": "🚗", "cor": ft.Colors.BLUE_GREY_400},
        {"nome": "Mustang ", "preco": 180000.00, "categoria": "Coupe", "emoji": "🏎️", "cor": ft.Colors.RED_700},
        {"nome": "Civic ", "preco": 90000.00, "categoria": "Sedan", "emoji": "🚘", "cor": ft.Colors.GREEN_700},
        {"nome": "Corolla ", "preco": 85000.00, "categoria": "Sedan", "emoji": "🚗", "cor": ft.Colors.YELLOW_600},
        {"nome": "Camaro ", "preco": 160000.00, "categoria": "Clássico", "emoji": "🏁", "cor": ft.Colors.ORANGE_700},
        {"nome": "Jeep ", "preco": 110000.00, "categoria": "Whagon", "emoji": "🚙", "cor": ft.Colors.BROWN_600},
        {"nome": "Fiat 500 ", "preco": 40000.00, "categoria": "Hatch", "emoji": "🚗", "cor": ft.Colors.PINK_600},
        {"nome": "Audi A4 ", "preco": 230000.00, "categoria": "Sedan", "emoji": "🚖", "cor": ft.Colors.BLACK87},
        {"nome": "BMW Série 3", "preco": 240000.00, "categoria": "Sedan", "emoji": "🚕", "cor": ft.Colors.GREY_800},
        {"nome": "Chevrolet Malibu", "preco": 220000.00, "categoria": "Vintage", "emoji": "🚘", "cor": ft.Colors.BLUE_800},
        {"nome": "Volkswagen Golf", "preco": 95000.00, "categoria": "Luxo", "emoji": "🚗", "cor": ft.Colors.GREEN_800},
        {"nome": "Nissan Altima", "preco": 210000.00, "categoria": "Sedan", "emoji": "🚖", "cor": ft.Colors.YELLOW_800},
        {"nome": "Mazda CX-5", "preco": 130000.00, "categoria": "Whagon", "emoji": "🚙", "cor": ft.Colors.RED_800},
        {"nome": "Subaru Outback", "preco": 140000.00, "categoria": "Whagon", "emoji": "🚐", "cor": ft.Colors.ORANGE_800},
        {"nome": "Tesla Model 3", "preco": 300000.00, "categoria": "Sedan", "emoji": "🚘", "cor": ft.Colors.CYAN_700},
        {"nome": "Kia Sorento", "preco": 160000.00, "categoria": "Whagon", "emoji": "🚚", "cor": ft.Colors.PURPLE_700},
        {"nome": "Hyundai Tucson", "preco": 150000.00, "categoria": "Whagon", "emoji": "🚙", "cor": ft.Colors.BROWN_700},
        {"nome": "Renault Duster", "preco": 90000.00, "categoria": "Whagon", "emoji": "🚐", "cor": ft.Colors.GREY_600},
        {"nome": "Peugeot 208", "preco": 85000.00, "categoria": "Hatch", "emoji": "🚗", "cor": ft.Colors.BLUE_600}  









    ]

    # Filtros
    filtro_categoria = ft.Dropdown(
        label="Categoria",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        width=150,
        value="Todas",
        color=ft.Colors.BLACK,
        options=[
            ft.dropdown.Option("Todas"),
            ft.dropdown.Option("Hatch"),
            ft.dropdown.Option("Sedan"),
            ft.dropdown.Option("Coupe"),
            ft.dropdown.Option("Esportivo"),
            ft.dropdown.Option("Whagon"),
            ft.dropdown.Option("Dragster"),
            ft.dropdown.Option("Turbo"),
            ft.dropdown.Option("Aspirado"),
            ft.dropdown.Option("Familia"),
            ft.dropdown.Option("Luxo"),
            ft.dropdown.Option("Clássico"),
            ft.dropdown.Option("Vintage"),
            ft.dropdown.Option("Potente")



        ]
    )
    filtro_preco = ft.Dropdown(
        label="Preço",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=150,
        value="Todos",
        options=[
            ft.dropdown.Option("Todos"),
            ft.dropdown.Option("Até R$ 100"),
            ft.dropdown.Option("R$ 100-500"),
            ft.dropdown.Option("Acima R$ 500"),
            ft.dropdown.Option("Acima R$ 1000"),
            ft.dropdown.Option("Acima R$ 5000"),
            ft.dropdown.Option("Acima R$ 10000"),
            ft.dropdown.Option("Acima R$ 50000"),
            ft.dropdown.Option("Acima R$ 100000"),
            ft.dropdown.Option("Acima R$ 500000")
        ]
    )
    campo_busca = ft.TextField(
        label="Buscar produto",
        label_style=ft.TextStyle(color=ft.Colors.BLACK),
        color=ft.Colors.BLACK,
        width=200,
        prefix_icon=ft.Icons.SEARCH
    )

    # Funções principais
    def mostrar_notificacao(msg):
        notificacao.value = msg
        page.update()

    def atualizar_carrinho():
        contador_carrinho.value = f"Carrinho ({len(carrinho)})"
        total_texto.value = f"Total: R$ {total_carrinho:.2f}"
        lista_carrinho.controls.clear()
        for i, item in enumerate(carrinho):
            linha = ft.Row([
                ft.Text(item["nome"], expand=True),
                ft.Text(f"R$ {item['preco']:.2f}", color=ft.Colors.GREEN_600),
                ft.IconButton(
                    ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=lambda e, idx=i: remover_do_carrinho(idx)
                )
            ], spacing=10)
            lista_carrinho.controls.append(linha)
        page.update()

    def adicionar_ao_carrinho(nome, preco):
        nonlocal total_carrinho
        carrinho.append({"nome": nome, "preco": preco})
        total_carrinho += preco
        atualizar_carrinho()
        mostrar_notificacao(f"✅ {nome} adicionado!")

    def remover_do_carrinho(idx):
        nonlocal total_carrinho
        if 0 <= idx < len(carrinho):
            produto = carrinho.pop(idx)
            total_carrinho -= produto["preco"]
            atualizar_carrinho()
            mostrar_notificacao(f"❌ {produto['nome']} removido")

    def criar_card_produto(nome, preco, categoria, emoji, cor):
        return ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=40, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    nome,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                    max_lines=2,
                    overflow=ft.TextOverflow.ELLIPSIS
                ),
                ft.Text(
                    f"R$ {preco:.2f}",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
            ),
            bgcolor=cor,
            padding=20,
            border_radius=15,
            width=160,
            height=180,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=8,
                color=ft.Colors.with_opacity(0.3, ft.Colors.BLACK)
            ),
            on_click=lambda e, n=nome, p=preco: adicionar_ao_carrinho(n, p),
            ink=True
        )

    def carregar_produtos(e=None):
        area_produtos.controls.clear()
        categoria = filtro_categoria.value
        preco_faixa = filtro_preco.value
        busca = (campo_busca.value or "").lower()
        for produto in produtos:
            # Filtro categoria
            if categoria != "Todas" and produto["categoria"] != categoria:
                continue
            # Filtro preço
            if preco_faixa == "Até R$ 100" and produto["preco"] > 100:
                continue
            elif preco_faixa == "R$ 100-500" and not (100 < produto["preco"] <= 500):
                continue
            elif preco_faixa == "Acima R$ 500" and produto["preco"] <= 500:
                continue
            elif preco_faixa == "Acima R$ 1000" and produto["preco"] <= 1000:
                continue
            elif preco_faixa == "Acima R$ 5000" and produto["preco"] <= 5000:
                continue
            elif preco_faixa == "Acima R$ 10000" and produto["preco"] <= 10000:
                continue
            elif preco_faixa == "Acima R$ 50000" and produto["preco"] <= 50000:
                continue
            elif preco_faixa == "Acima R$ 100000" and produto["preco"] <= 100000:
                continue
            elif preco_faixa == "Acima R$ 500000" and produto["preco"] <= 500000:
                continue
            # Filtro busca
            if busca and busca not in produto["nome"].lower():
                continue
            card = criar_card_produto(
                produto["nome"], produto["preco"], produto["categoria"], produto["emoji"], produto["cor"]
            )
            area_produtos.controls.append(card)
        page.update()

    def finalizar_compra(e):
        nonlocal total_carrinho
        if len(carrinho) > 0:
            carrinho.clear()
            total_carrinho = 0.0
            atualizar_carrinho()
            mostrar_notificacao("🎉 Compra finalizada! Obrigado!")
        else:
            mostrar_notificacao("⚠️ Carrinho vazio!")

    def limpar_filtros(e):
        filtro_categoria.value = "Todas"
        filtro_preco.value = "Todos"
        campo_busca.value = ""
        carregar_produtos()
        mostrar_notificacao("🧹 Filtros limpos!")
        page.update()

    # Eventos dos filtros
    for controle in [filtro_categoria, filtro_preco, campo_busca]:
        controle.on_change = carregar_produtos

    # Carrega produtos inicialmente
    carregar_produtos()

    # Interface
    page.add(
        ft.Column([
            ft.Text(
                "🛒 Loja Virtual Mini",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.BLUE_800,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Encontre os melhores produtos!",
                size=14,
                color=ft.Colors.GREY_600,
                text_align=ft.TextAlign.CENTER
            ),
            # Filtros
            ft.Row(
                [filtro_categoria, filtro_preco],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20
            ),
            ft.Row(
                [
                    campo_busca,
                    ft.ElevatedButton(
                        "🧹 Limpar Filtros",
                        on_click=limpar_filtros,
                        bgcolor=ft.Colors.ORANGE_400,
                        color=ft.Colors.WHITE,
                        height=40,
                        style=ft.ButtonStyle(
                            text_style=ft.TextStyle(size=12, weight=ft.FontWeight.BOLD)
                        )
                    )
                ]
            ),
            # Produtos
            ft.Container(
                content=area_produtos,
                height=400,
                border=ft.border.all(1, ft.Colors.GREY_300),
                border_radius=10,
                padding=10
            ),
            # Carrinho
            ft.Container(
                content=ft.Column([
                    ft.Row(
                        [contador_carrinho, total_texto],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    lista_carrinho,
                    ft.Row([
                        ft.ElevatedButton(
                            "🛒 Finalizar Compra",
                            on_click=finalizar_compra,
                            bgcolor=ft.Colors.GREEN,
                            color=ft.Colors.WHITE,
                            width=200
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    notificacao
                ], spacing=10),
                bgcolor=ft.Colors.WHITE,
                padding=20,
                border_radius=10,
                shadow=ft.BoxShadow(
                    spread_radius=1,
                    blur_radius=3,
                    color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
                )
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15
        )
    )

ft.app(target=main)

    
