import flet as ft

def main(page: ft.Page):
	# Título da página e padding
	page.title = "Calculadora Simples"
	page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)

	# Campos e elementos
	# Campo para o primeiro número
	numero1 = ft.TextField(label="Primeiro número", width=200, keyboard_type=ft.KeyboardType.NUMBER)
	# Campo para o segundo número
	numero2 = ft.TextField(label="Segundo número", width=200, keyboard_type=ft.KeyboardType.NUMBER)
	# Dropdown para escolher a operação
	operacao = ft.Dropdown(
		label="Operação", width=200,
		options=[
			ft.dropdown.Option("Soma"),
			ft.dropdown.Option("Subtração"),
			ft.dropdown.Option("Multiplicação"),
			ft.dropdown.Option("Divisão"),
			ft.dropdown.Option("Porcentagem")
		]
	)

	# Texto para mostrar o resultado
	resultado = ft.Text(
		"Resultado aparecerá aqui", size=20, text_align=ft.TextAlign.CENTER,
		color=ft.Colors.GREY_600
	)

	# Função para calcular o resultado
	def calcular(e):
		try:
			# Tenta converter os valores digitados para float
			num1, num2 = float(numero1.value), float(numero2.value)
			op = operacao.value

			# Se não escolheu operação
			if not op:
				resultado.value = "⚠️ Selecione uma operação!"
				resultado.color = ft.Colors.ORANGE
			# Se for divisão por zero
			elif op == "Divisão" and num2 == 0:
				resultado.value = "❌ Erro: Divisão por zero!"
				resultado.color = ft.Colors.RED
			else:
				# Dicionário para símbolos das operações
				simbolos = {"Soma": "+", "Subtração": "-", "Multiplicação": "x", "Divisão": "/", "Porcentagem": "%"}
				# Dicionário para operações
				op_funcs = {
					"Soma": lambda a, b: a + b,
					"Subtração": lambda a, b: a - b,
					"Multiplicação": lambda a, b: a * b,
					"Divisão": lambda a, b: a / b,
					"Porcentagem": lambda a, b: (a * b) / 100
				}
				res = op_funcs[op](num1, num2)
				simbolo = simbolos[op]
				# Mostra o resultado formatado
				resultado.value = f"{num1} {simbolo} {num2} = {res:.2f}"
				resultado.color = ft.Colors.GREEN
		except ValueError:
			# Caso digite algo inválido
			resultado.value = "❌ Digite números válidos!"
			resultado.color = ft.Colors.RED
		page.update()

	# Função para limpar os campos
	def limpar(e):
		numero1.value = numero2.value = operacao.value = ""
		resultado.value = "Campos limpos!"
		resultado.color = ft.Colors.BLUE
		page.update()

	# Interface
	page.add(
		ft.Column([
			# Título
			ft.Text("🧮 Calculadora Simples", size=24, weight=ft.FontWeight.BOLD),
			numero1,
			numero2,
			operacao,
			# Linha de botões
			ft.Row([
				ft.ElevatedButton("🟩 Calcular", on_click=calcular, width=150, bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
				ft.ElevatedButton("🧹 Limpar", on_click=limpar, width=150, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
			], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
			# Resultado
			resultado
		], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
	)

ft.app(target=main)
# 7ª Digitação (Aqui) ⚠️ ❌ ✨ 🧮 🧹