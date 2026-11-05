import Compras
import socios
import Ranking_torneo
from reservas_cancha import HORARIOS, crear_reserva, conjunto_ocupados, horario_esta_libre, horarios_libres, cargar_reservas, guardar_reservas

#Historiales 

def registrar_historial(reserva):
    archivo = open("historial.txt", "a")
    archivo.write("cancha" + str(reserva["cancha"]) + " | " + reserva["horario"] + " | " + reserva["nombre"] + "write")
    archivo.close()

def leer_historial():
    try:
        archivo= open("historial.txt", "r")
        for linea in archivo:
            print(linea.strip())
        archivo.close()
    except FileNotFoundError:
        print("No hay historial Todavia")


#Funciones de Reserva
def pedir_entero(mensaje):
    """Pide un numero entero por teclado y repite hasta que sea valido"""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un numero entero, intente de nuevo")


def numero_cancha():
    """Permite seleccionar la cancha a la que se desea alquilar"""
    print("1 - Cancha 1")
    print("2 - Cancha 2")
    seleccionada= pedir_entero("Ingrese el numero de cancha que desee: ")
    while seleccionada < 1 or seleccionada > 2:
        seleccionada= pedir_entero("Cancha no Valida, Reingrese: ")
    return seleccionada


def nombre_reserva(hora):
    """Permite ingresar el nombre del usuario para registrar su reserva."""
    nombre= input("Ingrese su nombre para registrar su reserva a las "+ hora + " :")
    return nombre
    

def alquiler_cancha(reservas):
    cancha = numero_cancha()
    libres= horarios_libres(reservas, cancha)
    if len(libres)== 0:
        print("No quedan horarios disponibles en esta cancha")
        return
    print("Los horarios disponibles son:")
    for i in range(len(libres)):
        print(i, "- ", libres[i])
    seleccionada= pedir_entero("Ingrese el numero de horario que desee: ")
    while seleccionada < 0 or seleccionada >= len(libres):
        seleccionada= pedir_entero("Horario no disponible, Reingrese: ")
    horario= libres[seleccionada]
    nombre= nombre_reserva(horario)
    reserva = crear_reserva(nombre,cancha,horario)
    reservas.append(reserva)
    return reserva

        


#Mostrar alquileres

def mostrar_reservas(reservas):
    """Muestra todas las reservas realizadas en la matriz de reservas."""
    print("------RESERVAS CANCHAS------")
    if len(reservas)== 0:
        print("Todavia no Hay reservas.")
    for reserva in reservas:
        print("cancha " , reserva["cancha"], " | ", reserva["horario"], " | ", reserva["nombre"])
   



#Opciones ALQUILER

def opciones_alquiler(reservas):
    """Muestra un menú de opciones relacionadas con el alquiler de canchas. Permite al usuario elegir entre agregar un alquiler, ver las reservas existentes o volver al menú principal."""
    sel= -1
    lista= ["Agregar Alquiler", "Reservas", "Historial", "Volver Atras"]
    while sel != 3:
        print("--ELIJA OPCION DESEADA--")
        for i in range(len(lista)):
            print(i, "- ", lista[i])
        sel = pedir_entero("Ingrese el indice de la opcion deseada: ")
        while sel > 3 or sel <0:
            sel= pedir_entero("Opcion no valida, reingrese porfavor: ")
        if sel == 0:
            reserva = alquiler_cancha(reservas)
            if reserva is not None:
                guardar_reservas(reservas)
                registrar_historial(reserva)   
        elif sel== 1:
            mostrar_reservas(reservas)
        elif sel == 2:
            leer_historial()


    



#Funciones Menu

def presentar_opciones(reservas):
    """Muestra un menú principal con opciones disponibles para el usuario. Permite al usuario elegir entre diferentes secciones del sistema."""
    sel= -1
    while sel != 4:
        lista= ["Alquiler CANCHA", "TIENDA", "SOCIOS", "TORNEOS/ RANKING", "SALIR"]
        print("Bienvenido a PADELMEISTER")
        print("--ELIJA OPCION DESEADA--")
        for i in range(len(lista)):
            print(i, "- ", lista[i])
        sel= pedir_entero("Ingrese el indice de la opcion deseada: ")
        while sel > 4 or sel < 0:
            sel= pedir_entero("Opcion No valida, reingrese porfavor: ")
        if sel == 0:
            opciones_alquiler(reservas)
        elif sel == 1:
            Compras.tienda()
        elif sel == 2:
            socios.menusocios(socios.socios, socios.dnis, socios.numerodesocios, socios.estadosocios, socios.tipodocs)
        elif sel == 3:
            Ranking_torneo.Ranking()
        elif sel == 4:
            print("Gracias por utilizar el sistema Padel Meister.")
            break


    
        

    
#PRINCIPAL
reservas= cargar_reservas()
presentar_opciones(reservas)
