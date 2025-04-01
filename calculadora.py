"""
Calculadora Flet - Proyecto Paso a Paso
Autor: TuNombre
"""

# === Importar Flet ===
# Documentación: https://flet.dev/docs/
import flet as ft

# === Clase Calculadora ===
# Hereda de ft.Column para crear un control personalizado
class Calculadora(ft.Column):
    def __init__(self):
        # Llamar al constructor de la clase padre
        super().__init__()
        
        # === Crear Display (Campo de Texto) ===
        # Documentación: https://flet.dev/docs/controls/textfield
        self.display = ft.TextField(
            value="0",  # Valor inicial
            text_align=ft.TextAlign.RIGHT,  # Alineación derecha
            read_only=True,  # Solo lectura (no editable)
            bgcolor=ft.colors.WHITE,  # Fondo blanco
            color=ft.colors.BLACK,  # Texto negro
            border=ft.InputBorder.NONE,  # Sin bordes
            text_size=40,  # Tamaño de fuente
            expand=True,  # Ocupar todo el ancho disponible
            height=80  # Altura fija
        )
        
        # === Construir Interfaz ===
        # Documentación: https://flet.dev/docs/controls/column
        self.controls = [
            # Contenedor del Display
            ft.Container(
                content=self.display,
                bgcolor=ft.colors.BLUE_GREY_900,  # Fondo oscuro
                padding=10,  # Espaciado interno
                border_radius=15,  # Bordes redondeados
                shadow=ft.BoxShadow(  # Sombra
                    spread_radius=2,
                    blur_radius=10
                )
            ),
            # Teclado Numérico
            self._crear_teclado()
        ]

    # === Método para Crear Teclado ===
    def _crear_teclado(self):
        # Matriz de botones (4x4)
        botones = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", ".", "+"],
            ["="]
        ]
        
        # Crear filas de botones
        filas = []
        for fila in botones:
            fila_botones = []
            for boton in fila:
                # Botón especial para "="
                if boton == "=":
                    fila_botones.append(
                        ft.Container(
                            content=ft.ElevatedButton(
                                text=boton,
                                bgcolor=ft.colors.ORANGE_600,
                                color=ft.colors.WHITE,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=10)
                                ),
                                on_click=self._manejar_click  # Evento clic
                            ),
                            expand=True  # Ocupar espacio disponible
                        )
                    )
                else:
                    fila_botones.append(
                        self._crear_boton(boton)
                    )
            # Crear fila con espaciado
            filas.append(
                ft.Row(fila_botones, spacing=5, expand=True)
            )
        # Devolver columna de filas
        return ft.Column(filas, spacing=5, expand=True)

    # === Método para Crear Botones ===
    def _crear_boton(self, valor):
        return ft.Container(
            content=ft.ElevatedButton(
                text=valor,
                bgcolor=ft.colors.BLUE_GREY_800,
                color=ft.colors.WHITE,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10)
                ),
                on_click=self._manejar_click  # Vincular evento
            ),
            expand=True,  # Ajuste automático de tamaño
            padding=5  # Espaciado alrededor del botón
        )

    # === Manejador de Eventos ===
    def _manejar_click(self, e):
        # Obtener texto del botón clickeado
        texto = e.control.text
        
        # === Lógica de la Calculadora ===
        if texto == "C":
            self.display.value = "0"  # Reiniciar display
        elif texto == "=":
            try:
                # Evaluar expresión matemática
                resultado = eval(self.display.value)
                self.display.value = str(resultado)
            except:
                self.display.value = "Error"  # Mostrar errores
        else:
            # Actualizar display con nuevos valores
            if self.display.value == "0" or self.display.value == "Error":
                self.display.value = texto
            else:
                self.display.value += texto
        
        # === Actualizar Interfaz ===
        # Documentación: https://flet.dev/docs/controls/control#update
        self.display.update()

# === Función Principal ===
def main(page: ft.Page):
    # === Configuración de la Página ===
    # Documentación: https://flet.dev/docs/controls/page
    page.title = "Calculadora Flet"  # Título de la ventana
    page.bgcolor = ft.colors.BLACK  # Fondo negro
    page.window_width = 400  # Ancho inicial
    page.window_height = 600  # Alto inicial
    
    # === Centrado de Contenido ===
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # === Agregar Calculadora a la Página ===
    page.add(
        ft.Container(
            content=Calculadora(),  # Instancia de nuestra clase
            width=page.window_width * 0.9,  # 90% del ancho
            bgcolor=ft.colors.BLUE_GREY_900,
            border_radius=15,
            padding=20
        )
    )

# === Ejecutar la Aplicación ===
# Documentación: https://flet.dev/docs/guides/python/application-lifecycle
if __name__ == "__main__":
    ft.app(main)  # Iniciar app con FastAPI