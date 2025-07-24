import sqlite3


def conexion_db():
    conexion = sqlite3.connect('productos.db')
    return conexion


def crear_tabla_productos():
    conexion = conexion_db()
    try:
        conexion.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )''')
        print("Tabla 'productos' creada exitosamente.")
    except sqlite3.OperationalError:
        print("La tabla 'productos' ya existe.")
    conexion.commit()
    conexion.close()
    return conexion


conexion_db()
crear_tabla_productos()
