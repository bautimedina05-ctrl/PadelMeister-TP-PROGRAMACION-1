def Agregar_socios():
    socio = int(input("Ingrese el número de socios a agregar: "))
    if socio <= 0:
        print("El número de socios debe ser mayor que cero.")
        socio = int(input("Ingrese el número de socios a agregar: "))
    return socio

def Agregar_datos(socio):
    Socios = []
    for i in range(socio):
        nombre = input("Ingrese el nombre del socio: ")
        apellido = input("Ingrese el apellido del socio: ")
        edad = int(input("Ingrese la edad del socio: "))
        telefono = input("Ingrese el número de teléfono del socio: ")
        Socios.append([nombre, apellido, edad])

def estado_cuota():
    """ da a conocer el estado de la cuota de los socios siendo los estados: al dia, atrasada, y no paga """
    pass