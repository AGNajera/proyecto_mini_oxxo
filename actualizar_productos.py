import os
import db.conexion as Conn


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
                print("El ID del producto debe ser un número positivo.")
                input("Presione cualquier tecla para continuar...")
                return cambio_desc()
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
                    return cambio_desc()
                elif conf.lower() == 's':
                    id_nuevo = input("Nuevo ID del producto (Debe de ser > a 0 y no debe de coincidir con uno registrado): ")
                    cursor = Conn.conexion.execute(f"SELECT id FROM productos WHERE id = {id_nuevo}")
                    if id_producto <= 0:
                        print("El ID del producto debe ser un número positivo.")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_desc()
                    if cursor.fetchone():
                        print("El ID que tecleeó no puede ser el mismo que uno registrado previamente.")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_desc()
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


def cambio_desc():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZAR ID DEL PRODUCTO")
        conf = input("¿Desea continuar con el cambio de la descripción de un producto? (s/n): ")
        if conf.lower() == 'n':
            print("Cancelando actualización de descripción de un producto.")
            input("Presione cualquier tecla para continuar...")
            return
        elif conf.lower() == 's':
            encontrado = None
            id_producto = int(input("ID del producto a cambiar su descripción: "))
            if id_producto <= 0:
                print("El ID del producto debe ser un número positivo.")
                input("Presione cualquier tecla para continuar...")
                return cambio_desc()
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
                    return cambio_desc()
                elif conf.lower() == 's':
                    desc_nuevo = input("Nueva descripción del producto: ")
                    cursor = Conn.conexion.execute(f"SELECT descripcion FROM productos WHERE descripcion = '{desc_nuevo}'")
                    if desc_nuevo == "" or desc_nuevo == " ":
                        print("La descripción del producto no puede estar vacia o contener un espacio en blanco")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_desc()
                    if cursor.fetchone():
                        print("La descripción tecleada no puede ser igual a una ya registrada previamente")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_desc()
                    else:
                        cursor = Conn.conexion.execute(
                            "UPDATE productos SET descripcion = ? WHERE id = ?",
                            (desc_nuevo, id_producto)
                        )
                        print("Descripción de producto actualizada.")
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


def actualizar_producto():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZACIÓN DE PRODUCTOS")
        print("Seleccione la opción deseada:")
        print("1.- Actualizar ID de un producto")
        print("2.- Actualizar descripción de un producto")
        print("3.- Actualizar precio de un producto")
        print("4.- Actualizar cantidad de un producto")
        print("5.- Actualizar todo un producto")
        print("6.- Volver al menú principal")
        opcion = input("Ingrese el número de la opción: ")
        if opcion == '1':
            cambio_id()
        elif opcion == '2':
            cambio_desc()
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida...")
            input("Presione cualquier tecla para intentar de nuevo...")
