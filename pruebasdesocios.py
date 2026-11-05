from socios import validar_dni, validar_sin_coma, busqueda, tipos_documento
 
 

def prueba_dni_valido():
    resultado = validar_dni("12345678")
 
    if resultado == True:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_dni_vacio():
    resultado = validar_dni("")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_dni_corto():
    resultado = validar_dni("1234567")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_dni_largo():
    resultado = validar_dni("123456789")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_dni_con_letras():
    resultado = validar_dni("1234567A")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_dni_con_espacio():
    resultado = validar_dni("1234 678")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 

def prueba_nombre_valido():
    resultado = validar_sin_coma("Juan Perez")
 
    if resultado == True:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_nombre_con_coma():
    resultado = validar_sin_coma("Perez, Juan")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_nombre_vacio():
    resultado = validar_sin_coma("")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_nombre_solo_espacios():
    resultado = validar_sin_coma("     ")
 
    if resultado == False:
        print("Prueba correcta")
    else:
        print("Error en la prueba")

def prueba_busqueda_encontrado():
    lista = [0, 1, 2, 3]
    resultado = busqueda(2, lista)
 
    if resultado == 2:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_busqueda_primer_elemento():
    lista = [10, 20, 30]
    resultado = busqueda(10, lista)
 
    if resultado == 0:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_busqueda_con_texto():
    lista = ["12345678", "87654321"]
    resultado = busqueda("87654321", lista)
 
    if resultado == 1:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_busqueda_no_encontrado():
    lista = [0, 1, 2, 3]
    resultado = busqueda(99, lista)
 
    if resultado == None:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
 
def prueba_busqueda_lista_vacia():
    lista = []
    resultado = busqueda(1, lista)
 
    if resultado == None:
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
def prueba_tipos_documento():
    if tipos_documento == ("DNI", "Pasaporte"):
        print("Prueba correcta")
    else:
        print("Error en la prueba")
 
print("Pruebas de validación de DNI:")
prueba_dni_valido()
print("Pruebas de validación de dni vacio")
prueba_dni_vacio()
print("Pruebas de validación de dni corto")
prueba_dni_corto()
print("Pruebas de validación de dni largo")
prueba_dni_largo()
print("Pruebas de validación de dni con letras")
prueba_dni_con_letras()
print("Pruebas de validación de dni con espacio")
prueba_dni_con_espacio()

print("Pruebas de validación de nombre:")
prueba_nombre_valido()
print("Pruebas de validación de nombre con coma")
prueba_nombre_con_coma()
print("Pruebas de validación de nombre vacio")
prueba_nombre_vacio()
print("Pruebas de validación de nombre solo espacios")
prueba_nombre_solo_espacios()
print("Pruebas de busqueda en lista:")
prueba_busqueda_encontrado()
print("Pruebas de busqueda primer elemento en lista:")
prueba_busqueda_primer_elemento()
print("Pruebas de busqueda con texto en lista:")
prueba_busqueda_con_texto()
print("Pruebas de busqueda no encontrado en lista:")
prueba_busqueda_no_encontrado()
print("Pruebas de busqueda en lista vacia:")
prueba_busqueda_lista_vacia()
print("Pruebas de tipos de documento:")
prueba_tipos_documento()
 