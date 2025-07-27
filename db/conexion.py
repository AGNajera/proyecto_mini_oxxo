import sqlite3


def conexion_db():
    conexion = sqlite3.connect('db/productos.db')
    return conexion