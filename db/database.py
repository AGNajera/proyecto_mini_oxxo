import sqlite3

def conexion_db():
    return sqlite3.connect('db/database.db')


conexion = conexion_db()
cursor = conexion.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    precio REAL NOT NULL,
    cantidad INTEGER NOT NULL,
    fecha TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS venta_maestro (
    folio_venta INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_venta TEXT NOT NULL,
    clave_cliente INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS venta_detalle (
    folio_ventaD INTEGER,
    producto_id INTEGER NOT NULL,
    cantidad_venta INTEGER NOT NULL,
    precio_venta REAL NOT NULL,
    FOREIGN KEY(producto_id) REFERENCES productos(id)
)
''')
conexion.commit()
conexion.close()