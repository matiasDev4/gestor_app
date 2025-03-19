import flet as ft
import datetime
import sqlite3
from flet import *
from componentes.excel import Archivo_button
from componentes.tabla_datos import tabla, obtener_datos
from componentes.crud_datos import insertar_datos, eliminarTodo
from componentes.reutilizar import convert_int, check_empty_input, visual_decimal_generator, Texts_class
from database.db_sql import conn




#funciones

def cambio_data(e):
    input_picker.value.strftime('%d-%m-%Y')
    input_picker.update()
    

def guardar_datos(e):
    try:
        insertar_datos(
            nombre=nombre.value, 
            percepcion=check_empty_input(perc.value), 
            grabado=check_empty_input(grabado.value), 
            iva21=check_empty_input(iva21.value), 
            iva105=check_empty_input(iva10.value), 
            varios=check_empty_input(varios.value), 
            cigarrillo=check_empty_input(cigarrillo.value), 
            fecha=input_picker.value.strftime('%d-%m-%Y'))
        
        
    except Exception as e:
        message_error_tab.open = True
        message_error_tab.update()



input_picker = ft.DatePicker(
    value="",
    on_change=cambio_data,
    )


message_error_tab = ft.SnackBar(
    Text("Seleccione una fecha", color="white", size=18), 
    bgcolor="red",
    action="Cerrar",
    action_color="white",
    duration=1500,)


def change_data(e):
    data = add_sugg(e.control.value) 
    if e.control.value == "":
        autocom.controls.clear()
        autocom.update()
        
    

def submit(e):
    nombre.value = e.control.data
    nombre.update()

def enter(e):
    e.control.value = add_sugg(e.control.value)
    e.control.update()
    e.control.autofocus = True
    if e.control.value == "":
        autocom.controls.clear()
        autocom.update()


nombre = ft.TextField(label="Nombre", border_color="#A2A2A2", color="white",autocorrect=True, label_style=ft.TextStyle(color="white"), on_change=change_data, on_submit=enter, enable_suggestions=True)
perc = ft.TextField(label="Percepcion", border_color="#A2A2A2", color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white") ) 
iva10 = ft.TextField(label="IVA 10,5%", border_color="#A2A2A2", color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
grabado = ft.TextField(label="Impuesto Interno", border_color="#A2A2A2",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, color="white", label_style=ft.TextStyle(color="white"))
iva21 = ft.TextField(label="IVA 21%", border_color="#A2A2A2", color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
total= ft.TextField(label="Total", border_color="#A2A2A2", input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, color="white", label_style=ft.TextStyle(color="white"))
varios= ft.TextField(label="Total varios", border_color="#A2A2A2", input_filter=ft.InputFilter(regex_string=r"[0-9.,]"),on_change=visual_decimal_generator, color="white", label_style=ft.TextStyle(color="white"))
cigarrillo= ft.TextField(label="Total cigarrillos", border_color="#A2A2A2", input_filter=ft.InputFilter(regex_string=r"[0-9.,]"),on_change=visual_decimal_generator, color="white", label_style=ft.TextStyle(color="white"))


    
    

autocom = ft.ListView()
autocom.visible = False


def add_sugg(value):
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM compras")
    consult = cursor.fetchall()
    lista = []
    if not consult == "":
        autocom.visible = True
        autocom.update()
        for item in consult:
            if value in item["nombre"]:
                lista.append(item)
    if lista:
        autocom.controls.clear()
        for x in lista:  
            autocom.controls.append(TextButton(x["nombre"], data=x["nombre"], on_click=submit))
            autocom.update()
            value = x["nombre"]
            return value
    
    if value == "":
        autocom.controls.clear()
        autocom.update()
        
            

     
#formulario compras
form = ft.Container(
    content=ft.Row([
        ft.Column([
            ft.Container(
                ft.Column([
                    nombre,
                    ft.Container(
                        autocom,
                        width=200
                    )
                ]),
                margin=margin.only(0, 50, 0, 0)
            ),
            ft.Container(
                perc ,
                margin=margin.symmetric(vertical=20)
            ),
            ft.Container(
                varios ,
                margin=margin.symmetric(vertical=20)
            ),

            ft.Container(
                ft.ElevatedButton(
                    "Nuevo",
                    icon=ft.icons.ADD, 
                    color="white", 
                    bgcolor="green", 
                    style=ft.ButtonStyle(
                        shape=ft.StadiumBorder(),
                        overlay_color="#6FC16E",
                        shadow_color={"hovered": "black", "":""},
                        animation_duration=300,
                        elevation={"hovered": 200, "": 0}),
                    on_click=guardar_datos),
                margin=margin.only(20, 20, 0, 0)
            ),

            ]),
        ft.Column([
            ft.Container(
                iva21,
                margin=margin.only(0, 50, 0, 20)
            ),
            ft.Container(
                iva10,
                margin=margin.symmetric(vertical=20)
            ),
            ft.Container(
                cigarrillo ,
                margin=margin.symmetric(vertical=20)
            ),
            ]),
        ft.Column([
            ft.Container(
                grabado,
                margin=margin.only(0, 50, 0, 20)
            ),
            ft.Container(
                ft.ElevatedButton(
                    "Selecciona fecha", 
                    bgcolor="white",
                    color="black",
                    style=ft.ButtonStyle(
                        shape=ft.StadiumBorder(),
                        overlay_color="#D4D4D4",
                        shadow_color="black",
                        animation_duration=300,
                        elevation={"hovered": 200, "": 0}),
                    icon=ft.icons.CALENDAR_MONTH,
                    on_click=lambda e: input_picker.pick_date()), margin=margin.only(0, 25, 0, 0))
            ]),
        ],
        spacing=30), margin=margin.only(30, 0, 0, 0)

)


total_perc = Texts_class(value="$0", color="black", size=16, weight="bold")
total_iva21 = Texts_class(value="$0", color="black", size=16, weight="bold")
total_iva105 = Texts_class(value="$0", color="black", size=16, weight="bold")
total_grabado = Texts_class(value="$0", color="black", size=16, weight="bold")
total_varios = Texts_class(value="$0", color="black", size=16, weight="bold")
total_cigarrillo = Texts_class(value="$0", color="black", size=16, weight="bold")
total_articulos = Texts_class(value="0", color="black", size=16, weight="bold")
total_general = Texts_class(value="$0", color="black", size=16, weight="bold") 




def actualizar_suma(e):
    try:
        resultados_suma()
    except Exception as e:
        message_error_suma.open = True
        message_error_suma.update()

def resultados_suma():
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*), SUM(percepcion), SUM(iva21), SUM(iva105), SUM(grabado), SUM(varios), SUM(cigarrillo) FROM compras")
    result = cursor.fetchall()
    try:
        for i in result:
            if i["COUNT(*)"] >= 0:  
                total_perc.actualizar("${:,.2f}".format(float(i["SUM(percepcion)"])))
                total_grabado.actualizar("${:,.2f}".format(float(i["SUM(grabado)"])))
                total_iva21.actualizar("${:,.2f}".format(float(i["SUM(iva21)"])))
                total_iva105.actualizar("${:,.2f}".format(float(i["SUM(iva105)"])))
                total_varios.actualizar("${:,.2f}".format(float(i["SUM(varios)"])))
                total_cigarrillo.actualizar("${:,.2f}".format(float(i["SUM(cigarrillo)"])))
                total_general.actualizar("${:,.2f}".format(float(i["SUM(cigarrillo)"]) + float(i["SUM(varios)"])))
                total_articulos.actualizar(i["COUNT(*)"])
            elif i["COUNT(*)"] == 0:
                total_perc.actualizar("$0")
                total_grabado.actualizar("$0")
                total_iva21.actualizar("$0")
                total_iva105.actualizar("$0")
                total_varios.actualizar("$0")
                total_cigarrillo.actualizar("$0")
                total_articulos.actualizar("0")
    except Exception as e:
        print(e)   
        
message_error_suma = ft.SnackBar(
    Text("No hay datos para recargar", color="white", size=18), 
    bgcolor="red",
    action="Cerrar",
    action_color="white",
    duration=1500,)

def limpiar_tabla(e):
     eliminarTodo()
  
tab_menu  = Tabs(
    selected_index=0,
    indicator_padding=0,
    indicator_color="#EEA44C",
    label_color="#E1DE4C",
    unselected_label_color="white",
    animation_duration=300,
    
    tabs=[
        ft.Tab(
            text="Ingresar compras",
            content=form
        ),
        ft.Tab(
            "Calcular ventas",
            content=Archivo_button
        ),
        ft.Tab(
            "Datos guardados",

            content=ft.Column([
                ft.Container(ft.Column([ft.Container(tabla, width=1320)], scroll=ScrollMode.ALWAYS), height=400),
                
                ft.Container(
                    ft.Column([
                        ft.Row([
                            ft.Container(ft.Row([Text("Total percepcion:", color="black", size=13, weight="bold"), total_perc]), margin=margin.only(20,0,0,0)),
                            ft.Container(ft.Row([Text("Total IVA 21:", color="black", size=13, weight="bold"), total_iva21]), margin=margin.only(20,0,0,0)),
                            ft.Container(ft.Row([Text("Total IVA 10,5:", color="black", size=13, weight="bold"), total_iva105]), margin=margin.only(20,0,0,0)),
                            ft.Container(ft.Row([Text("Total IInterno:", color="black", size=13, weight="bold"), total_grabado]), margin=margin.only(20,0,0,0)),
                    ]),
                        ft.Row([
                            ft.Container(ft.Row([Text("Total varios:", color="black", size=13, weight="bold"), total_varios]), margin=margin.only(20,0,0,0)),
                            ft.Container(ft.Row([Text("Total cigarrillos:", color="black", size=13, weight="bold"), total_cigarrillo]), margin=margin.only(20,0,0,0)),
                            ft.Container(ft.Row([Text("Total general:", color="black", size=13, weight="bold"), total_general]), margin=margin.only(20,0,0,0)),
                            ft.Container(ft.Row([Text("Articulos:", color="black", size=13, weight="bold"), total_articulos]), margin=margin.only(20,0,0,0)),
                        ])
                    ])


                ,bgcolor="#B6B5B5", padding=10), 
                ft.Row([
                    ft.Container(ft.ElevatedButton(
                        "Recargar datos", 
                        bgcolor="#5D93BD",
                        color="black",
                        style=ft.ButtonStyle(
                            shape=ft.StadiumBorder(),
                            overlay_color="#98CAF1",
                            shadow_color="black",
                            animation_duration=300,
                            elevation={"hovered": 200, "": 0}),
                        on_click=actualizar_suma
                    )  , margin=margin.only(20, 10, 0, 0)
                ),
                    ft.Container(ft.ElevatedButton(
                        "Limpiar datos", 
                        bgcolor="white",
                        color="black",
                        style=ft.ButtonStyle(
                            shape=ft.StadiumBorder(),
                            overlay_color="#bdbdbd",
                            shadow_color="black",
                            animation_duration=300,
                            elevation={"hovered": 200, "": 0}),
                        on_click=limpiar_tabla
                    )  , margin=margin.only(20, 10, 0, 0)
                ),
                ], spacing=25)
            ]),
        )
    ])





