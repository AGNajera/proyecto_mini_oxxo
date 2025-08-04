import sqlite3
import db.conexion as Conn


def crear_tabla_productos():
    conexion = Conn.conexion_db()
    try:
        conexion.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL,
            fecha datetime NOT NULL
        )''')
        print("Tabla 'productos' creada exitosamente.")
    except sqlite3.OperationalError:
        print("La tabla 'productos' ya existe.")
    conexion.commit()
    conexion.close()
    return conexion


crear_tabla_productos()