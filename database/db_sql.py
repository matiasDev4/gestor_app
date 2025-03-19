from pathlib import Path
import sys
import sqlite3
import os

dir_path = os.path.join(os.environ['APPDATA'], 'gestor_app')
if not os.path.exists(dir_path):
     os.makedirs(dir_path)
file_path = os.path.join(dir_path, 'kv.db')
conn = sqlite3.connect(file_path, check_same_thread=False)
    

def crearte_table_compras():
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compras(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        percepcion REAL ,
        iva21 REAL ,
        iva105 REAL ,
        grabado REAL ,
        varios REAL ,
        cigarrillo REAL ,
        fecha TEXT)
    """)
    conn.commit()










    






    

    
    
    
    