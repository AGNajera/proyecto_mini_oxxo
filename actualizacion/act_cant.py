from datetime import datetime
import db.conexion as Conn
import os


def act_cantidad(conexion):
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZAR CANTIDAD DE UN PRODUCTO")
        conf = input("¿Desea continuar con la actualización de la cantidad de un producto? (s/n): ")
        if conf.lower() == 'n':
            print("Cancelando actualización de cantidad de un producto.")
            input("Presione cualquier tecla para continuar...")
            return
        elif conf.lower() == 's':
            encontrado = None
            id_producto = int(input("ID del producto a actualizar su cantidad: "))
            if id_producto <= 0:
                print("El ID del producto debe mayor a 0.")
                input("Presione cualquier tecla para continuar...")
                return act_cantidad(conexion)
            cursor = conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
            print("Producto seleccionado de acuerdo al ID tecleado")
            for producto in cursor:
                encontrado = True
                print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: ${producto[2]}, Cantidad: {producto[3]}, Fecha: {producto[4]}")
                conf = ''
                conf = input("\n¿Desea actualizar la cantidad de este producto? (s/n): ")
                if conf.lower() == 'n':
                    print("No se ha realizado ningún cambio.")
                    input("Presione cualquier tecla para continuar...")
                    return act_cantidad(conexion)
                elif conf.lower() == 's':
                    cant_nuevo = float(input("Nueva cantidad del producto: "))
                    fecha_ingreso = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    print(f"Fecha del actualización: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
                    cursor = conexion.execute(f"SELECT cantidad FROM productos WHERE cantidad = {cant_nuevo}")
                    if cant_nuevo == "" or cant_nuevo == " ":
                        print("La cantidad del producto no puede estar vacia o contener un espacio en blanco")
                        input("Presione cualquier tecla para continuar...")
                        return act_cantidad(conexion)
                    if cant_nuevo <=0:
                        print("La cantidad debe de ser mayor a 0")
                        input("Presione cualquier tecla para continuar...")
                        return act_cantidad(conexion)
                    else:
                        cursor = conexion.execute(
                            "UPDATE productos SET cantidad = cantidad + ?, fecha = ? WHERE id = ?",
                            (cant_nuevo, fecha_ingreso, id_producto)
                        )
                    print("Cantidad de producto actualizada.")
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
