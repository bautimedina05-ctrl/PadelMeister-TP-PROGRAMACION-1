import re
import sys
import json
import importlib 
from functools import reduce

ARCHIVO_INDIVIDUAL = "ranking_individual.json"
ARCHIVO_DOBLES = "ranking_dobles.json"

def mostrar_alerta(mensaje):
    """Muestra un mensaje de alerta en la consola."""
    separador = "-" *90
    print(separador)
    print(mensaje)
    print(separador)

def obtener_socios_validos():
    """Importa o recarga dinámicamente la lista de socios desde socios.py."""
    try:
        import socios
        # Recargamos el módulo por si fue modificado externamente mientras corre el programa
        importlib.reload(socios)
        
        SOCIOS_VALIDOS = set(int(s) for s in socios.numerodesocios)
        if not SOCIOS_VALIDOS:
            mostrar_alerta("Advertencia: La lista de socios válidos está vacía en 'socios.py'.")
        return SOCIOS_VALIDOS
    except (ImportError, ModuleNotFoundError):
        mostrar_alerta("Error: No se pudo importar el archivo 'socios.py' o no contiene la variable 'numerodesocios'.")
        sys.exit(1)  # Salir del programa si no se puede importar la lista de socios válidos

# Verificación inicial al arrancar el programa
SOCIOS_VALIDOS = obtener_socios_validos()


def cargar_datos(archivo):
    """Carga los datos desde un archivo JSON."""
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_datos(archivo, datos):
    """Guarda los datos en un archivo JSON."""
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

ranking_individual = cargar_datos(ARCHIVO_INDIVIDUAL)
ranking_dobles = cargar_datos(ARCHIVO_DOBLES)



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
    coincidencias = list(filter(lambda registro: registro[0] == nro_socio, anotados))
    return len(coincidencias) > 0


def esta_anotado_dobles(ranking_dobles, nro_socio):
    """Verifica si un número de socio ya existe dentro del ranking de dobles."""
    coincidencias = list(filter(lambda equipo: nro_socio in equipo[1:3], ranking_dobles))
    return len(coincidencias) > 0


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
    guardar_datos(ARCHIVO_INDIVIDUAL, ranking_individual)
    mostrar_alerta(f"Socio {jugador_socio} inscrito con éxito en el ranking individual.")
    mostrar_alerta("¡Inscripción exitosa!")
    return ranking_individual

def normalizar_nombre_equipo(nombre):
    """Normaliza el nombre del equipo para evitar duplicados por mayúsculas/minúsculas y espacios."""
    return re.sub(r'\s+', ' ', nombre.strip().lower())


def equiposIguales(ranking_dobles):
    """Verifica si un equipo ya existe en el ranking de dobles."""
    equipo = input("Ingrese el nombre del equipo: ").strip().lower()
    while encontrar_equipo(ranking_dobles, equipo):
        print("El nombre de equipo ya existe. Elija otro.")
        equipo = input("Ingrese el nombre del equipo: ").strip().lower()
    return normalizar_nombre_equipo(equipo)


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
        guardar_datos(ARCHIVO_DOBLES, ranking_dobles)
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
        return 1
    elif gano == 0:
        mostrar_alerta(f"¡{jugador} ha perdido el partido!")
        return 0
    else:
        mostrar_alerta("Operación cancelada. Volviendo al menú principal.")
        return None


def sumar_puntos(ranking_individual, socios_validos):
    """Suma 3 puntos en el ranking individual si gana."""

    print("Introduzca su número de socio para modificar el ranking:")

    nro_socio = socio(socios_validos)

    if nro_socio is None:
        return ranking_individual

    if encontrar_Jugador(ranking_individual, nro_socio) == True:
        if partido(nro_socio) == 1:
            for jugador in ranking_individual:
                if jugador[0] == nro_socio:
                    jugador[1] += 3
                    mostrar_alerta(f"Se han sumado 3 puntos al socio {jugador[0]}.")
            guardar_datos(ARCHIVO_INDIVIDUAL, ranking_individual)

    else:
        mostrar_alerta("El socio no está registrado en el ranking individual.")

    return ranking_individual


def sumar_Puntos_dobles(ranking_dobles):
    """Suma 3 puntos al equipo en el ranking de dobles si gana."""

    nombre_equipo = input("Ingrese el nombre del equipo para modificar el ranking: ").strip()   

    if encontrar_equipo(ranking_dobles, nombre_equipo) == True:
        if partido(nombre_equipo) == 1:
            nombre_buscado = normalizar_nombre_equipo(nombre_equipo)
            for equipo in ranking_dobles:
                if normalizar_nombre_equipo(equipo[0]) == nombre_buscado:
                    equipo[3] += 3
                    mostrar_alerta(f"Se han sumado 3 puntos al equipo {equipo[0]}.")
            guardar_datos(ARCHIVO_DOBLES, ranking_dobles)
    else: 
        mostrar_alerta("El equipo no se encuentra registrado en el ranking de dobles.")

    return ranking_dobles


def encontrar_Jugador(ranking_individual, jugador):
    """Verifica si un jugador está registrado en el ranking individual."""

    coincidencias = list(filter(lambda x: x[0] == jugador, ranking_individual))
    return len(coincidencias) > 0


def encontrar_equipo(ranking_dobles, equipo):
    """Verifica si un equipo está registrado en el ranking de dobles."""
    equipo_buscado = normalizar_nombre_equipo(equipo)
    resultado = list(filter(lambda x: normalizar_nombre_equipo(x[0]) == equipo_buscado, ranking_dobles))
    return len(resultado) > 0

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
    if not Individual:
        print("No hay jugadores registrados.")
    else:
        lineas_individuales = list(map(lambda j: f"Socio: {j[0]} | Puntos: {j[1]}", Individual))
        for linea in lineas_individuales:
            print(linea)

    print("\n=== RANKING DOBLES ===")
    if not Dobles:
        print("No hay equipos registrados.")
    else:
        lineas_dobles = list(map(lambda e: f"Equipo: {e[0]} | Jugadores: {e[1]}, {e[2]} | Puntos: {e[3]}", Dobles))
        for linea in lineas_dobles:
            print(linea)


    if Individual:
        total_puntos_ind = reduce(lambda acumulador, j: acumulador + j[1], Individual, 0)
        print(f"\n[Estadística] Total de puntos repartidos en individual: {total_puntos_ind}")

    if Dobles:
        total_puntos_dob = reduce(lambda acumulador, e: acumulador + e[3], Dobles, 0)
        print(f"[Estadística] Total de puntos repartidos en dobles: {total_puntos_dob}")

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

    global ranking_individual, ranking_dobles

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Inscribirse en ranking individual")
        print("2. Inscribirse en ranking de dobles")
        print("3. Registrar resultado de partido individual")
        print("4. Registrar resultado de partido de dobles")
        print("5. Mostrar rankings")
        print("6. Salir")

        opcion = opciones()

        global SOCIOS_VALIDOS
        SOCIOS_VALIDOS = obtener_socios_validos()

        if opcion == 1:
            ranking_individual = Anotar_individual(ranking_individual, SOCIOS_VALIDOS)
        elif opcion == 2:
            ranking_dobles = Anotar_dobles(ranking_dobles, SOCIOS_VALIDOS)
        elif opcion == 3:
            ranking_individual = sumar_puntos(ranking_individual, SOCIOS_VALIDOS)
        elif opcion == 4:
            ranking_dobles = sumar_Puntos_dobles(ranking_dobles)
        elif opcion == 5:
            mostrar_ranking(ranking_individual, ranking_dobles)
        elif opcion == 6:
            print("Saliendo del programa...")
            break

if __name__ == "__main__":
    Ranking()