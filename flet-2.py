# Filas y columnas con FLet

import flet as ft

def main(page:ft.Page):
    # Diseño con filas y columnas
    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ]),
        ft.Column(controls=[
            ft.Text("1"),
            ft.Text("2"),
            ft.Text("hhhhhhhhhhhhhhhhhhhhh3")
        ],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )


ft.app(target=main,view=ft.WEB_BROWSER)