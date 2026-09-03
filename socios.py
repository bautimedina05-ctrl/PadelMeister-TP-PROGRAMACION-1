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
    numerorepetido = True

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
    numerodesocio=len(socios)-1
    while numerorepetido==True:
        if numerodesocio in numerodesocios:
            numerodesocio+=1
        else:
            numerorepetido=False
    numerodesocios.append(numerodesocio)
    print("Socio agregado exitosamente. Su " "número de socio es:", numerodesocio)
    return socios, dnis, numerodesocios, estadosocios

def buscar_socio(socios, dnis, numerodesocios, estadosocios):
    """Busca un socio por su número de socio."""
    numeroodni=int(input("¿Usted desea buscar el socio por numero de socio o por dni? 1. Numero de socio 2. DNI: "))
    if numeroodni == 1:
        numero=int(input("Ingrese el número de socio a buscar: "))
        if numero in numerodesocios:
            print("Socio encontrado:")
            print("Nombre:", socios[numero])
            print("DNI:", dnis[numero])
            print("Estado:", estadosocios[numero])
            return
        else: 
            print("No se encontró ningún socio con ese número.")
            return
    elif numeroodni == 2:
        dni=input("Ingrese el DNI del socio a buscar: ")
        for i in range(len(dnis)):
            if dnis[i] == dni:
                print("Socio encontrado:")
                print("Número de socio:", numerodesocios[i])
                print("Nombre:", socios[i])
                print("Estado:", estadosocios[i])
                return
        
def modificar_socio(socios, dnis, numerodesocios, estadosocios):
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
def estadodelsocio(socios, dnis, numerodesocios, estadosocios):
    """Modifica el estado de un socio a sancionado o inactivo."""
    numero = int(input("Ingrese el número de socio: "))
    if numero in numerodesocios:
        print("Ingrese el nuevo estado del socio", socios[numero] , ": ")
        print("1. Activo")
        print("2. Inactivo")
        print("3. Sancionado")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            estadosocios[numero] = "activo"
        elif opcion == "2":
            estadosocios[numero] = "inactivo"
        elif opcion == "3":
            estadosocios[numero] = "sancionado"
        else:
            print("Opción inválida. No se modificó el estado del socio.")
            return
        

        print("Estado del socio modificado correctamente.")
        return estadosocios 
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
1
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
            modificar_socio(socios, dnis, numerodesocios)
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