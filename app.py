import utils.screenController as sc
import menus.aniadir_elemento as ma
import menus.buscar_elemento as be
import menus.editar_elemento as ed
import menus.eliminar_elemento as el
import menus.ver_elemento as ve
import menus.ver_por_categoria as vp
from config import AGREGAR
if __name__ == "__main__":
        sc.limpiarPantalla()
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
      
      while True:
            main_menu()
            opcion = input("Selecciona una opción (1-8) ")
            opcion = int(opcion)
            match opcion:
                  case 1:
                        ma.aniadir_elemento()
                  case 2:
                        print("\n>>> Mostrando todos los elementos...")
                        ve.ver_elementos()
                  case 3:
                        print("\n>>> Buscando un elemento...")
                        be.buscar_elemento()
                  case 4:
                        print("\n>>> Editando un elemento...")
                        ed.editar_elemento()
                  case 5:
                        print("\n>>> Eliminando un elemento...")
                        el.eliminar_elemento()
                  case 6:
                        print("\n>>> Ver elementos por categoría...")
                        vp.ver_por_categoria()
                  case 7:
                        respuesta = input("¿Está seguro que desea salir? (s/n): ")
                        if respuesta.lower() == "s":
                            return
                        else:
                            print("Regresando al menú principal...")
                  case _:
                        print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
      main()