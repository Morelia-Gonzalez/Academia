categorias = {}

def mostrar_categorias_existentes():
    if not categorias:
        print("No hay categorías registradas aún.")
    else:
        print("Categorías registradas:")
        for cat in categorias:
            print(f"- {cat}")

def registrar_pelicula():
    print("\n--- Registrar Película ---")
    mostrar_categorias_existentes()

    categoria = input("Ingrese la categoría: ").strip()
    pelicula = input("Ingrese el nombre de la película: ").strip()
    if categoria not in categorias:
        categorias[categoria] = {}

    if pelicula in categorias[categoria]:
        print(f"La película '{pelicula}' ya está registrada en la categoría '{categoria}'.")
    else:
        categorias[categoria][pelicula] = 0
        print(f"Película '{pelicula}' registrada en la categoría '{categoria}' con 0 votos.")

def votar_pelicula():
    print("\n--- Votar por Película ---")
    mostrar_categorias_existentes()

    if not categorias:
        return

    categoria = input("Ingrese la categoría: ").strip()

    if categoria not in categorias:
        print("La categoría no existe.")
        return

    if not categorias[categoria]:
        print(f"No hay películas registradas en la categoría '{categoria}'.")
        return

    print(f"Películas en {categoria}:")
    for peli in categorias[categoria]:
        print(f"- {peli}")

    pelicula = input("Ingrese la película a votar: ").strip()

    if pelicula not in categorias[categoria]:
        print(f"La película '{pelicula}' no está registrada en '{categoria}'.")
    else:
        categorias[categoria][pelicula] += 1
        print(f"Voto registrado para '{pelicula}' en '{categoria}'.")

def mostrar_resultados():
    print("\n--- Resultados Actuales ---")
    if not categorias:
        print("No hay películas registradas.")
        return
    
    for categoria, peliculas in categorias.items():
        print(f"\nCategoría: {categoria}")
        if peliculas:
            for pelicula, votos in peliculas.items():
                print(f" - {pelicula}: {votos} votos")
        else:
            print(" (Sin películas registradas)")

def determinar_ganadoras():
    print("\n--- Ganadoras por Categoría ---")
    if not categorias:
        print("No hay datos para determinar ganadoras.")
        return

    for categoria, peliculas in categorias.items():
        if not peliculas:
            print(f"Categoría '{categoria}' no tiene películas registradas.")
            continue

        max_votos = -1
        ganadora = None
        for pelicula, votos in peliculas.items():
            if votos > max_votos:
                max_votos = votos
                ganadora = pelicula

        print(f"Ganadora en '{categoria}': {ganadora} con {max_votos} votos.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar película")
        print("2. Votar película")
        print("3. Mostrar resultados")
        print("4. Determinar ganadoras por categoría")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número del 1 al 5.")
            continue

        if opcion == 1:
            registrar_pelicula()
        elif opcion == 2:
            votar_pelicula()
        elif opcion == 3:
            mostrar_resultados()
        elif opcion == 4:
            determinar_ganadoras()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción fuera de rango, intente de nuevo.")
menu()