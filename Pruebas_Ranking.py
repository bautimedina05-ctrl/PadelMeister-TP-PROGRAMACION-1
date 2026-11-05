#Pruebas_Ranking

# Importamos las funciones principales del sistema a testear
# (Suponiendo que el código anterior se llama 'padelmeister.py')
from Ranking_torneo import (
    normalizar_nombre_equipo,
    esta_anotado,
    esta_anotado_dobles,
    encontrar_Jugador,
    encontrar_equipo,
    ordenar_ranking_Individual
)

def prueba_normalizar_nombre():
    print("Ejecutando: prueba_normalizar_nombre...")
    entrada = "   PAREJA   número   UNO   "
    resultado = normalizar_nombre_equipo(entrada)
    esperado = "pareja número uno"
    
    if resultado == esperado:
        print("Prueba correcta")
    else:
        print(f"Error en la prueba. Obtenido: '{resultado}', Esperado: '{esperado}'")

def prueba_esta_anotado():
    print("Ejecutando: prueba_esta_anotado...")
    ranking_ejemplo = [[101, 6], [102, 3], [103, 0]]
    
    # Caso 1: Jugador existente
    res1 = esta_anotado(ranking_ejemplo, 102)
    # Caso 2: Jugador inexistente
    res2 = esta_anotado(ranking_ejemplo, 999)
    
    if res1 == True and res2 == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba.")

def prueba_esta_anotado_dobles():
    print("Ejecutando: prueba_esta_anotado_dobles...")
    ranking_dobles_ejemplo = [
        ["los tigres", 101, 102, 6],
        ["los leones", 103, 104, 3]
    ]
    
    # Socio presente en un equipo
    res1 = esta_anotado_dobles(ranking_dobles_ejemplo, 102)
    # Socio no presente
    res2 = esta_anotado_dobles(ranking_dobles_ejemplo, 500)
    
    if res1 == True and res2 == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba.")

def prueba_encontrar_jugador_y_equipo():
    print("Ejecutando: prueba_encontrar_jugador_y_equipo...")
    ranking_ind = [[101, 9], [102, 3]]
    ranking_dob = [["Los cracks", 101, 102, 6]]
    
    # Búsqueda individual
    r_ind = encontrar_Jugador(ranking_ind, 101)
    # Búsqueda de equipo (probando normalización de mayúsculas/minúsculas)
    r_dob = encontrar_equipo(ranking_dob, "  LOS cracks  ")
    
    if r_ind == True and r_dob == True:
        print("Prueba correcta")
    else:
        print("Error en la prueba.")

def prueba_ordenamiento():
    print("Ejecutando: prueba_ordenamiento...")
    ranking_ind = [[101, 3], [102, 12], [103, 6]]
    
    ordenado = ordenar_ranking_Individual(ranking_ind)
    # El orden esperado de mayor a menor según los puntos debería ser 102 (12pts), 103 (6pts), 101 (3pts)
    esperado = [[102, 12], [103, 6], [101, 3]]
    
    if ordenado == esperado:
        print("Prueba correcta")
    else:
        print(f"Error en la prueba. Obtenido: {ordenado}, Esperado: {esperado}")

# Ejecución de todas las pruebas en secuencia
if __name__ == "__main__":
    print("=== INICIANDO BATERÍA DE PRUEBAS PARA PADELMEISTER ===")
    prueba_normalizar_nombre()
    print("-" * 50)
    prueba_esta_anotado()
    print("-" * 50)
    prueba_esta_anotado_dobles()
    print("-" * 50)
    prueba_encontrar_jugador_y_equipo()
    print("-" * 50)
    prueba_ordenamiento()
    print("=== FIN DE LAS PRUEBAS ===")