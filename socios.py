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
    numero = int(input("Ingrese el número de socio: "))

    if numero in numerodesocios:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_dni = input("Ingrese el nuevo DNI: ")

        socios[numero] = nuevo_nombre
        dnis[numero] = nuevo_dni

        print("Socio modificado correctamente.")
    else:
        print("No existe ese socio.")

def eliminar_socio():
    numero = int(input("Ingrese el número de socio a eliminar: "))

    if numero in numerodesocios:
        socios.pop(numero)
        dnis.pop(numero)
        numerodesocios.pop(numero)

        for i in range(len(numerodesocios)):
            numerodesocios[i] = i

        print("Socio eliminado correctamente.")
    else:
        print("No existe ese número de socio.")