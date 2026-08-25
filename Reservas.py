

#Funciones de Reserva

def reserva_cancha(reservado, disponible):
    """Permite seleccionar un horario disponible para reservar una cancha. Muestra los horarios libres, recibe la elección del usuario, agrega el horario seleccionado a la lista de reservados, lo elimina de la lista de disponibles y devuelve el horario elegido."""
    print("Los horarios disponibles para su reserva son: ")
    for i in range(len(disponible)):
        print(i, "- ", disponible[i])
    seleccionada = int(input("Ingrese el numero de horario que desee: "))
    horario = disponible[seleccionada]
    reservado.append(horario)
    del disponible[seleccionada]
    return horario

def nombre_reserva(hora):
    """Permite ingresar el nombre del usuario para registrar su reserva."""
    nombre= input("Ingrese su nombre para registrar su reserva a las "+ hora + " :")
    return nombre
    

def alquiler_cancha(matriz,reservado, disponible):
    """Permite realizar una reserva de cancha. Llama a las funciones reserva_cancha y nombre_reserva para obtener el horario y el nombre del usuario, y luego agrega esta información a la matriz de reservas."""
    horario= reserva_cancha(reservado, disponible)
    nombre= nombre_reserva(horario)
    matriz.append([horario, "Ocupado", nombre])


#Mostrar alquileres

def mostrar_reservas(matriz):
    """Muestra todas las reservas realizadas en la matriz de reservas."""
    print("------RESERVAS------")
    for i in range(len(matriz)):
        print(matriz[i][0], " | ", matriz[i][1], " | ", matriz[i][2])


#Opciones ALQUILER

<<<<<<< HEAD
def opciones_alquiler():
    """Muestra un menú de opciones relacionadas con el alquiler de canchas. Permite al usuario elegir entre agregar un alquiler, ver las reservas existentes o volver al menú principal."""
=======
def opciones_alquiler(matriz, reservado, disponible):
>>>>>>> a42dd58e8a8f4364f82e9d0e6fae39878edbffb3
    lista= ["Agregar Alquiler", "Reservas", "Volver Atras"]
    print("--ELIJA OPCION DESEADA--")
    for i in range(len(lista)):
        print(i, "- ", lista[i])
    sel = int(input("Ingrese el indice de la opcion deseada: "))
    while sel > 2 and sel <0:
        sel= int(input("Opcion no valida, reingrese porfavor: "))
    if sel == 0:
        alquiler_cancha(matriz, reservado, disponible)
    elif sel== 1:
        mostrar_reservas()
    else:
        presentar_opciones()
    



#Funciones Menu

<<<<<<< HEAD
def presentar_opciones():
    """Muestra un menú principal con opciones disponibles para el usuario. Permite al usuario elegir entre diferentes secciones del sistema."""
=======
def presentar_opciones(matriz, reservado, disponible):
>>>>>>> a42dd58e8a8f4364f82e9d0e6fae39878edbffb3
    lista= ["Alquiler CANCHA", "TIENDA", "SOCIOS", "TORNEOS", "RANKING"]
    print("--ELIJA OPCION DESEADA--")
    for i in range(len(lista)):
        print(i, "- ", lista[i])
    sel= int(input("Ingrese el indice de la opcion deseada: "))
    opcion= lista[sel]
    return opcion


    
        

    
#PRINCIPAL
matriz =[["Horario", "Estado", "Nombre Reserva"]]
reservado=[]
opcion= 0
disponible =["16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00", "00:00"]

opcionmain= presentar_opciones(matriz, reservado, disponible)
if opcion== 0:
    opciones_alquiler(matriz, reservado, disponible)


     
