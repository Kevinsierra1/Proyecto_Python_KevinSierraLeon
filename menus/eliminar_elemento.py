# import menus.eliminar_elemento
import utils.screenController as sc
import utils.validateData as vd
# import random
import utils.corefiles as cf


def eliminar_elemento():
    while True:
        sc.limpiarPantalla()
        print("\n--- Submenú: Eliminar Elemento ---")
        print("1. Eliminar Libro")
        print("2. Eliminar Película")
        print("3. Eliminar Canción")
        print("4. Volver al Menú Principal")
        print("----------------------------------------")

        opcion_sub = input("Seleccione una opción (1-4): ")
        try:
            opcion_sub = int(opcion_sub)
        except ValueError:
            print("Opción no válida, por favor ingrese un número.")
            sc.pausar_pantalla()
            sc.limpiarPantalla()
            continue

        match opcion_sub:
            case 1:
                print("\n>>> Eliminando libro...")
                nombre_libro = vd.validatatext("Ingrese el nombre del libro a eliminar: ")
                if cf.deleteJson(["LIBRO", nombre_libro]):
                    print(f"Libro '{nombre_libro}' eliminado exitosamente ✅")
                else:
                    print(f"No se pudo eliminar el libro '{nombre_libro}' ❌")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
            case 2:
                print("\n>>> Eliminando película...")
                nombre_pelicula = vd.validatatext("Ingrese el nombre de la película a eliminar: ")
                if cf.deleteJson(["PELICULA", nombre_pelicula]):
                    print(f"Película '{nombre_pelicula}' eliminada exitosamente ✅")
                else:
                    print(f"No se pudo eliminar la película '{nombre_pelicula}' ❌")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
            case 3:
                print("\n>>> Eliminando canción...")
                nombre_cancion = vd.validatatext("Ingrese el nombre de la canción a eliminar: ")
                if cf.deleteJson(["MUSICA", nombre_cancion]):
                    print(f"Canción '{nombre_cancion}' eliminada exitosamente ✅")
                else:
                    print(f"No se pudo eliminar la canción '{nombre_cancion}' ❌")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
            case 4:
                print("seguro que desea volver al menú principal? (s/n)")
                respuesta = input().strip().lower()
                if respuesta == 's':
                    return
                elif respuesta == 'n':
                    sc.limpiarPantalla()
                    continue
                else:
                    print('Opción no válida. Regresando al menú principal.')
                    sc.pausar_pantalla()
                    return
            case _:
                print('Opción no válida, por favor intente de nuevo.')
                sc.pausar_pantalla()
                sc.limpiarPantalla()
                continue