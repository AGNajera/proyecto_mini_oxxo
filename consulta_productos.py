import os
import productos as p


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
            p.conexion = p.conexion_db()
            cursor = p.conexion.execute("SELECT * FROM productos")
            for fila in cursor:
                print(f"ID: {fila[0]}, Descripción: {fila[1]}, Precio: {fila[2]}, Cantidad: {fila[3]}")
            input("Presione cualquier tecla para continuar...")

        elif opcion == '2':
            encontrado = None
            id_producto = int(input("Ingrese el ID del producto a consultar: "))
            p.conexion = p.conexion_db()
            cursor = p.conexion.execute(f"SELECT id, descripcion, precio, cantidad FROM productos WHERE id={id_producto}")
            for producto in cursor:
                encontrado = True
                os.system("clear")
                print(f"ID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
                input("Presione cualquier tecla para continuar...")
            if not encontrado:
                print(f"No se encontró un producto con ID {id_producto}.")
                input("Presione cualquier tecla para continuar...")
                p.conexion.close()
                continue
            if id_producto <= 0:
                print("El ID del producto debe ser un número entero positivo.")
                input("Presione cualquier tecla para continuar...")
                continue

        elif opcion == '3':
            print("Volviendo al menú principal...")
            break
            p.conexion.close()

        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
