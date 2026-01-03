import utils.screenController as sc
import menus.aniadir_elemento as ma
import menus.buscar_elemento as be
import menus.editar_elemento as ed
import menus.eliminar_elemento as el
import menus.ver_elemento as ve
import menus.ver_por_categoria as vp
from config import AGREGAR

def main_menu():
    print("\n===========================================")
    print("        Administrador de Colección")
    print("=============================================")
    print("1. Añadir un Nuevo Elemento")
    print("2. Ver Todos los Elementos")
    print("3. Buscar un Elemento")
    print("4. Editar un Elemento")
    print("5. Eliminar un Elemento")
    print("6. Ver Elementos por Categoría")
    print("7. Salir")
    print("=============================================")

def main():
      sc.limpiarPantalla()
      while True:
            main_menu()
            try:
                  opcion = input("Selecciona una opción (1-7): ")
                  opcion = int(opcion)
            except ValueError:
                  print("Opción no válida, por favor ingrese un número.")
                  sc.pausar_pantalla()
                  sc.limpiarPantalla()
                  continue
            
            match opcion:
                  case 1:
                        sc.limpiarPantalla()
                        ma.aniadir_elemento()
                        sc.limpiarPantalla()
                  case 2:
                        sc.limpiarPantalla()
                        print("\n>>> Mostrando todos los elementos...")
                        ve.ver_elementos()
                        sc.limpiarPantalla()
                  case 3:
                        sc.limpiarPantalla()
                        print("\n>>> Buscando un elemento...")
                        be.buscar_elemento()
                        sc.limpiarPantalla()
                  case 4:
                        sc.limpiarPantalla()
                        print("\n>>> Editando un elemento...")
                        ed.editar_elemento()
                        sc.limpiarPantalla()
                  case 5:
                        sc.limpiarPantalla()
                        print("\n>>> Eliminando un elemento...")
                        el.eliminar_elemento()
                        sc.limpiarPantalla()
                  case 6:
                        sc.limpiarPantalla()
                        print("\n>>> Ver elementos por categoría...")
                        vp.ver_por_categoria()
                        sc.limpiarPantalla()
                  case 7:
                        respuesta = input("¿Está seguro que desea salir? (s/n): ")
                        if respuesta.lower() == "s":
                            sc.limpiarPantalla()
                            return
                        else:
                            print("Regresando al menú principal...")
                            sc.pausar_pantalla()
                            sc.limpiarPantalla()
                  case _:
                        print("Opción no válida, por favor intente de nuevo.")
                        sc.pausar_pantalla()
                        sc.limpiarPantalla()

if __name__ == "__main__":
      main()