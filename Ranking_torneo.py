ranking_individual = []
ranking_dobles = []

# Lista de socios válidos para prueba
SOCIOS_VALIDOS = ["101", "102", "103", "104", "105"]


def socio(socios):
    """Función para ingresar el número de socio y verificar si es válido."""
    nro_socio = input("Ingrese su número de socio: ")
    while nro_socio not in socios:
        print("Número de socio inexistente. Por favor, ingrese un número válido.")
        nro_socio = input("Ingrese su número de socio: ")
    return nro_socio


def esta_anotado(anotados, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking."""
    for registro in anotados:
        if nro_socio in registro:
            return True
    return False


def Anotar_individual(ranking_individual, socios_validos):
    """Inscribe a un jugador en el ranking individual."""
    jugador_socio = socio(socios_validos)

    if esta_anotado(ranking_individual, jugador_socio):
        print("Usted ya se encuentra inscripto en el ranking.")
        return ranking_individual

    puntos = 0
    # Guardamos [nro_socio, puntos]
    ranking_individual.append([jugador_socio, puntos])
    print("¡Inscripción exitosa!")
    return ranking_individual


        


def Nombre_equipo(ranking_dobles, socios_validos):
    """Ingresa el nombre del equipo y verifica socios."""
    print("--- Datos del primer jugador ---")
    nro_socio1 = socio(socios_validos)
    print("--- Datos del segundo jugador ---")
    nro_socio2 = socio(socios_validos)

    if esta_anotado(ranking_dobles, nro_socio1) or esta_anotado(ranking_dobles, nro_socio2):
        print("Uno o ambos jugadores ya se encuentran inscriptos en un equipo.")
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    puntos = 0

    # Guardamos [nombre_equipo, nro_socio1, nro_socio2, puntos]
    return [nombre_equipo, nro_socio1, nro_socio2, puntos]


def Anotar_dobles(ranking_dobles, socios_validos):
    """Inscribe a un equipo en el ranking de dobles."""
    print("Bienvenido al apartado de torneos de PadelMeister")
    print("Para poder inscribirse en un torneo, primero debe ingresar su número de socio.")
    equipo = Nombre_equipo(ranking_dobles, socios_validos)
    ranking_dobles.append(equipo)
    print("¡Inscripción exitosa!")
    return ranking_dobles


def partido(jugador):
    """Pregunta el resultado del partido para el jugador/equipo."""
    gano = int(input(f"Ingrese 1 si ganó el partido o 0 si perdió ({jugador}): "))
    if gano == 1:
        print(f"¡{jugador} ha ganado el partido!")
    elif gano == 0:
        print(f"¡{jugador} ha perdido el partido!")
    return gano


def sumar_puntos(ranking_individual, socios_validos):
    """Suma 3 puntos en el ranking individual si gana."""
    print("Introduzca su número de socio para modificar el ranking:")
    nro_socio = socio(socios_validos)
    if encontrar_Jugador(ranking_individual, nro_socio) == True:
        if partido(nro_socio) == 1:
            for jugador in ranking_individual:
                if jugador[0] == nro_socio:
                    jugador[1] += 3
                    print(f"Se han sumado 3 puntos al socio {nro_socio}.")
    else:
        print("El socio no está registrado en el ranking individual.")

    return ranking_individual


def sumar_Puntos_dobles(ranking_dobles):
    """Suma 3 puntos al equipo en el ranking de dobles si gana."""
    nombre_equipo = input("Ingrese el nombre del equipo para modificar el ranking: ")   
    if encontrar_equipo(ranking_dobles, nombre_equipo) == True:
        if partido(nombre_equipo) == 1:
            for equipo in ranking_dobles:
                if equipo[0] == nombre_equipo:
                   equipo[3] += 3
                   print(f"Se han sumado 3 puntos al equipo {equipo[0]}.")
    else: 
        print("El equipo no se encuentra registrado en el ranking de dobles.")

    return ranking_dobles

def encontrar_Jugador(ranking_individual, jugador):
    for i in range(len(ranking_individual)):
        if jugador == ranking_individual[i,0]:
            return True

def encontrar_equipo(ranking_dobles, equipo):
    for i in range(len(ranking_dobles)):
        if equipo == ranking_dobles[i,0]:
            return True


def mostrar_ranking(ranking_individual, ranking_dobles):
    """Muestra la tabla de rankings."""
    print("\n=== RANKING INDIVIDUAL ===")
    for jugador in ranking_individual:
        print(f"Socio: {jugador[0]} | Puntos: {jugador[1]}")

    print("\n=== RANKING DOBLES ===")
    for equipo in ranking_dobles:
        print(f"Equipo: {equipo[0]} | Jugadores: {equipo[1]}, {equipo[2]} | Puntos: {equipo[3]}")

def opciones():
    opciones = int(input("Seleccione una opción: "))
    while opciones < 1 or opciones > 6:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        opciones = int(input("Seleccione una opción: "))
    return opciones

def Ranking():
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
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

Ranking()