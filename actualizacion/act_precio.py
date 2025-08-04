from datetime import datetime
import os


def cambio_precio(conexion):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZAR PRECIO DE UN PRODUCTO")
        conf = input("¿Desea continuar con el cambio de precio de un producto? (s/n): ")
        if conf.lower() == 'n':
            print("Cancelando actualización de precio de un producto.")
            input("Presione cualquier tecla para continuar...")
            return
        elif conf.lower() == 's':
            encontrado = None
            id_producto = int(input("ID del producto a cambiar su descripción: "))
            if id_producto <= 0:
                print("El ID del producto debe mayor a 0.")
                input("Presione cualquier tecla para continuar...")
                return cambio_precio(conexion)
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
                    return cambio_precio(conexion)
                elif conf.lower() == 's':
                    precio_nuevo = float(input("Nuevo precio del producto: "))
                    fecha_ingreso = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    print(f"Fecha del actualización: {fecha_ingreso}")
                    cursor = conexion.execute(f"SELECT precio FROM productos WHERE precio = {precio_nuevo}")
                    if precio_nuevo == "" or precio_nuevo == " ":
                        print("El precio del producto no puede estar vacio o contener un espacio en blanco")
                        input("Presione cualquier tecla para continuar...")
                        return cambio_precio(conexion)
                    if precio_nuevo <=0:
                        print("El precio debe de ser mayor a 0")
                    else:
                        cursor = conexion.execute(
                            "UPDATE productos SET precio = ? WHERE id = ?",
                            (precio_nuevo, id_producto)
                        )
                    print("Descripción de producto actualizada.")
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
