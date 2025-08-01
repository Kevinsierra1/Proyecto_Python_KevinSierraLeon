import utils.screenController as sc
import utils.validateData as vd
import random
import utils.corefiles as cf


def editar_elemento():
    while True:
        print("\n--- Submenú: Editar Elemento ---")
        print("1. Editar Libro")
        print("2. Editar Película")
        print("3. Editar Videojuego")
        print("4. Volver al Menú Principal")
        print("----------------------------------------")

        opcion_sub = input("Seleccione una opción (1-4): ")
        opcion_sub = int(opcion_sub)

        match opcion_sub:
            case 1:
                nombre_libro = vd.validatatext("Ingrese el nombre del libro a editar: ")

                nomLi = vd.validatatext("Ingrese el nombre del libro: ")
                autLi = vd.validatatext("Autor: ")
                generoLi = vd.validatatext("Genero: ")
                valorLi = vd.validateflot("Ingrese la valoración que le da al libro (1-10): ")
                valorLi = float(valorLi)
                if valorLi <=0 or valorLi >10:
                    print("Por favor solo de (1-10)")
                    return valorLi
                libro = {
                    "Name": nomLi,
                    "aut": autLi,
                    "genero": generoLi,
                    "valora": valorLi,
                }
                if nomLi != nombre_libro:
                    cf.deleteJson(["LIBRO", nombre_libro])
                else:
                    print("El libro no existe.")

                if not cf.updateJson({nomLi: libro}, ["LIBRO"], nombre_libro):
                    print("Libro editado exitosamente ✅")
                else:
                    print("No se pudo editar el libro ❌ ")
                    
                sc.pausar_pantalla()
            case 2:
                print("\n>>> Editando película...")
                nombre_pelicula = vd.validatatext("Ingrese el nombre de la película a editar: ")

                nomPe = vd.validatatext("Ingrese el nombre de la película: ")
                autPe = vd.validatatext("Autor: ")
                generoPe = vd.validatatext("Genero: ")
                valorPe = vd.validateflot("Ingrese la valoración que le da a la película (1-10): ")
                valorPe = float(valorPe)
                if valorPe <=0 or valorPe >10:
                    print("Por favor solo de (1-10)")
                    return valorPe
                pelicula = {
                    "Name": nomPe,
                    "aut": autPe,
                    "genero": generoPe,
                    "valora": valorPe,
                }
                if nomPe != nombre_pelicula:
                    cf.deleteJson(["PELICULA", nombre_pelicula])
                else:
                    print("La película no existe.")

                if not cf.updateJson({nomPe: pelicula}, ["PELICULA"], nombre_pelicula):
                    print("Película editada exitosamente ✅")
                else:
                    print("No se pudo editar la película ❌ ")
                    
                sc.pausar_pantalla()
            case 3:
                nombre_musica = vd.validatatext("Ingrese el nombre de la canción a editar: ")

                nomMu = vd.validatatext("Ingrese el nombre de la canción: ")
                autMu = vd.validatatext("Artista: ")
                generoMu = vd.validatatext("Genero: ")
                valorMu = vd.validateflot("Ingrese la valoración que le da a la canción (1-10): ")
                valorMu = float(valorMu)
                if valorMu <=0 or valorMu >10:
                    print("Por favor solo de (1-10)")
                    return valorMu
                musica = {
                    "Name": nomMu,
                    "aut": autMu,
                    "genero": generoMu,
                    "valora": valorMu,
                }
                if nomMu != nombre_musica:
                    cf.deleteJson(["MUSICA", nombre_musica])
                else:
                    print("La canción no existe.")

                if not cf.updateJson({nomMu: musica}, ["MUSICA"], nombre_musica):
                    print("Canción editada exitosamente ✅")
                else:
                    print("No se pudo editar la canción ❌ ")
                    
                sc.pausar_pantalla()
            case 4:
                print("seguro que desea volver al menú principal? (s/n)")
                respuesta = input().strip().lower()
                if respuesta == 's':
                    return
                elif respuesta == 'n':
                    continue
                else:
                    print('Opción no válida. Regresando al menú principal.')
                    return
            case _:
                print("Opción no válida, por favor intente de nuevo.")
                sc.pausar_pantalla()
                continue