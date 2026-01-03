import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def ver_elementos():
    sc.limpiarPantalla()
    elementos = cf.readJson()
    if not elementos:
        print("No hay elementos en la colección.")
        return

    categorias = list(elementos.keys())
    print("\n=== Menú de Categorías ===")
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")
    print(f"{len(categorias)+1}. Volver al menú principal")

    try:
        opcion = int(input("Seleccione una categoría: "))
        if opcion == len(categorias) + 1:
            return
        if opcion < 1 or opcion > len(categorias):
            print("Opción no válida.")
            sc.pausar_pantalla()
            return
    except ValueError:
        print("Entrada no válida.")
        sc.pausar_pantalla()
        return

    categoria = categorias[opcion - 1]
    items = elementos.get(categoria, {})
    print(f"\n=== Elementos en la categoría {categoria} ===")
    for nombre, detalles in items.items():
        print(f"Nombre: {nombre}")
        for clave, valor in detalles.items():
            print(f"{clave.capitalize()}: {valor}")
        print("-------------------------------")
    
    sc.pausar_pantalla()