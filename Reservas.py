precio=5000


def reservas():
    horarios=["08:00","09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00"]
    for i in range(len(horarios)):
        print(i, horarios[i])
    horario = int(input("seleccione el horario que desea reservar: "))
    reservados=[]
    if horario in reservados:
        print("El horario ya está reservado. Por favor, seleccione otro horario.")
    else:
        print("El importe por el horario seleccionado es de: .", precio)
        x = input("¿Desea reservar este horario? Y=0/N=1: ")
        if x == "0":
            reservados.append(horario)
            print("Su horario ha sido reservado con éxito.")
        else:
            print("No se ha realizado ninguna reserva.")

reservas()