import db.conexion as Conn
import os


def cambio_id():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZAR ID DEL PRODUCTO")
        conf = input("¿Desea cambiar algún ID? (s/n): ")
        if conf.lower() == 'n':
            print("Cancelando actualización de ID del producto.")
            input("Presione cualquier tecla para continuar...")
            return
        elif conf.lower() == 's':
            encontrado = None
            id_producto = int(input("ID del producto a cambiar: "))
            if id_producto <= 0:
                print("El ID del producto debe ser mayor a 0.")
                input("Presione cualquier tecla para continuar...")
                return cambio_id()
            cursor = Conn.conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
            print("Producto seleccionado de acuerdo al ID tecleado")
            for producto in cursor:
                encontrado = True
                print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
                conf = ''
                conf = input("\n¿Desea cambiar el ID de este producto? (s/n): ")
                if conf.lower() == 'n':
                    print("No se ha realizado ningún cambio.")
                    input("Presione cualquier tecla para continuar...")
                    return cambio_id()
                elif conf.lower() == 's':
                    id_nuevo = input("Nuevo ID del producto (Debe de ser > a 0 y no debe de coincidir con uno registrado): ")
                    cursor = Conn.conexion.execute(f"SELECT id FROM productos WHERE id = {id_nuevo}")
                    if id_producto <= 0:
                        print("El ID del producto debe ser un número positivo.")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_id()
                    if cursor.fetchone():
                        print("El ID que tecleeó no puede ser el mismo que uno registrado previamente.")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_id()
                    else:
                        cursor = Conn.conexion.execute(f"UPDATE productos SET id = {id_nuevo} WHERE id = {id_producto}")
                        print("ID de producto actualizado.")
                        input("Presione cualquier tecla para continuar...")
                        Conn.conexion.commit()
                        return
                else:
                    print("Opción no válida, por favor intente de nuevo.")
                    input("Presione cualquier tecla para continuar...")
                    continue
            if not encontrado:
                print(f"No se encontró un producto con ID: '{id_producto}' .")
                input("Presione cualquier tecla para continuar...")
                continue
        else:
            print("Opción no válida, por favor intente de nuevo.")
            input("Presione cualquier tecla para continuar...")
            continue