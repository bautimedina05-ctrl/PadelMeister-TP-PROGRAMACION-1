def reserva_cancha(reservado, disponible):
    print("Los horarios disponibles para su reserva son: ")
    for i in range(len(disponible)):
        print(i, "- ", disponible[i])
    seleccionada = int(input("Ingrese el numero de horario que desee: "))
    horario = disponible[seleccionada]
    reservado.append(horario)
    del disponible[seleccionada]
    return horario

def nombre_reserva(hora):
    nombre= input("Ingrese su nombre para registrar su reserva a las "+ hora + " :")
    return nombre
    

def alquiler_cancha(matriz,reservado, disponible):
    horario= reserva_cancha(reservado, disponible)
    nombre= nombre_reserva(horario)
    matriz.append([horario, "Ocupado", nombre])

def mostrar_reservas(matriz):
    print("------RESERVAS------")
    for i in range(len(matriz)):
        print(matriz[i][0], " | ", matriz[i][1], " | ", matriz[i][2])
    

matriz =[["Horario", "Estado", "Nombre Reserva"]]
reservado=[]
opcion= 0
disponible =["16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00", "00:00"]
while opcion != -1:
    opcion= int(input("ingresa"))
    if opcion== -1:
        break
    else:
        alquiler_cancha(matriz, reservado, disponible)
mostrar_reservas(matriz)
    