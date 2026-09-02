def buscar_productos(productos):
    """Busca productos por código."""
    codigo = int(input("Ingrese el código del producto a buscar: "))
    if codigo != -1:
            for i in range(len(productos)):
                if productos[i][0] == codigo:
                    print("codigo","   ""nombre","   ","precio","   ","cantidad")
                    print(f"{productos[i]}")
    else:
        print("Codigo no encontrado")

def producto_nuevo():
    """Crea un nuevo producto."""
    codigo= int(input("Ingrese el código del producto: "))
    nombre= input("Ingrese el nombre del producto: ")
    precio= int(input("Ingrese el precio del producto: "))
    cant= int(input("Ingrese la cantidad del producto: "))
    print("Producto agregado exitosamente.")
    return [codigo, nombre, precio, cant]

def agregar_producto(productos):
    """Agrega un nuevo producto a la lista de productos."""
    productos.append(producto_nuevo())
    return productos

def eliminar_producto(productos):
    codigo = int(input("Ingrese el código del producto a eliminar: "))
    for i in range(len(productos)):
        if productos[i][0] == codigo:
            del productos[i]
            print("Producto eliminado exitosamente.")
        else:
            print("Producto no encontrado.")
    return productos

def modificar_producto(productos):
    codigo = int(input("Ingrese el código del producto a modificar: "))
    for i in range(len(productos)):
        if productos[i][0] == codigo:
            precio= int(input("Ingrese el nuevo precio del producto: "))
            cant= int(input("Ingrese la nueva cantidad del producto: "))
            productos[i][2] = precio
            productos[i][3] = cant
            print("Producto modificado exitosamente.")
        else:
            print("Producto no encontrado.")
    return productos

def aseguraropcion():
    """Asegurar que el usuario ingrese una opción válida."""
    opcion= int(input("Ingrese la opcion que decida realizar: "))
    while opcion < 1 or opcion > 5:
        print("Opción no válida. Por favor, ingrese una opción válida.")
        opcion = int(input("Ingrese la opcion que decida realizar: "))
    return opcion

def tienda():
    """Función principal del programa."""
    productos =  []
    print("Bienvenido al sistema de compras")
    print("1. Buscar productos por código")
    print("2. Ingresar nuevo producto: ")
    print("3. Eliminar producto: ")
    print("4. Modificar producto:")
    print("5. Salir del sistema: ")
    opcion= aseguraropcion()

    while opcion != 5:

        if opcion == 1:
            opcion= buscar_productos(productos)
        elif opcion == 2:
            opcion= agregar_producto(productos)
        elif opcion == 3:
            opcion= eliminar_producto(productos)
        elif opcion == 4:
            opcion= modificar_producto(productos)

        print("Bienvenido al sistema de compras")
        print("1. Buscar productos por código")
        print("2. Ingresar nuevo producto: ")
        print("3. Eliminar producto: ")
        print("4. Modificar producto:")
        print("5. Salir del sistema: ")
        opcion= aseguraropcion()
        return opcion
    print("Gracias por utilizar el sistema de compras. ¡Hasta luego!")
    

tienda()
