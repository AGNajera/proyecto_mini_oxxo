import os
import db.conexion as Conn


def consulta_de_producto():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("CONSULTA DE PRODUCTOS")
        print("Seleccione la opción deseada:")
        print("1.- Consultar todos los productos")
        print("2.- Consultar un producto específico por ID")
        print("3.- Volver al menú principal")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == '1':
            os.system("cls" if os.name == "nt" else "clear")
            print("PRODUCTOS REGISTRADOS:")
            cursor = Conn.conexion.execute("SELECT * FROM productos")
            for fila in cursor:
                print(f"ID: {fila[0]}, Descripción: {fila[1]}, Precio: {fila[2]}, Cantidad: {fila[3]}")
            input("Presione cualquier tecla para continuar...")

        elif opcion == '2':
            encontrado = None
            os.system("cls" if os.name == "nt" else "clear")
            id_producto = int(input("Ingrese el ID del producto a consultar: "))
            cursor = Conn.conexion.execute(f"SELECT id, descripcion, precio, cantidad FROM productos WHERE id={id_producto}")
            for producto in cursor:
                encontrado = True
                os.system("cls" if os.name == "nt" else "clear")
                print(f"ID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
                input("Presione cualquier tecla para continuar...")
            if not encontrado:
                print(f"No se encontró un producto con ID: '{id_producto}' .")
                input("Presione cualquier tecla para continuar...")
                continue

        elif opcion == '3':
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
