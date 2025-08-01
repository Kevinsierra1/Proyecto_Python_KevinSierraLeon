import utils.screenController as sc
import utils.corefiles as cf

def ver_por_categoria():
    elementos = cf.readJson()
    if not elementos:
        print("No hay elementos en la colección.")
        return

    categorias = list(elementos.keys())
    while True:
        print("\nCategorías disponibles:")
        for idx, cat in enumerate(categorias, 1):
            print(f"{idx}. {cat}")
        print(f"{len(categorias)+1}. Volver al menú principal")

        try:
            opcion = int(input("Seleccione la categoría a mostrar: "))
            if opcion == len(categorias) + 1:
                # Salir del menú
                return
            if opcion < 1 or opcion > len(categorias) + 1:
                print("Opción no válida.")
                continue
        except ValueError:
            print("Entrada no válida.")
            continue

        categoria_seleccionada = categorias[opcion - 1]
        items = elementos.get(categoria_seleccionada, {})

        print(f"\n=== Elementos en la categoría {categoria_seleccionada} ===")
        for nombre, detalles in items.items():
            print(f"Nombre: {nombre}")
            for clave, valor in detalles.items():
                print(f"{clave.capitalize()}: {valor}")
            print("-------------------------------")
        sc.pausar_pantalla()