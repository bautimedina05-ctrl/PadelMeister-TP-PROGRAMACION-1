socios=[]
dnis=[]
tipodocs=[]
numerodesocios=[]
estadosocios=[]
lista_tipos = ["DNI", "Pasaporte"]
tipos_documento = tuple(lista_tipos)

def validar_dni(dni):
    """Valida un numero tengam digitos y que no sea posible introducir otro caracter que no sea numero. En este caso para validadr que el dni sea un numero valido."""
    if len(dni) == 0:
        return False
    
    digitos = "0123456789"
    for caracter in dni:
        if caracter not in digitos:
            return False  
    return True

def elegir_tipo_documento():
    """Muestra los tipos de documento posibles y devuelve el elegido."""
    print("Tipo de documento:")
    print("1.", tipos_documento[0])
    print("2.", tipos_documento[1])
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue
        if opcion == 1 or opcion == 2:
            return tipos_documento[opcion - 1]
        print("Opción inválida.")

def validar_pasaporte():
    MinL = 6
    MaxL = 9
    permitido = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    while True:
        pasaporte = input("Número de pasaporte: ")

        if " " in pasaporte:
            print("No se permiten espacios.")
        elif len(pasaporte) < MinL or len(pasaporte) > MaxL:
            print("Debe tener entre 6 y 9 caracteres validos segun la norma ICAO 9303")
        else:
            valido = True
            for letra in pasaporte:
                if letra not in permitido:
                    valido = False
            if valido:
                return pasaporte
            else:
                print("Solo se permiten letras mayusculas y números.")

def agregar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs):

    """Agrega un nuevo socio al sistema."""
    socio=input("Ingrese el nombre del socio: ")
    socios.append(socio)
    tipo_documento = elegir_tipo_documento()
    tipodocs.append(tipo_documento)


    if tipo_documento == "DNI":
        dni = input("Ingrese el número del DNI del socio: ")
        numerovalido = validar_dni(dni)
    else:
        dni = validar_pasaporte()
        numerovalido = True
    if dni in dnis or numerovalido==False:
        print("El " + tipo_documento + " ya está registrado o no es un número válido. No se puede agregar el socio.")
        socios.pop()
        tipodocs.pop()
        return socios, dnis, numerodesocios, estadosocios, tipodocs
    dnis.append(dni)
    estadosocios.append("activo")
    if len(numerodesocios) == 0:
        numerodesocio = 0
    else:
        numerodesocio = max(numerodesocios) + 1

    numerodesocios.append(numerodesocio)
    print("Socio agregado exitosamente. Su " "número de socio es:", numerodesocio)
    return socios, dnis, numerodesocios, estadosocios, tipodocs
def busqueda(numero, lista):
    """Busqueda secuencial para encontrar el índice de una lista"""
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
def buscar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs):
    """Busca un socio por su número de socio."""
    numeroodni=input("¿Usted desea buscar el socio por numero de socio o por dni/pasaporte? 1. Numero de socio 2. DNI o pasaporte: ")
    if numeroodni == "1":
        try:
            numero = int(input("Ingrese el número de socio a buscar: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return
        if numero in numerodesocios:
            x = busqueda(numero, numerodesocios)
            print("Socio encontrado:")
            print("Número de socio:", numerodesocios[x])
            print("Nombre:", socios[x])
            print(tipodocs[x] + ":", dnis[x])
            print("Estado:", estadosocios[x])

        else: 
            print("No se encontró ningún socio con ese número.")
            return
    elif numeroodni == "2":
        dni = input("Ingrese el DNI o pasaporte del socio a buscar: ")
        if dni in dnis:
            x = busqueda(dni, dnis)
            print("Socio encontrado:")
            print("Número de socio:", numerodesocios[x])
            print("Nombre:", socios[x])
            print(tipodocs[x] + ":", dnis[x])
            print("Estado:", estadosocios[x])
        else:
            print("No se encontró ningún socio con ese DNI o pasaporte.")
        return
    else:
        print("Opción inválida.")
        
def modificar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs):
    """Modifica los datos de un socio existente."""
    try:
        numero = int(input("Ingrese el número de socio: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
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
        if tipodocs[x] == "DNI":
            nuevo_dni = input("Ingrese el nuevo DNI: ")
            validar = validar_dni(nuevo_dni)
        else:
            nuevo_dni = validar_pasaporte()
            validar = True
        if validar==False:
            print("El documento ingresado no es válido. No se puede modificar el socio.")
            return
        if nuevo_dni in dnis and nuevo_dni != dnis[x]:
            print("El documento ya está registrado. No se puede modificar el socio.")
            return

        socios[x] = nuevo_nombre
        dnis[x] = nuevo_dni

        print("Socio modificado correctamente.")
    else:
        print("Numero de socio no encontrado.")
def estadodelsocio(socios, dnis, numerodesocios, estadosocios, tipodocs):
    """Modifica el estado de un socio a sancionado o inactivo."""
    try:
        numero = int(input("Ingrese el número de socio: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if numero not in numerodesocios:
        print("Número de socio no encontrado.")
        return
    x = busqueda(numero, numerodesocios)

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

def eliminar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs):
    """Elimina un socio del sistema."""
    try:
        numero = int(input("Ingrese el número de socio a eliminar: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if numero in numerodesocios:
        x = busqueda(numero, numerodesocios)
        socios.pop(x)
        dnis.pop(x)
        numerodesocios.pop(x)
        estadosocios.pop(x)
        tipodocs.pop(x)


        print("Socio eliminado correctamente.")
    else:
        print("No encontrado.")

def mostrar_socios(socios, dnis, numerodesocios, estadosocios, tipodocs):
    """Muestra la lista de socios registrados."""
    if socios:
        print("Lista de socios:")
        for i in range(len(socios)):
            print("..........................")
            print("Número de socio:", numerodesocios[i])
            print("Nombre:", socios[i])
            print(tipodocs[i] + ":", dnis[i])
            print("Estado:", estadosocios[i])
            
    else:
        print("No hay socios registrados.")
    print("..........................")

def menusocios(socios, dnis, numerodesocios, estadosocios, tipodocs):
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
            agregar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs)
        elif opcion == "2":
            buscar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs)
        elif opcion == "3":
            modificar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs)
        elif opcion == "4":
            eliminar_socio(socios, dnis, numerodesocios, estadosocios, tipodocs)
        elif opcion == "5":
            mostrar_socios(socios, dnis, numerodesocios, estadosocios, tipodocs)
        elif opcion == "6":
            estadodelsocio(socios, dnis, numerodesocios, estadosocios, tipodocs)
        elif opcion == "7":
            print("Saliendo del menú de socios.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
