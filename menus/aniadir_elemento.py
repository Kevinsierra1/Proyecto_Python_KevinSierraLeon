import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def aniadir_elemento():
     while True:
        sc.limpiarPantalla()
        print("\n======Submenú: Añadir Nuevo Elemento =======")
        print("1. Añadir Libro")
        print("2. Añadir Película")
        print("3. Añadir Musica")
        print("4. Volver al Menú Principal")
        print("==============================================")

        opcion_sub = input("Seleccione una opcion (1-4): ")
        try:
            opcion_sub = int(opcion_sub)
        except ValueError:
            print("Opción no válida, por favor ingrese un número.")
            sc.pausar_pantalla()
            sc.limpiarPantalla()
            continue

        match opcion_sub:
            case 1:
                print("\n>>> Añadiendo libro...")
                nomLi = vd.validatatext("Ingrese el nombre del libro: ")
                autLi = vd.validatatext("Autor: ")
                generoLi = vd.validatatext("Genero: ")
                valorLi = vd.validateflot("Ingrese la valoración que le da al libro (1-10): ")
                if valorLi <=0 or valorLi >10:
                    print("Por favor solo de (1-10)")
                    sc.pausar_pantalla()
                    sc.limpiarPantalla()
                    continue
                libro = {
                    "Name": nomLi,
                    "aut": autLi,
                    "genero": generoLi,
                    "valora": valorLi,
                }
                if not cf.updateJson({nomLi: libro}, ["LIBRO"]):
                    print("Libro agregado exitosamente ✅")
                else:
                    print("No se pudo agregar el libro ❌ ")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
            case 2:
                print("\n>>> Añadiendo película...")
                nomPe = vd.validatatext("Ingrese el nombre de la pelicula: ")
                autPe = vd.validatatext("Autor: ")
                generoPe = vd.validatatext("Genero: ")
                valorPe = vd.validateflot("Ingrese la valoración que le da a la pelicula (1-10): ")
                if valorPe <=0 or valorPe >10:
                    print("Por favor solo de (1-10)")
                    sc.pausar_pantalla()
                    sc.limpiarPantalla()
                    continue
                pelicula = {
                    "Name": nomPe,
                    "aut": autPe,
                    "genero": generoPe,
                    "valora": valorPe,
                }
                if not  cf.updateJson({nomPe: pelicula}, ["PELICULA"]):
                    print("Pelicula agregada exitosamente ✅")
                else:
                    print("No se pudo agregar la Pelicula ❌ ")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
            case 3:
                print("\n>>> Añadiendo canción...")
                nomMu = vd.validatatext("Ingrese el nombre de la canción: ")
                autMu = vd.validatatext("Artista: ")
                generoMu = vd.validatatext("Genero: ")
                valorMu = vd.validateflot("Ingrese la valoración que le da a la canción (1-10): ")
                if valorMu <=0 or valorMu >10:
                    print("Por favor solo de (1-10)")
                    sc.pausar_pantalla()
                    sc.limpiarPantalla()
                    continue
                musica = {
                    "Name": nomMu,
                    "aut": autMu,
                    "genero": generoMu,
                    "valora": valorMu,
                }
                if not  cf.updateJson({nomMu: musica}, ["MUSICA"]):
                    print("Canción agregada exitosamente ✅")
                else:
                    print("No se pudo agregar la canción ❌ ")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
            case 4:
                print('Seguro de que desea volver al menú principal? (S/N)')
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
                print("Opción no válida, por favor intente de nuevo.")
                sc.pausar_pantalla()
                sc.limpiarPantalla()
                continue