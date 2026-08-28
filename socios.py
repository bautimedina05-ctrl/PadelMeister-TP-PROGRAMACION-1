socios=[]
dnis=[]
numerodesocios=[]
def agregar_socio():
    """Agrega un nuevo socio al sistema."""
    socio=input("Ingrese el nombre del socio: ")
    socios.append(socio)
    dni=input("Ingrese el DNI del socio: ")
    dnis.append(dni)
    numerodesocio=len(socios)-1
    numerodesocios.append(numerodesocio)
    print("Socio agregado exitosamente. Su " "número de socio es:", numerodesocio)
    return socios, dnis, numerodesocios

def buscar_socio():
    """Busca un socio por su número de socio."""
    numero=int(input("Ingrese el número de socio a buscar: "))
    if numero in numerodesocios:

        print("Socio encontrado:")
        print("Nombre:", socios[numero])
        print("DNI:", dnis[numero])
    else:
        print("No se encontró ningún socio con ese número.")

def modificar_socio():
    """Modifica los datos de un socio existente."""
    numero = int(input("Ingrese el número de socio: "))

    if numero in numerodesocios:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_dni = input("Ingrese el nuevo DNI: ")

        socios[numero] = nuevo_nombre
        dnis[numero] = nuevo_dni

        print("Socio modificado correctamente.")
    else:
        print("Numero de socio no encontrado.")

def eliminar_socio():
    """Elimina un socio del sistema."""
    numero = int(input("Ingrese el número de socio a eliminar: "))

    if numero in numerodesocios:
        socios.pop(numero)
        dnis.pop(numero)
        numerodesocios.pop(numero)


        print("Socio eliminado correctamente.")
    else:
        print("No encontrado.")

def mostrar_socios():
    """Muestra la lista de socios registrados."""
    if socios:
        print("Lista de socios:")
        for i in range(len(socios)):
            print("Número de socio: {numerodesocios[i]}, Nombre: {socios[i]}, DNI: {dnis[i]}")
    else:
        print("No hay socios registrados.")