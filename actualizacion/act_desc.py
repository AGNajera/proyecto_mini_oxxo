from datetime import datetime
import db.conexion as Conn
import os


def cambio_desc(conexion):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZAR DESCRIPCIÓN DE UN PRODUCTO")
        conf = input("¿Desea continuar con el cambio de la descripción de un producto? (s/n): ")
        if conf.lower() == 'n':
            print("Cancelando actualización de descripción de un producto.")
            input("Presione cualquier tecla para continuar...")
            return
        elif conf.lower() == 's':
            encontrado = None
            id_producto = int(input("ID del producto a cambiar su descripción: "))
            if id_producto <= 0:
                print("El ID del producto debe ser mayor a 0.")
                input("Presione cualquier tecla para continuar...")
                return cambio_desc(conexion)
            cursor = conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
            print("Producto seleccionado de acuerdo al ID tecleado")
            for producto in cursor:
                encontrado = True
                print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: ${producto[2]}, Cantidad: {producto[3]}, Fecha: {producto[4]}")
                conf = ''
                conf = input("\n¿Desea cambiar el ID de este producto? (s/n): ")
                if conf.lower() == 'n':
                    print("No se ha realizado ningún cambio.")
                    input("Presione cualquier tecla para continuar...")
                    return cambio_desc(conexion)
                elif conf.lower() == 's':
                    desc_nuevo = input("Nueva descripción del producto: ")
                    fecha_ingreso = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    print(f"Fecha del actualización: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
                    cursor = conexion.execute(f"SELECT descripcion FROM productos WHERE descripcion = '{desc_nuevo}'")
                    if desc_nuevo == "" or desc_nuevo == " ":
                        print("La descripción del producto no puede estar vacia o contener un espacio en blanco")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_desc(conexion)
                    if cursor.fetchone():
                        print("La descripción tecleada no puede ser igual a una ya registrada previamente")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_desc(conexion)
                    else:
                        cursor = conexion.execute(
                            "UPDATE productos SET descripcion = ? WHERE id = ?",
                            (desc_nuevo, id_producto)
                        )
                        print("Descripción de producto actualizada.")
                        input("Presione cualquier tecla para continuar...")
                        conexion.commit()
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