import flet as ft

def main(page: ft.Page):
    def ir_a_home(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/home",
                [ft.Text("Página de Inicio")]
            )
        )
        page.update()

    def ir_a_ajustes(e):
        page.views.append(
            ft.View(
                "/settings",
                [ft.Text("Página de Ajustes")]
            )
        )
        page.update()

    # Barra de navegación
    page.add(
        ft.AppBar(
            title=ft.Text("Mi App"),
            actions=[
                ft.IconButton(ft.icons.HOME, on_click=ir_a_home),
                ft.IconButton(ft.icons.SETTINGS, on_click=ir_a_ajustes)
            ]
        )
    )

ft.app(target=main)