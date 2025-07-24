import os
import productos as p
import registro_productos as r
import consulta_productos as c
import actualizar_productos as a


def principal():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("Seleccione la opción deseada:")
        print("1.- Registrar un producto")
        print("2.- Consultar un producto")
        print("3.- Actualizar un producto")
        print("4.- Eliminar un producto")
        print("5.- Salir")
        opcion = input("Ingrese el número de la opción: ")
        if opcion == "1":
            r.registro_de_producto()
            input("Presione cualquier tecla para continuar...")
        elif opcion == "2":
            c.consulta_de_producto()
            input("Presione cualquier tecla para continuar...")
        elif opcion == "3":
            a.actualizar_producto()
        elif opcion == "5":
            print("Saliendo del programa...")
            p.conexion_db().close()
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione cualquier tecla para continuar...")


if __name__ == "__main__":
    principal()
