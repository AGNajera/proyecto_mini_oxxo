import os
import productos as p


def cambio_id():
    conf = ''
    confirmacion = ''
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        p.conexion = p.conexion_db()
        print("ACTUALIZAR ID DEL PRODUCTO")
        conf = input("¿Desea continuar con el cambio? (s/n): ")
        if conf.lower() == 's':
            id_producto = int(input("ID del producto a cambiar: "))
            if id_producto <= 0:
                print("El ID del producto debe ser un número positivo.")
                input("Presione cualquier tecla para continuar...")
                return
            for id in p.conexion.execute(f"SELECT id FROM productos WHERE id = {id_producto}"):
                if id_producto != id[0]:
                    print("Producto seleccionado de acuerdo al ID")
                    cursor = p.conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
                    for producto in cursor:
                        print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
                        while confirmacion.lower() not in ['s', 'n']:
                            confirmacion = input("\n¿Desea cambiar el ID de este producto? (s/n): ")
                            if confirmacion.lower() == 's':
                                id_nuevo = int(input("Nuevo ID del producto: "))
                                p.conexion.execute(f"UPDATE productos SET id = {id_nuevo} WHERE id = {id_producto}")
                                if id_nuevo <= 0:
                                    print("El ID del producto debe ser un número positivo.")
                                    input("Presione cualquier tecla para continuar...")
                                    return
                                if id_nuevo == id_producto:
                                    print("El nuevo ID no puede ser el mismo que el actual.")
                                    input("Presione cualquier tecla para continuar...")
                                    return
                                p.conexion.commit()
                                print(f"ID del producto actualizado a {id_nuevo}.")
                                input("Presione cualquier tecla para continuar...")
                                p.conexion.close()
                                return
                            elif confirmacion.lower() == 'n':
                                print("No se ha realizado ningún cambio.")
                                input("Presione cualquier tecla para continuar...")
                                p.conexion.close()
                                break
                            else:
                                print("Opción no válida, por favor intente de nuevo.")
                                input("Presione cualquier tecla para continuar...")
                                continue
                else:
                    print("ID de producto no existe, intente nuevamente.")
                    input("Presione cualquier tecla para continuar...")
                    break

        elif conf.lower() == 'n':
            print("Cancelando actualización de ID del producto.")
            input("Presione cualquier tecla para continuar...")
            p.conexion.close()
            break

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
