# Hola mundo con Flet
import flet as ft

def main(page:ft.Page):
    """
        Es la función principal del programa
        
        Args:
            page: una pagina de flet
    """
    label = ft.Text("Escribe tu Nombre")
    output_text = ft.Text()

    name = ft.TextField()

    def btn_click(e):
        output_text.value = f"Hello, {name.value}!"
        page.update()
    my_btn = ft.ElevatedButton("Enviar",on_click=btn_click)
    page.add(label,name,output_text,my_btn)

ft.app(target=main,view=ft.WEB_BROWSER)