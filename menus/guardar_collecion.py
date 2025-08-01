import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def guardar_cargar_coleccion():
    print("\n--- Menú de Colección ---")
    print("1. Guardar colección")
    print("2. Cargar colección")
    print("3. Volver al menú principal")
    opcion = input("Seleccione una opción (1-3): ")

    if opcion == "1":
        print("\n>>> Guardando colección...")
        if cf.guardar_coleccion("guardar"):
            print("Colección guardada exitosamente ✅")
        else:
            print("Error al guardar la colección ❌")
    elif opcion == "2":
        print("\n>>> Cargando colección...")
        if cf.guardar_coleccion("cargar"):
            print("Colección cargada exitosamente ✅")
        else:
            print("Error al cargar la colección ❌")
    elif opcion == "3":
        print("Volviendo al menú principal...")
        return
    else:
        print("Opción no válida. Por favor, elija una opción del menú.")

    sc.pausar_pantalla()