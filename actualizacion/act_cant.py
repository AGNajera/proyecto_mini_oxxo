import datetime
import db.conexion as Conn
import os


def act_cantidad():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("ACTUALIZAR CANTIDAD DE UN PRODUCTO")
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
                return act_cantidad()
            cursor = Conn.conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
            print("Producto seleccionado de acuerdo al ID tecleado")
            for producto in cursor:
                encontrado = True
                print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: ${producto[2]}, Cantidad: {producto[3]}")
                conf = ''
                conf = input("\n¿Desea actualizar la cantidad de este producto? (s/n): ")
                if conf.lower() == 'n':
                    print("No se ha realizado ningún cambio.")
                    input("Presione cualquier tecla para continuar...")
                    return act_cantidad()
                elif conf.lower() == 's':
                    cant_nuevo = float(input("Nueva cantidad del producto: "))
                    fecha_ingreso = datetime.strptime(input("Fecha de ingreso del producto (Año-Mes-Día): "), "%Y-%m-%d")
                    cursor = Conn.conexion.execute(f"SELECT cantidad FROM productos WHERE cantidad = {cant_nuevo}")
                    if fecha_ingreso > datetime.now():
                        print("La fecha de ingreso no puede ser futura.")
                        input("Presione cualquier tecla para continuar...")
                        return act_cantidad()
                    if cant_nuevo == "" or cant_nuevo == " ":
                        print("La cantidad del producto no puede estar vacia o contener un espacio en blanco")
                        input("Presione cualquier tecla para continuar...")
                        return act_cantidad()
                    if cant_nuevo <=0:
                        print("El precio debe de ser mayor a 0")
                        input("Presione cualquier tecla para continuar...")
                        return act_cantidad()
                    else:
                        cursor = Conn.conexion.execute(
                            "UPDATE productos SET cantidad += ?, fecha = ? WHERE id = ?",
                            (cant_nuevo, fecha_ingreso, id_producto)
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