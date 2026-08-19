def reserva_cancha(reservado, disponible):
    print("Los horarios disponibles para su reserva son: ")
    for i in range(len(disponible)):
        print(i, "- ", disponible[i])
    seleccionada = int(input("Ingrese el numero de horario que desee: "))
    horario = disponible[seleccionada]
    reservado.insert(seleccionada, horario)
    del disponible[seleccionada]
    return horario

def horarios_canchas():
    reservado=[]
    disponible=["16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00", "00:00"]
    horario= reserva_cancha(reservado, disponible)
    print("El horario seleccionado es: " , horario)
    print("el resto de horarios es: ", disponible)
    print("el resto de horarios es: ", reservado)
    

def alquiler_cancha():
    matriz=[["Horario", "Estado", "Nombre Reserva"]]
    horario= horarios_canchas()
    


alquiler_cancha()