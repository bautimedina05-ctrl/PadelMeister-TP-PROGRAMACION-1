import re
cadena= "El precio del producto es $11.33. "
patron= "[0-9]+"
match= re.search(patron, cadena)
if match:
    numeroencontrado= match.group()
    posicioninicio= match.start()
    posicionfin= match.end()
    posicionspan= match.span()
    print(f"Número encontrado: {numeroencontrado}")
    print(f"Posición de inicio: {posicioninicio}")
    print(f"Posición de fin: {posicionfin}")
    print(f"Posicion donde comienza y termina (tupla span): {posicionspan}")
else:
    print("No se encontró ningún número en la cadena.")
    