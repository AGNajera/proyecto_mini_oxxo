import os
import db.conexion as Conn
import datetime


def error_0():
    print("Debe de teclear un número mayor a 0.")
    input("Presione cualquier tecla para continuar...")
    return registro_de_producto()


def registro_de_producto():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        conf = input("¿Desea registrar un producto? (s/n): ")
        # Con lower da igual si el usuario escribe 'n' o 'N' el input lo pasa a minúscula
        if conf.lower() == 'n':
            print("Registro cancelado. Volviendo al menú principal...")
            break
        else:
            print("REGISTRO DE PRODUCTOS")
            id_producto = int(input("ID del producto: "))
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
                return registro_de_producto()
            precio = float(input("Precio del producto: "))
            if precio <= 0:
                error_0()
                return

            cantidad = int(input("Cantidad del producto: "))
            if cantidad <= 0:
                error_0()
                return
            if cantidad == "" or cantidad == " ":
                print("La cantidad del producto no puede estar vacía o contener un espacio en blanco.")
                input("Presione cualquier tecla para continuar...")
                return registro_de_producto()
            fecha_ingreso = datetime.strptime(input("Fecha de ingreso del producto (Año-Mes-Día): "), "%Y-%m-%d")
            if fecha_ingreso > datetime.now():
                print("La fecha de ingreso no puede ser futura.")
                input("Presione cualquier tecla para continuar...")
                return registro_de_producto()
            # Por si escribe cualquier cosa que no sea 's' o 'n'
            conf = ''
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
                Conn.conexion.commit()
                return id_producto, descripcion, precio, cantidad
            else:
                print("Opción no válida, por favor intente de nuevo.")
                input("Presione cualquier tecla para continuar...")
                continue
    Conn.conexion.close()
