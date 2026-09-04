socios=[]
dnis=[]
numerodesocios=[]
estadosocios=[]
def validar_dni(dni):
    """Valida un numero tengam digitos y que no sea posible introducir otro caracter que no sea numero. En este caso para validadr que el dni sea un numero valido."""
    if len(dni) == 0:
        return False
    
    digitos = "0123456789"
    for caracter in dni:
        if caracter not in digitos:
            return False  
            
    return True
def agregar_socio(socios, dnis, numerodesocios, estadosocios):

    """Agrega un nuevo socio al sistema."""
    socio=input("Ingrese el nombre del socio: ")
    socios.append(socio)
    dni=input("Ingrese el DNI del socio: ")
    numerovalido=validar_dni(dni)
    if dni in dnis or numerovalido==False:
        print("El DNI ya está registrado o no es un numero valido. No se puede agregar el socio.")
        socios.pop()
        return socios, dnis, numerodesocios, estadosocios
    dnis.append(dni)
    estadosocios.append("activo")
    if len(numerodesocios) == 0:
        numerodesocio = 0
    else:
        numerodesocio = max(numerodesocios) + 1

    numerodesocios.append(numerodesocio)
    print("Socio agregado exitosamente. Su " "número de socio es:", numerodesocio)
    return socios, dnis, numerodesocios, estadosocios
def busqueda(numero, lista):
    """Busqueda secuencial para encontrar el índice de una lista"""
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
def buscar_socio(socios, dnis, numerodesocios, estadosocios):
    """Busca un socio por su número de socio."""
    numeroodni=input("¿Usted desea buscar el socio por numero de socio o por dni? 1. Numero de socio 2. DNI: ")
    if numeroodni == "1":
        numero=int(input("Ingrese el número de socio a buscar: "))
        if numero in numerodesocios:
            x = busqueda(numero, numerodesocios)
            print("Socio encontrado:")
            print("Número de socio:", numerodesocios[x])
            print("Nombre:", socios[x])
            print("DNI:", dnis[x])
            print("Estado:", estadosocios[x])

        else: 
            print("No se encontró ningún socio con ese número.")
            return
    elif numeroodni == "2":
        dni=input("Ingrese el DNI del socio a buscar: ")
        if dni in dnis:
            x = busqueda(dni, dnis)
            print("Socio encontrado:")
            print("Número de socio:", numerodesocios[x])
            print("Nombre:", socios[x])
            print("DNI:", dnis[x])
            print("Estado:", estadosocios[x])
        else:
            print("No se encontró ningún socio con ese DNI.")
        return
    else:
        print("Opción inválida.")
        
def modificar_socio(socios, dnis, numerodesocios, estadosocios):
    """Modifica los datos de un socio existente."""
    numero = int(input("Ingrese el número de socio: "))
    if numero not in numerodesocios:
        print("Número de socio no encontrado.")
        return
    x = busqueda(numero, numerodesocios)
    print("¿Está seguro de que desea modificar los datos del socio ", socios[x], "?")
    confirmacion=input("Ingrese cualquier tecla para confirmar o 2 para cancelar: ")
    if confirmacion=="2":
        print("No se modificaron los datos del socio.")
        return
    if numero in numerodesocios:
        x=busqueda(numero, numerodesocios)
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nuevo_dni = input("Ingrese el nuevo DNI: ")
        validar=validar_dni(nuevo_dni)
        if validar==False:
            print("El DNI ingresado no es válido. No se puede modificar el socio.")
            return

        socios[x] = nuevo_nombre
        dnis[x] = nuevo_dni

        print("Socio modificado correctamente.")
    else:
        print("Numero de socio no encontrado.")
def estadodelsocio(socios, dnis, numerodesocios, estadosocios):
    """Modifica el estado de un socio a sancionado o inactivo."""
    numero = int(input("Ingrese el número de socio: "))
    if numero not in numerodesocios:
        print("Número de socio no encontrado.")
        return
    x = busqueda(numero, numerodesocios)
    if x is not None:
        print("Ingrese el nuevo estado del socio", socios[x] , ": ")
        print("1. Activo")
        print("2. Inactivo")
        print("3. Sancionado")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            estadosocios[x] = "activo"
        elif opcion == "2":
            estadosocios[x] = "inactivo"
        elif opcion == "3":
            estadosocios[x] = "sancionado"
        else:
            print("Opción inválida. No se modificó el estado del socio.")
            return
        

        print("Estado del socio modificado correctamente.")
        return estadosocios 
    else:
        print("Numero de socio no encontrado.")

def eliminar_socio(socios, dnis, numerodesocios, estadosocios):
    """Elimina un socio del sistema."""
    numero = int(input("Ingrese el número de socio a eliminar: "))

    if numero in numerodesocios:
        x = busqueda(numero, numerodesocios)
        socios.pop(x)
        dnis.pop(x)
        numerodesocios.pop(x)
        estadosocios.pop(x)


        print("Socio eliminado correctamente.")
    else:
        print("No encontrado.")

def mostrar_socios(socios, dnis, numerodesocios, estadosocios):
    """Muestra la lista de socios registrados."""
    if socios:
        print("Lista de socios:")
        for i in range(len(socios)):
            print("..........................")
            print("Número de socio:", numerodesocios[i])
            print("Nombre:", socios[i])
            print("DNI:", dnis[i])
            print("Estado:", estadosocios[i])
            
    else:
        print("No hay socios registrados.")
    print("..........................")

def menusocios(socios, dnis, numerodesocios, estadosocios):
    opcion=0
    """Muestra el menú de opciones para gestionar socios."""
    while opcion!="7":
        print("--- Menú de Socios ---")
        print("1. Agregar socio")
        print("2. Buscar socio")
        print("3. Modificar socio")
        print("4. Eliminar socio")
        print("5. Mostrar socios")
        print("6. Cambiar estado del socio")
        print("7. Salir")


        opcion = input("Seleccione una opción: ")
        print("----------------------------------------")

        if opcion == "1":
            agregar_socio(socios, dnis, numerodesocios, estadosocios)
        elif opcion == "2":
            buscar_socio(socios, dnis, numerodesocios, estadosocios)
        elif opcion == "3":
            modificar_socio(socios, dnis, numerodesocios, estadosocios)
        elif opcion == "4":
            eliminar_socio(socios, dnis, numerodesocios, estadosocios)
        elif opcion == "5":
            mostrar_socios(socios, dnis, numerodesocios, estadosocios)
        elif opcion == "6":
            estadodelsocio(socios, dnis, numerodesocios, estadosocios)
        elif opcion == "7":
            print("Saliendo del menú de socios.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menusocios(socios, dnis, numerodesocios, estadosocios)