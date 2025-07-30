import os
import db.conexion as Conn


def cambio_id():
    conf = ''
    confirmacion = ''
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
                return cambio_id()
            cursor = Conn.conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
            print("Producto seleccionado de acuerdo al ID tecleado")
            for producto in cursor:
                encontrado = True
                print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
                while confirmacion.lower() not in ['s', 'n']:
                    confirmacion = input("\n¿Desea cambiar el ID de este producto? (s/n): ")
                    if confirmacion.lower() == 's':
                        id_nuevo = int(input("Nuevo ID del producto (Debe de ser > a 0 y no debe de coincidir con uno registrado): "))
                        cursor = Conn.conexion.execute(f"SELECT id FROM productos WHERE id = {id_nuevo}")
                        if id_nuevo <= 0:
                            print("El ID del producto debe ser un número positivo.")
                            input("Presione cualquier tecla para continuar...")
                            return cambio_id()
                        if cursor.fetchone():
                            print("El nuevo ID no puede ser el mismo que uno registrado previamente.")
                            input("Presione cualquier tecla para continuar...")
                            return cambio_id()
                        else:
                            cursor = Conn.conexion.execute(f"UPDATE productos SET id = {id_nuevo} WHERE id = {id_producto}")
                            print("ID de producto actualizado.")
                            input("Presione cualquier tecla para continuar...")
                            Conn.conexion.commit()
                            return actualizar_producto()
                    elif confirmacion.lower() == 'n':
                        print("No se ha realizado ningún cambio.")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_id()
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
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else: 
            print("Opción no válida...")
            input("Presione cualquier tecla para intentar de nuevo...")
