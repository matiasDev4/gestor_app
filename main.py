
import flet as ft
from flet import *
import datetime
from componentes.tabs import tab_menu, input_picker, message_error_tab, message_error_suma, resultados_suma, nombre
from componentes.excel import file_picker, dlg_modal
from componentes.tabla_datos import obtener_datos, dlg_edit, input_picker2
from componentes.crud_datos import message_delete, message_error_count_data, message_success
from componentes.reutilizar import Texts_class, miSnakBar
from database.db_sql import crearte_table_compras, conn




def main(page: ft.Page):
    #configuracion ventana
    page.window.maximizable = False
    page.title="Gestor de compras MYM"
    page.window.max_width = 1320
    page.window.height = 800
    page.window.max_height = 800
    page.window.min_width = 680
    page.window.center()
    page.bgcolor="#1a1a1a"
    page.padding = 0
    
    #funciones 
           
    def comprobar():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM compras")
        result = cursor.fetchall()
        if result == []:
            pass
        else:
            obtener_datos()
            
    comprobar()
   
    
    
    #controls variables
    body_top=ft.Container(
        ft.Text("Administrador de facturas", text_align="center", size=30, color="white"),
        width=1320,
        height=100,
        padding=padding.only(0, 30, 0, 0),
        
    )
    body_tabs=ft.Container(
        tab_menu,
        width=page.window.width,
        height=600,
        margin=margin.only(0, 50, 0, 0)
    )
    

    #add controls
    page.overlay.append(input_picker)
    page.overlay.append(input_picker2)
    page.overlay.append(file_picker)
    page.overlay.append(dlg_modal)
    page.overlay.append(message_error_tab)
    page.overlay.append(message_error_suma)
    page.overlay.append(message_delete)
    page.overlay.append(dlg_edit)
    page.overlay.append(message_error_count_data)
    page.overlay.append(message_success)
    
    

    

    page.add(body_top)
    page.add(body_tabs)
    
    page.update()
    

if __name__=="__main__":
    crearte_table_compras()
    ft.app(target=main)
