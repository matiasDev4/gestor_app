import sqlite3
from flet import *

from database.db_sql import conn
import flet as ft
from componentes.reutilizar import miSnakBar, Texts_class

def resetInsert():
    from componentes.tabs import nombre, perc, iva21, iva10, grabado, varios, cigarrillo
    nombre.value = ""
    nombre.update()
    perc.value = ""
    perc.update()
    iva21.value = ""
    iva21.update()
    iva10.value = ""
    iva10.update()
    grabado.value = ""
    grabado.update()
    varios.value = ""
    varios.update()
    cigarrillo.value = ""
    cigarrillo.update()
    

def insertar_datos(
    nombre: str,
    percepcion: float,
    grabado: float,
    iva21: float,
    iva105: float,
    varios: float,
    cigarrillo: float,
    fecha: float,
    ):
    from componentes.tabla_datos import obtener_datos
    from componentes.tabla_datos import tabla
    from componentes.tabs import tab_menu, resultados_suma
    
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO compras(nombre, percepcion, iva21, iva105, grabado, varios, cigarrillo, fecha) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
        (nombre, percepcion.replace(",", ""), iva21.replace(",", ""), iva105.replace(",", ""), grabado.replace(",", ""), varios.replace(",", ""), cigarrillo.replace(",", ""), fecha))
        conn.commit()
        tabla.rows.clear()
        obtener_datos()
        resultados_suma()
        tab_menu.update()
        tabla.update()
        resetInsert()

        message_success.activate()
        
    except Exception as e:
        print(e)



def editar_Datos(
    nombre: str,
    percepcion: float,
    grabado: float,
    iva105: float,
    iva21: float,
    varios: float,
    cigarrillo: float,
    fecha: str,
    id: int,
):
    from componentes.tabla_datos import obtener_datos
    from componentes.tabla_datos import tabla
    from componentes.tabs import tab_menu, resultados_suma
    try:

        cursor = conn.cursor()
        cursor.execute("UPDATE compras SET nombre=?, percepcion=?, iva21=?, iva105=?, grabado=?, varios=?, cigarrillo=?, fecha=? WHERE id=?",
                       (nombre, percepcion , iva21, iva105 , grabado, varios, cigarrillo, fecha, id))
        conn.commit()

        tabla.rows.clear()
        tab_menu.update()
        obtener_datos()
        resultados_suma()
        tabla.update()
        message_success.activate()
    except Exception as e:
        print(e)
    
    
def eliminarDatos(
    id: int,
):
    from componentes.tabla_datos import obtener_datos
    from componentes.tabla_datos import tabla
    from componentes.tabs import tab_menu, resultados_suma
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM compras WHERE id=?",(id,))
        conn.commit()
        tabla.rows.clear()
        obtener_datos()
        tabla.update()
        resultados_suma()
        tab_menu.update()
        message_delete.activate()
    except Exception as e:
        message_error_count_data.activate()

def eliminarTodo():
    from componentes.tabla_datos import obtener_datos
    from componentes.tabla_datos import tabla
    from componentes.tabs import tab_menu, resultados_suma
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM compras")
        conn.commit()
        tabla.rows.clear()
        obtener_datos()
        tabla.update()
        resultados_suma()
        tab_menu.update()
        message_all_delete.activate()
    except Exception as e:
        pass

message_success = miSnakBar(
    text="Datos guardados correctamente",
    size=18,
    color="white",
    bgcolor="green",
    action="Cerrar",
    action_color="white",
    duration=1500, open=False)

message_delete= miSnakBar(
    text="Dato eliminado correctamente!",
    size=18,
    color="white",
    bgcolor="blue",
    action="Cerrar",
    action_color="white",
    duration=1500, open=False)

message_error_count_data = miSnakBar(
    text="No hay datos para borrar!",
    size=18,
    color="white",
    bgcolor="red",
    action="Cerrar",
    action_color="white",
    duration=1500, open=False)

message_all_delete = miSnakBar(
    text="Todos los datos fueron eliminados!",
    size=18,
    color="white",
    bgcolor="gray",
    action="Cerrar",
    action_color="white",
    duration=1500, open=False)

    