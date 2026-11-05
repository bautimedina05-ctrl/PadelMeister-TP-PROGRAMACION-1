import json
HORARIOS = ("16:00","17:00", "18:00","19:00","20:00","21:00","22:00","23:00", "00:00")

def conjunto_ocupados(reservas):
    ocupados = set()
    for reserva in reservas:
        ocupados.add((reserva["cancha"], reserva["horario"]))
    return ocupados

def horarios_libres(reservas, cancha):
    return [h for h in HORARIOS if horario_esta_libre(reservas,cancha,h)]

def horario_esta_libre(reservas, cancha, horario):
    return (cancha, horario) not in conjunto_ocupados(reservas)

def crear_reserva(nombre,cancha,horario):
    reserva= {
        "nombre": nombre,
        "cancha": cancha,
        "horario": horario
    }
    return reserva

def cargar_reservas(nombre_archivo = "reservas.json"):
    try:
        archivo = open(nombre_archivo, "r")
        reservas = json.load(archivo)
        archivo.close()
        return reservas
    except FileNotFoundError:
        return []

def guardar_reservas(reservas, nombre_archivo = "reservas.json"):
    """Guarda la lista de reservas en reservas.json."""
    archivo = open(nombre_archivo, "w")
    json.dump(reservas, archivo, indent=4)
    archivo.close()





