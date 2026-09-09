from socios import numerodesocios
import re

ranking_individual = []
ranking_dobles = []

# Se importa la lista numerodesocios directamente desde el archivo socios.py
SOCIOS_VALIDOS = numerodesocios


def validar_numero_socio():
    """Valida que el número de socio ingresado sea numérico entero positivo o cero."""
    socio = input("Ingrese su número de socio: ")
    while not re.match(r'^\d+$', socio):
        print("---------------------------------------------------------------------------------------")
        print("Número de socio inválido. Debe ingresar solo números positivos o 0.")
        print("---------------------------------------------------------------------------------------")
        socio = input("Ingrese su número de socio: ")
    return int(socio)


def socio(socios_validos):
    """Función para ingresar el número de socio y verificar si es válido."""
    nro_socio = validar_numero_socio()
    if nro_socio not in socios_validos:
        print("---------------------------------------------------------------------------------------")
        print("Número de socio inexistente. Por favor, ingrese un número válido.")
        print("---------------------------------------------------------------------------------------")
    else:
        print("---------------------------------------------------------------------------------------")
        print(f"Bienvenido, socio {nro_socio}.")
        print("---------------------------------------------------------------------------------------")
    return nro_socio


def esta_anotado(anotados, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking."""
    for registro in anotados:
        if registro[0] == nro_socio:
            return True
    return False


def esta_anotado_dobles(ranking_dobles, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking de dobles."""
    for equipo in ranking_dobles:
        if nro_socio == equipo[1] or nro_socio == equipo[2]:
            return True
    return False


def Anotar_individual(ranking_individual, socios_validos):
    """Inscribe a un jugador en el ranking individual."""
    jugador_socio = socio(socios_validos)

    if esta_anotado(ranking_individual, jugador_socio):
        print("---------------------------------------------------------------------------------------")
        print("Usted ya se encuentra inscripto en el ranking.")
        print("---------------------------------------------------------------------------------------")
        return ranking_individual

    puntos = 0
    # Guardamos [nro_socio, puntos]
    ranking_individual.append([jugador_socio, puntos])
    print("---------------------------------------------------------------------------------------")
    print(f"Socio {jugador_socio} inscrito con éxito en el ranking individual.")
    print("¡Inscripción exitosa!")
    print("---------------------------------------------------------------------------------------")
    return ranking_individual


def equiposIguales(ranking_dobles):
    """Verifica si un equipo ya existe en el ranking de dobles."""
    equipo = input("Ingrese el nombre del equipo: ")
    while encontrar_equipo(ranking_dobles, equipo):
        print("El nombre de equipo ya existe. Elija otro.")
        equipo = input("Ingrese el nombre del equipo: ")
    return equipo


def Nombre_equipo(ranking_dobles, socios_validos):
    """Ingresa el nombre del equipo y verifica socios."""
    print("--- Datos del primer jugador ---")
    nro_socio1 = socio(socios_validos)
    print("--- Datos del segundo jugador ---")
    nro_socio2 = socio(socios_validos)
    
    if nro_socio1 == nro_socio2:
        print("---------------------------------------------------------------------------------------")
        print("Los jugadores no pueden ser la misma persona. Por favor, ingrese números de socio diferentes.")
        print("---------------------------------------------------------------------------------------")
        return None

    if esta_anotado_dobles(ranking_dobles, nro_socio1) or esta_anotado_dobles(ranking_dobles, nro_socio2):
        print("Uno o ambos jugadores ya se encuentran inscriptos en un equipo.")
        return None
        
    equipo = equiposIguales(ranking_dobles)
    puntos = 0

    # Guardamos [nombre_equipo, nro_socio1, nro_socio2, puntos]
    return [equipo, nro_socio1, nro_socio2, puntos]


def Anotar_dobles(ranking_dobles, socios_validos):
    """Inscribe a un equipo en el ranking de dobles."""
    print("Bienvenido al apartado de torneos de PadelMeister")
    print("Para poder inscribirse en un torneo, primero debe ingresar su número de socio.")
    equipo = Nombre_equipo(ranking_dobles, socios_validos)
    if equipo is not None:
        ranking_dobles.append(equipo)
        print("---------------------------------------------------------------------------------------")
        print(f"Equipo {equipo[0]} inscrito con éxito. Jugadores: {equipo[1]} y {equipo[2]}.")
        print("¡Inscripción exitosa!")
        print("---------------------------------------------------------------------------------------")
    return ranking_dobles


def equipo_existe(ranking_dobles, nombre_equipo):
    """Verifica si un equipo ya existe en el ranking de dobles."""
    for equipo in ranking_dobles:
        if equipo[0] == nombre_equipo:
            return True
    return False


def partido(jugador):
    """Pregunta el resultado del partido para el jugador/equipo."""
    gano = input(f"Ingrese 1 si ganó el partido o 0 si perdió ({jugador}): ")
    while not re.match(r'^[01]$', gano):
        print("---------------------------------------------------------------------------------------")
        print("Opción inválida. Por favor, ingrese 1 para ganar o 0 para perder.")
        print("---------------------------------------------------------------------------------------")
        gano = input(f"Ingrese 1 si ganó el partido o 0 si perdió ({jugador}): ")
    if gano == "1":
        print("---------------------------------------------------------------------------------------")
        print(f"¡{jugador} ha ganado el partido!")
        print("---------------------------------------------------------------------------------------")
    elif gano == "0":
        print("---------------------------------------------------------------------------------------")
        print(f"¡{jugador} ha perdido el partido!")
        print("---------------------------------------------------------------------------------------")
    return gano


def sumar_puntos(ranking_individual, socios_validos):
    """Suma 3 puntos en el ranking individual si gana."""
    print("Introduzca su número de socio para modificar el ranking:")
    nro_socio = socio(socios_validos)
    if encontrar_Jugador(ranking_individual, nro_socio) == True:
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
    """Suma 3 puntos al equipo en el ranking de dobles si gana."""
    nombre_equipo = input("Ingrese el nombre del equipo para modificar el ranking: ")   
    if encontrar_equipo(ranking_dobles, nombre_equipo) == True:
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
    """Verifica si un jugador está registrado en el ranking individual."""
    for i in range(len(ranking_individual)):
        if jugador == ranking_individual[i][0]:
            return True
    return False


def encontrar_equipo(ranking_dobles, equipo):
    """Verifica si un equipo está registrado en el ranking de dobles."""
    for i in range(len(ranking_dobles)):
        if equipo == ranking_dobles[i][0]:
            return True
    return False


def mostrar_ranking(ranking_individual, ranking_dobles):
    """Muestra la tabla de rankings."""
    print("\n=== RANKING INDIVIDUAL ===")
    for jugador in ranking_individual:
        print(f"Socio: {jugador[0]} | Puntos: {jugador[1]}")

    print("\n=== RANKING DOBLES ===")
    for equipo in ranking_dobles:
        print(f"Equipo: {equipo[0]} | Jugadores: {equipo[1]}, {equipo[2]} | Puntos: {equipo[3]}")


def opciones():
    """Asegura que el usuario ingrese una opción válida del menú."""
    opciones = input("Seleccione una opción: ")
    while not re.match(r'^[1-6]$', opciones):
        print("Opción inválida. Por favor, seleccione una opción válida.")
        opciones = input("Seleccione una opción: ")
    return int(opciones)


def Ranking():
    """Función principal que ejecuta el menú de opciones para el ranking de torneos."""
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