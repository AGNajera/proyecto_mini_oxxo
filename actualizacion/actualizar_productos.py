import os
import db.conexion as Conn
import act_id
import act_desc 
import act_precio


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
            act_id.cambio_id()
        elif opcion == '2':
            act_desc.cambio_desc()
        elif opcion == '3':
            act_precio.cambio_precio()
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida...")
            input("Presione cualquier tecla para intentar de nuevo...")
