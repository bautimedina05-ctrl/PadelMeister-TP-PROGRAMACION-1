
#Funciones de Reserva

def numero_cancha():
    """Permite seleccionar la cancha a la que se desea alquilar"""
    canchas=[0,1, 2]
    for i in range(1,3):
            print(i, "- Cancha", canchas[i])
    seleccionada = int(input("Ingrese el numero de horario que desee: "))
    return seleccionada


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
    

def alquiler_cancha(matriz1, matriz2, reservado1, reservado2 , disponible1, disponible2):
    """Permite realizar una reserva de cancha. Llama a las funciones reserva_cancha y nombre_reserva para obtener el horario y el nombre del usuario, y luego agrega esta información a la matriz de reservas."""
    cancha= numero_cancha()
    if cancha == 1:
        horario= reserva_cancha(reservado1, disponible1)
    elif cancha == 2:
        horario= reserva_cancha(reservado2, disponible2)
    nombre= nombre_reserva(horario)
    if cancha == 1:
        matriz1.append([horario, "Ocupado", nombre])
    elif cancha== 2:
        matriz2.append([horario, "Ocupado", nombre])
    return


#Mostrar alquileres

def mostrar_reservas(matriz):
    """Muestra todas las reservas realizadas en la matriz de reservas."""
    print("------RESERVAS CANCHAS------")
    for i in range(len(matriz)):
        print(matriz[i][0], " | ", matriz[i][1], " | ", matriz[i][2])


#Opciones ALQUILER

def opciones_alquiler(matriz1, matriz2, reservado1, reservado2 , disponible1, disponible2):
    """Muestra un menú de opciones relacionadas con el alquiler de canchas. Permite al usuario elegir entre agregar un alquiler, ver las reservas existentes o volver al menú principal."""
    lista= ["Agregar Alquiler", "Reservas", "Volver Atras"]
    print("--ELIJA OPCION DESEADA--")
    for i in range(len(lista)):
        print(i, "- ", lista[i])
    sel = int(input("Ingrese el indice de la opcion deseada: "))
    while sel > 2 and sel <0:
        sel= int(input("Opcion no valida, reingrese porfavor: "))
    while sel != 2:
        if sel == 0:
            alquiler_cancha(matriz1, matriz2, reservado1, reservado2 , disponible1, disponible2)
        elif sel== 1:  
            mostrar_reservas(matriz1)
            print("")
            mostrar_reservas(matriz2)
            volver= int(input("PRESIONE 1 PARA VOLVER: "))
            while volver != 1:
                volver= int(input("NUMERO INVALIDO,PRESIONE 1 PARA VOLVER: "))
            return
        opciones_alquiler(matriz1, matriz2, reservado1, reservado2 , disponible1, disponible2)

            
    else:
        presentar_opciones()
    



#Funciones Menu

def presentar_opciones():
    """Muestra un menú principal con opciones disponibles para el usuario. Permite al usuario elegir entre diferentes secciones del sistema."""
    lista= ["Alquiler CANCHA", "TIENDA", "SOCIOS", "TORNEOS", "RANKING"]
    print("--ELIJA OPCION DESEADA--")
    for i in range(len(lista)):
        print(i, "- ", lista[i])
    sel= int(input("Ingrese el indice de la opcion deseada: "))
    opcion= lista[sel]
    return opcion


    
        

    
#PRINCIPAL
matriz1 =[["Horario", "Estado", "Nombre Reserva"]]
matriz2 =[["Horario", "Estado", "Nombre Reserva"]]
reservado1=[]
reservado2=[]
opcion= 0
disponible1 =["16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00", "00:00"]
disponible2 =["16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00", "00:00"]

opcionmain= presentar_opciones()
if opcion== 0:
    opciones_alquiler(matriz1, matriz2, reservado1, reservado2 , disponible1, disponible2)


     
