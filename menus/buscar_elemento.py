import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def buscar_elemento():
    elementos = cf.readJson()
    if not elementos:
        print("No hay elementos en la colección.")
        return

    categorias = list(elementos.keys())
    print("\n=== Menú de Búsqueda ===")
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")
    print(f"{len(categorias)+1}. Buscar en todas las categorías")
    print(f"{len(categorias)+2}. Volver al menú principal")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == len(categorias) + 2:
            return
        if opcion < 1 or opcion > len(categorias) + 2:
            print("Opción no válida.")
            sc.pausar_pantalla()
            return
    except ValueError:
        print("Entrada no válida.")
        sc.pausar_pantalla()
        return

    print("\nBuscar por:")
    print("1. Nombre")
    print("2. Autor/Director/Artista")
    print("3. Género")
    try:
        tipo_busqueda = int(input("Seleccione el tipo de búsqueda (1-3): "))
        if tipo_busqueda not in [1, 2, 3]:
            print("Opción no válida.")
            sc.pausar_pantalla()
            return
    except ValueError:
        print("Entrada no válida.")
        sc.pausar_pantalla()
        return

    criterio = input("Ingrese el texto a buscar: ")
    resultados = []

    def coincide(detalles):
        if tipo_busqueda == 1:
            return criterio.lower() in detalles.get("Name", "").lower()
        elif tipo_busqueda == 2:
            return criterio.lower() in detalles.get("aut", "").lower()
        elif tipo_busqueda == 3:
            return criterio.lower() in detalles.get("genero", "").lower()
        return False

    if opcion == len(categorias) + 1:
        # Buscar en todas las categorías
        for categoria, items in elementos.items():
            for nombre, detalles in items.items():
                if coincide(detalles):
                    resultados.append((categoria, nombre, detalles))
    else:
        # Buscar solo en la categoría seleccionada
        categoria = categorias[opcion - 1]
        for nombre, detalles in elementos[categoria].items():
            if coincide(detalles):
                resultados.append((categoria, nombre, detalles))

    if resultados:
        print("\n=== Resultados de la Búsqueda ===")
        for categoria, nombre, detalles in resultados:
            print(f"\nCategoría: {categoria}")
            print(f"Nombre: {nombre}")
            for clave, valor in detalles.items():
                print(f"{clave.capitalize()}: {valor}")
            print("-------------------------------")
    else:
        print("No se encontraron elementos que coincidan con el criterio de búsqueda.")
