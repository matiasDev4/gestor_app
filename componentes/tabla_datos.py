import flet as ft
from flet import * 
import sqlite3
from componentes.crud_datos import editar_Datos, eliminarDatos
from componentes.reutilizar import convert_int
from componentes.reutilizar import convert_float, convert_int, visual_decimal_generator, check_data
from database.db_sql import conn





def cambio_data(e):
    input_picker2.value.strftime('%d-%m-%Y')
    input_picker2.update()

input_picker2 = ft.DatePicker(
    on_change=cambio_data,
    
    )


tabla = ft.DataTable(
    columns=[
        DataColumn(label=Text("Acciones", color="white")),
        DataColumn(label=Text("Nombre", color="white")),
        DataColumn(label=Text("Percepcion", color="white")),
        DataColumn(label=Text("IInterno",color="white")),
        DataColumn(label=Text("IVA 21",color="white")),
        DataColumn(label=Text("IVA 10,5", color="white")),
        DataColumn(label=Text("Total varios",color="white")),
        DataColumn(label=Text("Total cigarrillo",color="white")),
        DataColumn(label=Text("Fecha",color="white")),], 
    rows=[]
    )
def eliminar(e):
    data = e.control.data
    get_id = data["id"]
    if check_data(get_id) == "1":
        eliminarDatos(get_id)
        
    

def obtener_datos():
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compras")
    query = cursor.fetchall()
    if not query == "":
        for i in query:
            tabla.rows.append(
                DataRow([
                    DataCell(
                        ft.Row([
                            ft.IconButton(
                                icon=ft.icons.EDIT,
                                on_click=editar,
                                icon_color="#9FC1F1",
                                data=i
                                ),
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color="#9FC1F1",
                                on_click=eliminar,
                                data=i)
                        ], spacing=30)
                    ),
                    DataCell(Text(i["nombre"], color="white")),
                    DataCell(Text(convert_float(int(i["percepcion"])), color="white")),
                    DataCell(Text(convert_float(int(i["grabado"])), color="white")),
                    DataCell(Text(convert_float(int(i["iva21"])), color="white")),
                    DataCell(Text(convert_float(int(i["iva105"])), color="white")),
                    DataCell(Text(convert_float(int(i["varios"])), color="white")),
                    DataCell(Text(convert_float(int(i["cigarrillo"])), color="white")),
                    DataCell(Text(i["fecha"], color="white"))
                ])
            )
            
    cursor.close()
    


    
def cerrar_dlg(e):
    dlg_edit.offset = transform.Offset(2,0)
    dlg_edit.update()
    
def guardar_datos(e):
    editar_Datos(
        nombre=nombre_nuevo.value, 
        percepcion=convert_int(perc_nuevo.value), 
        grabado=convert_int(grabado_nuevo.value), 
        iva105=convert_int(iva10_nuevo.value), 
        iva21=convert_int(iva21_nuevo.value), 
        varios=convert_int(varios_nuevo.value), 
        cigarrillo=convert_int(cigarrillo_nuevo.value), 
        fecha=fecha_nuevo.value, 
        id=id_row.value)
    
    dlg_edit.offset = transform.Offset(2,0)
    dlg_edit.update()
    
    
def editar(e):
    data = e.control.data
    id_row.value = data["id"]
    nombre_nuevo.value = data['nombre']
    grabado_nuevo.value = convert_float(data['grabado'])
    perc_nuevo.value = convert_float(data["percepcion"])
    iva10_nuevo.value = convert_float(data['iva105'])
    iva21_nuevo.value = convert_float(data['iva21'])
    varios_nuevo.value = convert_float(data['varios'])
    cigarrillo_nuevo.value = convert_float(data['cigarrillo'])
    fecha_nuevo.value = data["fecha"]
    
    dlg_edit.offset = transform.Offset(0,0)
    dlg_edit.update()
 



 
id_row = Text()       
nombre_nuevo = ft.TextField(label="Nombre", border_color="#A2A2A2", color="white", label_style=ft.TextStyle(color="white"))
perc_nuevo = ft.TextField(label="Percepcion", border_color="#A2A2A2",  color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
iva10_nuevo = ft.TextField(label="IVA 10,5%", border_color="#A2A2A2", color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
grabado_nuevo = ft.TextField(label="Impuesto Interno", border_color="#A2A2A2",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, color="white", label_style=ft.TextStyle(color="white"))
iva21_nuevo = ft.TextField(label="IVA 21%", border_color="#A2A2A2",  color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
varios_nuevo = ft.TextField(label="Total varios", border_color="#A2A2A2",  color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
cigarrillo_nuevo = ft.TextField(label="Total cigarrillo", border_color="#A2A2A2",  color="white",input_filter=ft.InputFilter(regex_string=r"[0-9.,]"), on_change=visual_decimal_generator, label_style=ft.TextStyle(color="white"))
fecha_nuevo = ft.TextField(label="Fecha", border_color="#A2A2A2", color="white", label_style=ft.TextStyle(color="white"))


dlg_edit = Card(
    margin=margin.only(250, 80, 0, 0),
    offset= transform.Offset(2, 0),
    color="#1A2A42",
    animate_offset= animation.Animation(400, "ease all"),
        content=ft.Container(
            ft.Row([

                ft.Column([
                ft.Container(
                        ft.Text("Editar datos", text_align=TextAlign.CENTER, size=20, color="white"),margin=margin.only(0, 30, 0, 0)
                ),
                    ft.Container(
                        nombre_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                    ft.Container(
                        perc_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                    ft.Container(
                        iva10_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                    ft.Container(
                        varios_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                    ft.Container(
                        ft.ElevatedButton(
                            "Guardar", 
                            on_click=guardar_datos,
                            icon=ft.icons.ADD, 
                            color="white", 
                            bgcolor="green", 
                            style=ft.ButtonStyle(
                                shape=ft.StadiumBorder(),
                                overlay_color="#6FC16E",
                                shadow_color={"hovered": "black", "":""},
                                animation_duration=300,
                                elevation={"hovered": 200, "": 0}),
                ), margin=margin.only(10, 40, 0, 0))
                ]),
                ft.Column([
                    ft.Container(
                            ft.IconButton(
                                icon=ft.icons.CLOSE, 
                                icon_color="white",
                                bgcolor="#C25C5C",
                                on_click=cerrar_dlg,
                                style=ft.ButtonStyle(shape=ft.CircleBorder())
                                ),margin=margin.only(280, 20, 0, 0)),
                    ft.Container(
                        iva21_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                    ft.Container(
                        grabado_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                    ft.Container(
                        fecha_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                        
                    ),
                    ft.Container(
                        cigarrillo_nuevo,
                        margin=margin.only(0, 30, 0, 0)
                    ),
                ]),
            ], spacing=30),
            width=700,
            height=500,
            margin=margin.only(60, 0, 0, 0), bgcolor="#1A2A42"),
            
    )


    