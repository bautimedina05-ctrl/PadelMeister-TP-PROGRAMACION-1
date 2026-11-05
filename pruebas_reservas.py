from reservas_cancha import HORARIOS, crear_reserva, conjunto_ocupados, horario_esta_libre, horarios_libres, cargar_reservas


def mostrar_resultado(funcion, datos, esperado, obtenido):
    """Muestra el detalle de una prueba y si fue aprobada o fallida."""
    print("Funcion:", funcion)
    print("Datos:", datos)
    print("Esperado:", esperado)
    print("Obtenido:", obtenido)
    if esperado == obtenido:
        print("Resultado: APROBADA")
    else:
        print("Resultado: FALLIDA")
    print("----------")


def prueba_crear_reserva_valida():
    esperado = {"nombre": "Juan", "cancha": 2, "horario": "18:00"}
    obtenido = crear_reserva("Juan", 2, "18:00")
    mostrar_resultado("crear_reserva", "Juan, 2, 18:00", esperado, obtenido)


def prueba_horario_libre_valido():
    reservas = [{"nombre": "Juan", "cancha": 2, "horario": "18:00"}]
    esperado = True
    obtenido = horario_esta_libre(reservas, 1, "18:00")
    mostrar_resultado("horario_esta_libre", "reserva Juan c2 18:00, consulta c1 18:00", esperado, obtenido)


def prueba_horarios_libres_valido():
    reservas = [{"nombre": "Juan", "cancha": 2, "horario": "18:00"}]
    esperado = ["16:00", "17:00", "19:00", "20:00", "21:00", "22:00", "23:00", "00:00"]
    obtenido = horarios_libres(reservas, 2)
    mostrar_resultado("horarios_libres", "reserva Juan c2 18:00, consulta c2", esperado, obtenido)


def prueba_conjunto_ocupados_valido():
    reservas = [crear_reserva("Juan", 2, "18:00"), crear_reserva("Ana", 1, "16:00")]
    esperado = {(2, "18:00"), (1, "16:00")}
    obtenido = conjunto_ocupados(reservas)
    mostrar_resultado("conjunto_ocupados", "Juan c2 18:00 y Ana c1 16:00", esperado, obtenido)


def prueba_horario_ocupado_invalido():
    reservas = [crear_reserva("Juan", 2, "18:00")]
    esperado = False
    obtenido = horario_esta_libre(reservas, 2, "18:00")
    mostrar_resultado("horario_esta_libre", "reserva Juan c2 18:00, consulta c2 18:00", esperado, obtenido)


def prueba_cargar_archivo_inexistente():
    esperado = []
    obtenido = cargar_reservas("no_existe.json")
    mostrar_resultado("cargar_reservas", "no_existe.json", esperado, obtenido)


def prueba_conjunto_duplicados_invalido():
    reservas = [crear_reserva("Juan", 2, "18:00"), crear_reserva("Ana", 2, "18:00")]
    esperado = {(2, "18:00")}
    obtenido = conjunto_ocupados(reservas)
    mostrar_resultado("conjunto_ocupados", "Juan y Ana, ambas c2 18:00", esperado, obtenido)


def prueba_cancha_llena_limite():
    reservas = [crear_reserva("x", 1, h) for h in HORARIOS]
    esperado = []
    obtenido = horarios_libres(reservas, 1)
    mostrar_resultado("horarios_libres", "9 reservas en cancha 1, una por horario", esperado, obtenido)


def prueba_sin_reservas_limite():
    esperado = set()
    obtenido = conjunto_ocupados([])
    mostrar_resultado("conjunto_ocupados", "lista vacia", esperado, obtenido)


def prueba_misma_hora_dos_canchas():
    reservas = [crear_reserva("Juan", 1, "18:00"), crear_reserva("Ana", 2, "18:00")]
    esperado = {(1, "18:00"), (2, "18:00")}
    obtenido = conjunto_ocupados(reservas)
    mostrar_resultado("conjunto_ocupados", "Juan c1 18:00 y Ana c2 18:00", esperado, obtenido)


prueba_crear_reserva_valida()
prueba_horario_libre_valido()
prueba_horarios_libres_valido()
prueba_conjunto_ocupados_valido()
prueba_horario_ocupado_invalido()
prueba_cargar_archivo_inexistente()
prueba_conjunto_duplicados_invalido()
prueba_cancha_llena_limite()
prueba_sin_reservas_limite()
prueba_misma_hora_dos_canchas()

