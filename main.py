import os
import registro_productos as r
import consulta_productos as c
import actualizacion.actualizar_productos as a
import eliminar_productos as e
import db.database as Conn


def principal():
    conexion = Conn.conexion_db()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Seleccione la opción deseada:")
        print("1.- Registrar un producto")
        print("2.- Consultar un producto")
        print("3.- Actualizar un producto")
        print("4.- Eliminar un producto")
        print("5.- Salir")
        opcion = input("Ingrese el número de la opción: ")
        try:
            if opcion == "1":
                r.registro_de_producto(conexion)
                input("Presione cualquier tecla para continuar...")
            elif opcion == "2":
                c.consulta_de_producto(conexion)
                input("Presione cualquier tecla para continuar...")
            elif opcion == "3":
                a.actualizar_producto(conexion)
                input("Presione cualquier tecla para continuar...")
            elif opcion == "4":
                e.eliminar(conexion)
                input("Presione cualquier tecla para continuar...")
            elif opcion == "5":
                print("Saliendo del programa...")
                conexion.close()
                break
            else:
                print("Opción no válida...")
                input("Presione cualquier tecla para intentar de nuevo...")
        except ValueError:
            print("Debe ingresar el valor que se le indique. Intente de nuevo.")
            input("Presione cualquier tecla para intentar de nuevo...")
            continue


if __name__ == "__main__":
    principal()
