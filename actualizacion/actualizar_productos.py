import os
import actualizacion.act_id as act_id
import actualizacion.act_desc as act_desc
import actualizacion.act_precio as act_precio
import actualizacion.act_cant as act_cant



def actualizar_producto(conexion):
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
            act_id.cambio_id(conexion)
        elif opcion == '2':
            act_desc.cambio_desc(conexion)
        elif opcion == '3':
            act_precio.cambio_precio(conexion)
        elif opcion == '4':
            act_cant.act_cantidad(conexion)
        elif opcion == '6':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida...")
            input("Presione cualquier tecla para intentar de nuevo...")
