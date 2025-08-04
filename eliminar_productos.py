import os
from datetime import datetime


def eliminar(conexion):
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        conf = input("¿Desea eliminar un producto? (s/n): ")
        if conf.lower() == 'n':
            print("Registro cancelado. Volviendo al menú principal...")
            break
        elif conf.lower() == 's':
            print("ELIMINACIÓN DE UN PRODUCTO")
            encontrado = None
            id_producto = int(input("ID del producto a eliminar: "))
            if id_producto <= 0:
                print("Debe de teclear un número mayor a 0.")
                input("Presione cualquier tecla para continuar...")
                return
            cursor = conexion.execute(f"SELECT * FROM productos WHERE id = {id_producto}")
            print("Producto seleccionado de acuerdo al ID tecleado")
            for producto in cursor:
                encontrado = True
                print(f"\nID: {producto[0]}, Descripción: {producto[1]}, Precio: ${producto[2]}, Cantidad: {producto[3]}, Fecha: {producto[4]}")
                conf = ''
                conf = input("\n¿Desea eliminar este producto? (s/n): ")
                if conf.lower() == 'n':
                    print("No se ha realizado ningún cambio.")
                    input("Presione cualquier tecla para continuar...")
                    return eliminar(conexion)
                elif conf.lower() == 's':
                    fecha_ingreso = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    print(f"Fecha de eliminación: {fecha_ingreso}")
                    cursor = conexion.execute(f"DELETE FROM productos WHERE id = {id_producto}")
                    print("Producto eliminado.")
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
