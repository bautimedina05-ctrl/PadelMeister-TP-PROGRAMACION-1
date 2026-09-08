import re
texto= "El numero de telefono de Oliver es 123-456-7890, y el de Gabriela es 987-654-3210."
patron= "[0-9]{3}-[0-9]{3}-[0-9]{4}"
cadenaenmascarada= "XXX-XXX-XXXX"

textoOfuscado= re.sub(patron, cadenaenmascarada, texto)
print("Texto original:")
print(texto)
print("\nTexto despues de ofuscar los numeros de telefono: ")
print(textoOfuscado)
