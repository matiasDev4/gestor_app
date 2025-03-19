import flet as ft
from flet import *
import pandas as pd


#variables

page: ft.Page
dir = Text("", size=15)
total_ventas = Text("", size=20, color="#4F9B55")
total_grabado = Text("", size=20, color="#4F9B55")
total_iva21 = Text("", size=20, color="#4F9B55")
total_iva10 = Text("", size=20, color="#4F9B55")

#funciones
def close(e):
    dlg_modal.open = False
    dlg_modal.update()

def on_dialog_result(e: ft.FilePickerResultEvent):
    #Itero sobre el archivo para obtener sus propiedades
     for x in e.files:
        #Le paso el valor nuevo al widget
        dir.value = f"Archivo actual: {x.name}"
        dir.update()
        try:
        #obtengo el tipo de extension del archivo
            extension = x.path.split(".")[1]
            if extension == "xlsx" or extension == "xls":
                try: 
                    datos = pd.read_excel(f"{x.path}")
                    ventas = datos["Total"].sum()
                    grabado = datos["IInterno"].sum()
                    iva21 = datos["IVA21"].sum()
                    iva10 = datos["IVA105"].sum()  
                    #Creo formato de numeros
                    formato_total = "{:0,.0f}".format(ventas)
                    formato_grabado = "{:0,.0f}".format(grabado)
                    formato_iva21 = "{:0,.0f}".format(iva21)
                    formato_iva10 = "{:0,.0f}".format(iva10)
                    #Le paso los nuevos valores a los widget
                    total_ventas.value = f"${formato_total}"
                    total_ventas.update()
                    total_grabado.value = f"${formato_grabado}"
                    total_grabado.update()
                    total_iva21.value = f"${formato_iva21}"
                    total_iva21.update()        
                    total_iva10.value = f"${formato_iva10}"
                    total_iva10.update()
                except Exception as e:
                    print(e)
            else:
                dlg_modal.open = True
                dlg_modal.update()       
        except Exception as e:
            pass


#page.overlay.append
file_picker = ft.FilePicker(on_result=on_dialog_result)
dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Ocurrio un error ❌"),
        content=ft.Text("Solo se permiten archivos de tipo xlsx o xls, intente con otro", color="red", size=16),
        actions=[
            ft.TextButton("Cerrar", on_click=close),
        ]
    )
Archivo_button = ft.Container(
    ft.Column([
        ft.Row(
        wrap=True,
        spacing=15,
        run_spacing=10,
        controls=[(
            ft.ElevatedButton(
                "Selecciona un archivo...",
                bgcolor="white",
                icon=ft.icons.UPLOAD,
                color="black",
                style=ft.ButtonStyle(
                    shape=ft.StadiumBorder(),
                    overlay_color="#D4D4D4",
                    shadow_color="black",
                    animation_duration=300,
                    elevation={"hovered": 200, "": 0}),
        on_click=lambda _: file_picker.pick_files(allow_multiple=False))  
    ),
    dir]
    ),
        ft.SafeArea(
            content=ft.Container(
                content=ft.Column(spacing=25, controls=[
                    ft.Row([
                        ft.Container(
                            ft.Text("Total ventas", size=25, color="white"),
                                ),total_ventas
                        ],
                        spacing=15),
                    ft.Row([
                        ft.Container(
                            ft.Text("Total Interno:", size=25, color="white"),
                                ),total_grabado
                        ],
                        spacing=15),
                    ft.Row([
                        ft.Container(
                            ft.Text("Total IVA 21:", size=25, color="white"),
                                ),total_iva21
                        ],
                        spacing=15),
                    ft.Row([
                        ft.Container(
                            ft.Text("Total IVA 10,5:", size=25, color="white"),
                                ),total_iva10
                        ],
                        spacing=15)]),
                margin=margin.only(30, 30, 0, 0)
                
        )
    )
    ]),
    margin=margin.only(80, 50, 0, 0),
        
)


