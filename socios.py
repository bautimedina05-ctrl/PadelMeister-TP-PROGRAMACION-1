socios=[]
dnis=[]
numerodesocios=[]

def agregar_socio(socios, dnis, numerodesocios):
    numerorepetido = True

    """Agrega un nuevo socio al sistema."""
    socio=input("Ingrese el nombre del socio: ")
    socios.append(socio)
    dni=input("Ingrese el DNI del socio: ")
    dnis.append(dni)
    numerodesocio=len(socios)-1
    while numerorepetido==True:
        if numerodesocio in numerodesocios:
            numerodesocio+=1
        else:
            numerorepetido=False
    numerodesocios.append(numerodesocio)
    print("Socio agregado exitosamente. Su " "número de socio es:", numerodesocio)
    return socios, dnis, numerodesocios

def buscar_socio(socios, dnis, numerodesocios):
    """Busca un socio por su número de socio."""
    numero=int(input("Ingrese el número de socio a buscar: "))
    if numero in numerodesocios:

        print("Socio encontrado:")
        print("Nombre:", socios[numero])
        print("DNI:", dnis[numero])
    else:
        print("No se encontró ningún socio con ese número.")

def modificar_socio(socios, dnis, numerodesocios):
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

def eliminar_socio(socios, dnis, numerodesocios):
    """Elimina un socio del sistema."""
    numero = int(input("Ingrese el número de socio a eliminar: "))

    if numero in numerodesocios:
        socios.pop(numero)
        dnis.pop(numero)
        numerodesocios.pop(numero)


        print("Socio eliminado correctamente.")
    else:
        print("No encontrado.")

def mostrar_socios(socios, dnis, numerodesocios):
    """Muestra la lista de socios registrados."""
    if socios:
        print("Lista de socios:")
        for i in range(len(socios)):
            print("Número de socio:", numerodesocios[i])
            print("Nombre:", socios[i])
            print("DNI:", dnis[i])
            
    else:
        print("No hay socios registrados.")

def menusocios():
    opcion=0
    """Muestra el menú de opciones para gestionar socios."""
    while opcion!="6":
        print("--- Menú de Socios ---")
        print("1. Agregar socio")
        print("2. Buscar socio")
        print("3. Modificar socio")
        print("4. Eliminar socio")
        print("5. Mostrar socios")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        print("----------------------------------------")

        if opcion == "1":
            agregar_socio(socios, dnis, numerodesocios)
        elif opcion == "2":
            buscar_socio(socios, dnis, numerodesocios)
        elif opcion == "3":
            modificar_socio(socios, dnis, numerodesocios)
        elif opcion == "4":
            eliminar_socio(socios, dnis, numerodesocios)
        elif opcion == "5":
            mostrar_socios(socios, dnis, numerodesocios)
        elif opcion == "6":
            print("Saliendo del menú de socios.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menusocios()