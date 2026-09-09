import re
from socios import socios

# Lista de socios válidos importada desde socios.py
SOCIOS_VALIDOS = socios

ranking_individual = []
ranking_dobles = []


def validar_numero_socio():
    """Valida que el número ingresado conste exactamente de 4 dígitos."""
    socio = input("Ingrese su número de socio (4 dígitos): ").strip()
    while not re.match(r'^\d{4}$', socio):
        print("---------------------------------------------------------------------------------------")
        print("Número de socio inválido. Debe ser un número de exactamente 4 dígitos.")
        print("---------------------------------------------------------------------------------------")
        socio = input("Ingrese su número de socio (4 dígitos): ").strip()
    return int(socio)


def socio(socios_validos):
    """Solicita el número de socio y itera hasta que el número exista en la lista oficial."""
    while True:
        nro_socio = validar_numero_socio()
        if nro_socio in socios_validos:
            return nro_socio
        print("---------------------------------------------------------------------------------------")
        print("Número de socio inexistente. Por favor, ingrese un número válido registrado.")
        print("---------------------------------------------------------------------------------------")


def esta_anotado(anotados, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking individual."""
    return any(registro[0] == nro_socio for registro in anotados)


def esta_anotado_dobles(ranking_dobles, nro_socio):
    """Verifica si un socio ya forma parte de algún equipo de dobles."""
    return any(nro_socio == equipo[1] or nro_socio == equipo[2] for equipo in ranking_dobles)


def Anotar_individual(ranking_individual, socios_validos):
    """Inscribe a un jugador en el ranking individual."""
    jugador_socio = socio(socios_validos)

    if esta_anotado(ranking_individual, jugador_socio):
        print("---------------------------------------------------------------------------------------")
        print("Usted ya se encuentra inscripto en el ranking individual.")
        print("---------------------------------------------------------------------------------------")
        return ranking_individual

    ranking_individual.append([jugador_socio, 0])
    print("---------------------------------------------------------------------------------------")
    print(f"Socio {jugador_socio} inscrito con éxito en el ranking individual.")
    print("¡Inscripción exitosa!")
    print("---------------------------------------------------------------------------------------")
    return ranking_individual


def equiposIguales(ranking_dobles):
    """Garantiza que el nombre del equipo sea único en la lista de dobles."""
    equipo = input("Ingrese el nombre del equipo: ").strip()
    while encontrar_equipo(ranking_dobles, equipo) or not equipo:
        print("El nombre de equipo ya existe o es inválido. Elija otro.")
        equipo = input("Ingrese el nombre del equipo: ").strip()
    return equipo


def Nombre_equipo(ranking_dobles, socios_validos):
    """Registra los socios del equipo y valida que no se repitan."""
    print("--- Datos del primer jugador ---")
    nro_socio1 = socio(socios_validos)
    
    print("--- Datos del segundo jugador ---")
    nro_socio2 = socio(socios_validos)

    if nro_socio1 == nro_socio2:
        print("---------------------------------------------------------------------------------------")
        print("Los jugadores no pueden ser la misma persona. Ingrese números distintos.")
        print("---------------------------------------------------------------------------------------")
        return None

    if esta_anotado_dobles(ranking_dobles, nro_socio1) or esta_anotado_dobles(ranking_dobles, nro_socio2):
        print("---------------------------------------------------------------------------------------")
        print("Uno o ambos jugadores ya se encuentran inscriptos en un equipo de dobles.")
        print("---------------------------------------------------------------------------------------")
        return None

    nombre_eq = equiposIguales(ranking_dobles)
    return [nombre_eq, nro_socio1, nro_socio2, 0]


def Anotar_dobles(ranking_dobles, socios_validos):
    """Inscribe un equipo en la lista de dobles."""
    print("Bienvenido al apartado de torneos de PadelMeister.")
    equipo = Nombre_equipo(ranking_dobles, socios_validos)
    if equipo is not None:
        ranking_dobles.append(equipo)
        print("---------------------------------------------------------------------------------------")
        print(f"Equipo '{equipo[0]}' inscrito con éxito. Jugadores: {equipo[1]} y {equipo[2]}.")
        print("¡Inscripción exitosa!")
        print("---------------------------------------------------------------------------------------")
    return ranking_dobles


def partido(jugador):
    """Consulta e ingresa el resultado de la competencia."""
    gano = input(f"Ingrese 1 si ganó el partido o 0 si perdió ({jugador}): ").strip()
    while gano not in ("0", "1"):
        print("---------------------------------------------------------------------------------------")
        print("Opción inválida. Por favor, ingrese 1 para ganar o 0 para perder.")
        print("---------------------------------------------------------------------------------------")
        gano = input(f"Ingrese 1 si ganó el partido o 0 si perdió ({jugador}): ").strip()

    if gano == "1":
        print("---------------------------------------------------------------------------------------")
        print(f"¡{jugador} ha ganado el partido!")
        print("---------------------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------------------")
        print(f"¡{jugador} ha perdido el partido!")
        print("---------------------------------------------------------------------------------------")
    return gano


def sumar_puntos(ranking_individual, socios_validos):
    """Asigna 3 puntos al jugador si el resultado fue victoria."""
    print("Introduzca su número de socio para modificar el ranking:")
    nro_socio = socio(socios_validos)

    if encontrar_Jugador(ranking_individual, nro_socio):
        if partido(nro_socio) == "1":
            for jugador in ranking_individual:
                if jugador[0] == nro_socio:
                    jugador[1] += 3
                    print("---------------------------------------------------------------------------------------")
                    print(f"Se han sumado 3 puntos al socio {nro_socio}.")
                    print("---------------------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------------------")
        print("El socio no está registrado en el ranking individual.")
        print("---------------------------------------------------------------------------------------")

    return ranking_individual


def sumar_Puntos_dobles(ranking_dobles):
    """Asigna 3 puntos al equipo registrado en dobles si resulta ganador."""
    nombre_equipo = input("Ingrese el nombre del equipo para modificar el ranking: ").strip()
    if encontrar_equipo(ranking_dobles, nombre_equipo):
        if partido(nombre_equipo) == "1":
            for equipo in ranking_dobles:
                if equipo[0] == nombre_equipo:
                    equipo[3] += 3
                    print("---------------------------------------------------------------------------------------")
                    print(f"Se han sumado 3 puntos al equipo {equipo[0]}.")
                    print("---------------------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------------------")
        print("El equipo no se encuentra registrado en el ranking de dobles.")
        print("---------------------------------------------------------------------------------------")

    return ranking_dobles


def encontrar_Jugador(ranking_individual, jugador):
    """Busca al jugador en la lista individual."""
    return any(jugador == item[0] for item in ranking_individual)


def encontrar_equipo(ranking_dobles, equipo):
    """Busca la existencia del equipo por nombre exacto."""
    return any(equipo == item[0] for item in ranking_dobles)


def mostrar_ranking(ranking_individual, ranking_dobles):
    """Muestra ambas tablas ordenadas de mayor a menor puntaje."""
    print("\n=== RANKING INDIVIDUAL ===")
    ranking_ind_ordenado = sorted(ranking_individual, key=lambda x: x[1], reverse=True)
    for pos, jugador in enumerate(ranking_ind_ordenado, start=1):
        print(f"{pos}. Socio: {jugador[0]} | Puntos: {jugador[1]}")

    print("\n=== RANKING DOBLES ===")
    ranking_dob_ordenado = sorted(ranking_dobles, key=lambda x: x[3], reverse=True)
    for pos, equipo in enumerate(ranking_dob_ordenado, start=1):
        print(f"{pos}. Equipo: {equipo[0]} | Jugadores: {equipo[1]}, {equipo[2]} | Puntos: {equipo[3]}")


def opciones():
    """Valida la entrada de opciones del menú principal."""
    opcion = input("Seleccione una opción: ").strip()
    while not re.match(r'^[1-6]$', opcion):
        print("Opción inválida. Por favor, seleccione una opción válida.")
        opcion = input("Seleccione una opción: ").strip()
    return int(opcion)


def Ranking():
    """Controlador principal del sistema de gestión de rankings."""
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Inscribirse en ranking individual")
        print("2. Inscribirse en ranking de dobles")
        print("3. Registrar resultado de partido individual")
        print("4. Registrar resultado de partido de dobles")
        print("5. Mostrar rankings")
        print("6. Salir")

        opcion = opciones()

        if opcion == 1:
            Anotar_individual(ranking_individual, SOCIOS_VALIDOS)
        elif opcion == 2:
            Anotar_dobles(ranking_dobles, SOCIOS_VALIDOS)
        elif opcion == 3:
            sumar_puntos(ranking_individual, SOCIOS_VALIDOS)
        elif opcion == 4:
            sumar_Puntos_dobles(ranking_dobles)
        elif opcion == 5:
            mostrar_ranking(ranking_individual, ranking_dobles)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
