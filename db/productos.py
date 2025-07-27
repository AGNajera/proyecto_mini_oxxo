import sqlite3
import db.conexion as Conn


def crear_tabla_productos():
    Conn.conexion = Conn.conexion_db()
    try:
        Conn.conexion.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )''')
        print("Tabla 'productos' creada exitosamente.")
    except sqlite3.OperationalError:
        print("La tabla 'productos' ya existe.")
    Conn.conexion.commit()
    Conn.conexion.close()
    return Conn.conexion


crear_tabla_productos()