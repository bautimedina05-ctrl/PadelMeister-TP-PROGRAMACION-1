def busca_productos(productos):
    """Busca productos por código."""
    posicion= -1
    codigo= int(input("Ingrese el código del producto: "))
    for i in range(len(productos)):
        if codigo == productos[i]:
            posicion= i
    return posicion



#MAIN
productos=[23]
precios=[4]
cantidad=[32]
print("Bienvenido al sistema de compras")
print("1. Buscar productos por código")
print("2. Ingresar nuevo producto: ")
print("3. Eliminar producto: ")
print("4. Salir del sistema: ")
opcion= int(input("Ingrese la opcion que decida realizar: "))
if opcion == 1:
    codigo= busca_productos(productos)
    if codigo != -1:
        print("Codigo", "Precio", "Cantidad")
        print(productos[codigo],"    ", precios[codigo],"     ",cantidad[codigo])
    else:
        print("Codigo no encontrado")


    