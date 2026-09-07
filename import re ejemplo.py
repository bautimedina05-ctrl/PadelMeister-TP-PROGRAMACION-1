import re

def validar_dni():
    dni = input("Ingrese su DNI: ")

    if re.match(r"^\d{8}$", dni):
        print("DNI valido")
    else:
        print("DNI invalido")

def extraer_numeros():
    texto= input("Ingrese un texto: ")
    numeros= re.findall(r"\d+", texto)
    print("Numeros encontrados:")

    i=0
    while i < len(numeros):
        print(numeros[i])
        i= i+1

#llamada a la funcion
