import flet as ft

def main(page: ft.Page):
	# Configurações iniciais da página
	page.title = "Calcule seu IMC"
	page.vertical_alignment = ft.MainAxisAlignment.CENTER
	page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
	page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
	page.bgcolor = "#E3F2FD"

	# Campos e elementos
	# Campo para o primeiro número
	numero1 = ft.TextField(label="Peso (kg)", width=250, keyboard_type=ft.KeyboardType.NUMBER, border_radius=10, filled=True, bgcolor="#FFFFFF", border_color="#CCCCCC")
	numero2 = ft.TextField(label="Altura (m)", width=250, keyboard_type=ft.KeyboardType.NUMBER, border_radius=10, filled=True, bgcolor="#FFFFFF", border_color="#CCCCCC")
	# Dropdown para escolher a unidade de medida

	# Texto para mostrar o resultado do IMC
	resultado = ft.Text(value="", size=22, color="#0D47A1", weight=ft.FontWeight.BOLD)

	# Função chamada ao clicar no botão para calcular o IMC
	# Calcula o IMC ao clicar no botão
	def calcular_imc(e):
		try:
			peso = float(numero1.value)
			altura = float(numero2.value)
			imc = peso / (altura * altura)
			if imc < 18.5:
				resultado.value = f"Seu IMC é: {imc:.2f} (Abaixo do peso)"
			elif 18.5 <= imc < 24.9:
				resultado.value = f"Seu IMC é: {imc:.2f} (Peso normal)"
			elif 25 <= imc < 29.9:
				resultado.value = f"Seu IMC é: {imc:.2f} (Sobrepeso)"
			else:
				resultado.value = f"Seu IMC é: {imc:.2f} (Obesidade)"
		except Exception:
			resultado.value = "Valores inválidos."
		page.update()

	# Botão que chama a função de cálculo
	botao = ft.ElevatedButton(
		"Calcular IMC",
		on_click=calcular_imc,
		style=ft.ButtonStyle(
			shape=ft.RoundedRectangleBorder(radius=10),
			bgcolor="#1976D2",
			color="#FFFFFF"
		)
	)

	# Cria o container principal como referência
	container_principal = ft.Container(
		content=ft.Column([
			ft.Text("Calculadora de IMC", size=32, weight=ft.FontWeight.BOLD, color="#0D47A1"),
			numero1,
			numero2,
			botao,
			resultado,
			# O botão de tema será adicionado depois da função
		], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
		padding=30,
		border_radius=20,
		bgcolor="#FFFFFF",
		border=ft.border.all(2, "#CCCCCC"),
		shadow=ft.BoxShadow(blur_radius=20, color="#90CAF9", offset=ft.Offset(0, 8))
	)

	# Função para alternar entre modo claro e escuro
	def alternar_tema(e):
		if page.theme_mode == ft.ThemeMode.LIGHT:
			page.theme_mode = ft.ThemeMode.DARK
			page.bgcolor = "#000000"
			container_principal.bgcolor = "#000000"
			container_principal.border = ft.border.all(2, "#FFFFFF")
			resultado.color = "#74BDEA"
			numero1.bgcolor = "#000000"
			numero2.bgcolor = "#000000"
			numero1.border_color = "#FFFFFF"
			numero2.border_color = "#FFFFFF"
		else:
			page.theme_mode = ft.ThemeMode.LIGHT
			page.bgcolor = "#E3F2FD"
			container_principal.bgcolor = "#FFFFFF"
			container_principal.border = ft.border.all(2, "#CCCCCC")
			resultado.color = "#0D47A1"
			numero1.bgcolor = "#FFFFFF"
			numero2.bgcolor = "#FFFFFF"
			numero1.border_color = "#CCCCCC"
			numero2.border_color = "#CCCCCC"
		page.update()

	botao_tema = ft.Switch(
		on_change = alternar_tema,
	)
	# Adiciona o botão de tema à coluna do container
	container_principal.content.controls.append(botao_tema)
	page.add(container_principal)

	# Executa o app Flet, chamando a função main
if __name__ == "__main__":
	ft.app(target=main)
