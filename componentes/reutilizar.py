from typing import Any, List, Callable, Dict, Tuple
from flet import *
import flet as ft
from flet_core.protocol import Command
from database.db_sql import conn

import sqlite3

# ------CLASES------


#Control personalizado para crear Control: Text()
class Texts_class(ft.Text):
    def _get_control_name(self) -> str:
        return super()._get_control_name()
    
    def __init__(self, value: str | None = None, spans: List[TextSpan] | None = None, text_align: ft.TextAlign | None = None, font_family: str | None = None, size: int | float | None = None, weight: ft.FontWeight | None = None, italic: bool | None = None, style: ft.TextThemeStyle | ft.TextStyle | None = None, theme_style: ft.TextThemeStyle | None = None, max_lines: int | None = None, overflow: ft.TextOverflow | None = None, selectable: bool | None = None, no_wrap: bool | None = None, color: str | None = None, bgcolor: str | None = None, semantics_label: str | None = None, ref: ft.Ref | None = None, key: str | None = None, width: int | float | None = None, height: int | float | None = None, left: int | float | None = None, top: int | float | None = None, right: int | float | None = None, bottom: int | float | None = None, expand: None | bool | int = None, expand_loose: bool | None = None, col: Dict[str, int | float] | int | float | None = None, opacity: int | float | None = None, rotate: int | float | ft.Rotate | None = None, scale: int | float | ft.Scale | None = None, offset: ft.Offset | Tuple[float | int, float | int] | None = None, aspect_ratio: int | float | None = None, animate_opacity: bool | int | ft.Animation | None = None, animate_size: bool | int | ft.Animation | None = None, animate_position: bool | int | ft.Animation | None = None, animate_rotation: bool | int | ft.Animation | None = None, animate_scale: bool | int | ft.Animation | None = None, animate_offset: bool | int | ft.Animation | None = None, on_animation_end: Callable[[ControlEvent], None] | None = None, tooltip: str | None = None, visible: bool | None = None, disabled: bool | None = None, data: Any = None, rtl: bool | None = None):
        super().__init__(value, spans, text_align, font_family, size, weight, italic, style, theme_style, max_lines, overflow, selectable, no_wrap, color, bgcolor, semantics_label, ref, key, width, height, left, top, right, bottom, expand, expand_loose, col, opacity, rotate, scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation, animate_scale, animate_offset, on_animation_end, tooltip, visible, disabled, data, rtl)
    
    def actualizar(self, new):
        self.value = new
        self.update()
        

class miSnakBar(ft.SnackBar):
    def __init__(self, text: str, color: str, size: int, bgcolor: str, action: str, action_color: str, duration: int, open: bool):
        super().__init__(text, bgcolor, action, action_color, duration, open)
        self.control_text = Texts_class(value=text, size=size, color=color)
        self.content = self.control_text
        self.bgcolor = bgcolor
        self.action = action
        self.action_color = action_color,
        self.duration = duration
    
    def _build_add_commands(self, indent: int = 0, index=None, added_controls=None) -> List[Command]:
        return super()._build_add_commands(indent, index, added_controls)
    
    def activate(self):
        self.open = True
        self.update()
    
    def overray(self, page):
        page.overlay.append(self)
        page.update()
        
        
# ------FUNCIONES------

# convierte valores flotantes en enteros
def convert_int(value):  
    convert = str(value).replace(",","")
    return convert


# Darle efecto visual de decimales al input
def visual_decimal_generator(e): 
    data = e.control.value.replace(",","")
    if data.isdigit():
        e.control.value = f"{int(data):,}"
        e.control.update()
        
#convierte los valores en decimales
def convert_float(value):
    convert = "{:,.2f}".format(float(value))
    return convert

#verifica si el input se envio vacio y le da un valor por defecto "0,"
def check_empty_input(value):
    if value == "":
        return "0,"
    return value


def check_data(value):
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM compras WHERE id=?",(value,))
    if cursor.fetchone():
        return "1"


        


    


