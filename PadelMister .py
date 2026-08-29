def socio(socios):
    nro_socio = input("Ingrese su número de socio: ")
    while nro_socio not in socios:
        print("Numero de socio inexistente. Por favor, ingrese un número válido.")
        nro_socio = input("Ingrese su número de socio: ")
    return nro_socio

def anotado(anotados):
    print("Bienvenido al apartado de torneos de PadelMeister")
    print("Para poder inscribirse en un torneo, primero debe ingresar su número de socio.")
    nro_socio = socio()
    jugador = JugadorAnotado(anotados, nro_socio)
    if jugador == False:
        print("No puede inscribirse nuevamente en el torneo.")
        anotados.append(nro_socio)
    print("¡Inscripción exitosa!")
    return anotados

def JugadorAnotado(anotados, nro_socio):
    if nro_socio in anotados:
        print("El jugador ya está anotado en el torneo.")
        return True
    else:
        return False

