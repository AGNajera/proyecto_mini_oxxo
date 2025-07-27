import os
import db.conexion as Conn


def error_0():
    Conn.conexion = Conn.conexion_db()
    print("Debe de teclear un número entero positivo")
    input("Presione cualquier tecla para continuar...")
    return registro_de_producto()


def registro_de_producto():
    conf = ''
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        confirmacion = input("¿Desea registrar del producto? (s/n): ")
        # Con lower da igual si el usuario escribe 'n' o 'N' el input lo pasa a minúscula
        if confirmacion.lower() == 'n':
            print("Registro cancelado. Volviendo al menú principal...")
            break
        else:
            print("REGISTRO DE PRODUCTOS")
            id_producto = int(input("ID del producto: "))
            Conn.conexion = Conn.conexion_db()
            if id_producto <= 0:
                error_0()
                continue
            for id in Conn.conexion.execute("SELECT id FROM productos"):
                if id_producto == id[0]:
                    print("El ID del producto ya existe. Por favor, ingrese un ID único.")
                    input("Presione cualquier tecla para continuar...")
                    return registro_de_producto()

            descripcion = input("Descripción del producto: ")
            for desc in Conn.conexion.execute("SELECT descripcion FROM productos"):
                if descripcion == desc[0]:
                    print("Este producto ya existe. Por favor, ingrese una descripción única.")
                    input("Presione cualquier tecla para continuar...")
                    return registro_de_producto()
            if descripcion == "" or descripcion == " ":
                print("La descripción del producto no puede estar vacía.")
                input("Presione cualquier tecla para continuar...")
                continue

            precio = float(input("Precio del producto: "))
            if precio <= 0:
                error_0()
                return

            cantidad = int(input("Cantidad del producto: "))
            if cantidad <= 0:
                error_0()
                return
            # Por si escribe cualquier cosa que no sea 's' o 'n'
            while conf.lower() not in ['s', 'n']:
                conf = input("Está seguro de registrar este producto? (s/n): ")
                if conf.lower() == 'n':
                    print("Registro cancelado. Volviendo al menú principal...")
                    break
                elif conf.lower() == 's':
                    Conn.conexion.execute('''
                    INSERT INTO productos (id, descripcion, precio, cantidad)
                    VALUES (?, ?, ?, ?)
                    ''', (id_producto, descripcion, precio, cantidad))
                    print("Producto registrado exitosamente:")
                    input("Presione cualquier tecla para continuar...")
                    return id_producto, descripcion, precio, cantidad