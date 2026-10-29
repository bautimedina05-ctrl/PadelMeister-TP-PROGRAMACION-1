try:
    from socios import numerodesocios
    SOCIOS_VALIDOS = set(numerodesocios)
except ((ImportError, ModuleNotFoundError)):
    print("Error: No se pudo importar la lista de socios válidos. Asegúrese de que el archivo 'socios.py' exista y contenga la variable 'numerodesocios'.")
    SOCIOS_VALIDOS = set()
    
import re

ranking_individual = []
ranking_dobles = []


def mostrar_alerta(mensaje):
    """Muestra un mensaje de alerta en la consola."""
    separador = "-" *90
    print(separador)
    print(mensaje)
    print(separador)

def validar_numero_socio():
    """Valida que el número de socio ingresado sea numérico entero positivo, 0 o -1 para salir."""
    while True:
        try:
            socio = input("Ingrese su número de socio (o -1 para salir): ")
            if socio == "-1":
                return -1
            nro_socio = int(socio)
            if nro_socio < 0:
                mostrar_alerta("Número de socio inválido. Debe ingresar solo números positivos, 0 o -1 para salir.")
            else:
                return nro_socio
        except ValueError:
            mostrar_alerta("Número de socio inválido. Debe ingresar solo números positivos, 0 o -1 para salir.")

def socio(socios_validos):
    """Función para ingresar el número de socio y verificar si es válido."""
    while True:
        nro_socio = validar_numero_socio()
        
        if nro_socio == -1:
            mostrar_alerta("Operación cancelada. Volviendo al menú principal.")
            return None
            
        if nro_socio not in socios_validos:
            mostrar_alerta("Número de socio inexistente. Por favor, ingrese un número válido o -1 para salir.")
        else:
            mostrar_alerta(f"Bienvenido, socio {nro_socio}.")
            return nro_socio


def esta_anotado(anotados, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking."""
    return any(registro[0] == nro_socio for registro in anotados)


def esta_anotado_dobles(ranking_dobles, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking de dobles."""
    return any(nro_socio in equipo[1:3] for equipo in ranking_dobles)


def Anotar_individual(ranking_individual, socios_validos):
    """Inscribe a un jugador en el ranking individual."""
    jugador_socio = socio(socios_validos)

    if jugador_socio is None:
        return ranking_individual

    if esta_anotado(ranking_individual, jugador_socio):
        mostrar_alerta("Usted ya se encuentra inscripto en el ranking.")
        return ranking_individual

    puntos = 0
    # Guardamos [nro_socio, puntos]
    ranking_individual.append([jugador_socio, puntos])
    mostrar_alerta(f"Socio {jugador_socio} inscrito con éxito en el ranking individual.")
    mostrar_alerta("¡Inscripción exitosa!")
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
    if nro_socio1 is None:
        return None

    print("--- Datos del segundo jugador ---")
    nro_socio2 = socio(socios_validos)
    if nro_socio2 is None:
        return None
    
    if nro_socio1 == nro_socio2:
        mostrar_alerta("Los jugadores no pueden ser la misma persona. Por favor, ingrese números de socio diferentes.")
        return None

    if esta_anotado_dobles(ranking_dobles, nro_socio1) or esta_anotado_dobles(ranking_dobles, nro_socio2):
        mostrar_alerta("Uno o ambos jugadores ya se encuentran inscriptos en un equipo.")
        return None
        
    equipo = equiposIguales(ranking_dobles)
    puntos = 0

    # Guardamos [nombre_equipo, nro_socio1, nro_socio2, puntos]
    return [equipo, nro_socio1, nro_socio2, puntos]


def Anotar_dobles(ranking_dobles, socios_validos):
    """Inscribe a un equipo en el ranking de dobles."""

    mostrar_alerta("Bienvenido al apartado de torneos de PadelMeister")
    mostrar_alerta("Para poder inscribirse en un torneo, primero debe ingresar su número de socio.")
    equipo = Nombre_equipo(ranking_dobles, socios_validos)

    if equipo is not None:
        ranking_dobles.append(equipo)
        mostrar_alerta(f"Equipo {equipo[0]} inscrito con éxito. Jugadores: {equipo[1]} y {equipo[2]}.")
        mostrar_alerta("¡Inscripción exitosa!")

    return ranking_dobles


def equipo_existe(ranking_dobles, nombre_equipo):
    """Verifica si un equipo ya existe en el ranking de dobles."""

    return any(equipo[0] == nombre_equipo for equipo in ranking_dobles)


def partido(jugador):
    """Pregunta el resultado del partido para el jugador/equipo."""

    while True: 
        try: 
            gano = int(input(f"¿Ganó el jugador/equipo {jugador}? (1: Sí, 0: No): "))
            if gano in [0, 1, 2]:
                break
            mostrar_alerta("Opción inválida. Por favor, ingrese 1, 0 o 2.")
        except ValueError:
            mostrar_alerta("Error: Debe ingresar obligatoriamente un número entero (0, 1 o 2).")

    if gano == 1:
        mostrar_alerta(f"¡{jugador} ha ganado el partido!")
        return "1"
    elif gano == 0:
        mostrar_alerta(f"¡{jugador} ha perdido el partido!")
        return "0"
    else:
        mostrar_alerta("Operación cancelada. Volviendo al menú principal.")
        return "2"


def sumar_puntos(ranking_individual, socios_validos):
    """Suma 3 puntos en el ranking individual si gana."""

    print("Introduzca su número de socio para modificar el ranking:")

    nro_socio = socio(socios_validos)

    if nro_socio is None:
        return ranking_individual

    if encontrar_Jugador(ranking_individual, nro_socio) == True:
        if partido(nro_socio) == "1":
            for jugador in ranking_individual:
                if jugador[0] == nro_socio:
                    jugador[1] += 3
                    mostrar_alerta(f"Se han sumado 3 puntos al socio {jugador[0]}.")

    else:
        mostrar_alerta("El socio no está registrado en el ranking individual.")

    return ranking_individual


def sumar_Puntos_dobles(ranking_dobles):
    """Suma 3 puntos al equipo en el ranking de dobles si gana."""

    nombre_equipo = input("Ingrese el nombre del equipo para modificar el ranking: ")   

    if encontrar_equipo(ranking_dobles, nombre_equipo) == True:
        if partido(nombre_equipo) == "1":
            for equipo in ranking_dobles:
                if equipo[0] == nombre_equipo:
                    equipo[3] += 3
                    mostrar_alerta(f"Se han sumado 3 puntos al equipo {equipo[0]}.")

    else: 
        mostrar_alerta("El equipo no se encuentra registrado en el ranking de dobles.")

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

def ordenar_ranking_Individual(ranking_individual):
    """Ordena el ranking de mayor a menor según los puntos."""
    return sorted(ranking_individual, key=lambda x: x[1], reverse=True)


def ordenar_ranking_dobles(ranking_dobles):
    """Ordena el ranking de dobles de mayor a menor según los puntos."""
    return sorted(ranking_dobles, key=lambda x: x[3], reverse=True)


def mostrar_ranking(ranking_individual, ranking_dobles):
    """Muestra la tabla de rankings."""
    Individual = ordenar_ranking_Individual(ranking_individual)
    Dobles = ordenar_ranking_dobles(ranking_dobles)
    print("\n=== RANKING INDIVIDUAL ===")
    for jugador in Individual:
        print(f"Socio: {jugador[0]} | Puntos: {jugador[1]}")

    print("\n=== RANKING DOBLES ===")
    for equipo in Dobles:
        print(f"Equipo: {equipo[0]} | Jugadores: {equipo[1]}, {equipo[2]} | Puntos: {equipo[3]}")


def opciones():
    
    """Asegura que el usuario ingrese una opción válida del menú."""
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            mostrar_alerta("Opción inválida. Por favor, seleccione un número entre 1 y 6.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


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

if __name__ == "__main__":
    Ranking()