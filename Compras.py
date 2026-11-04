def validar_numeros(mensaje):
    """Valida que el dato ingresado sea un número entero."""
    while True:
        try:
            dato = int(input(mensaje))
            if dato > 0:
                return dato
        except ValueError:
            print("Error: Debe ingresar un número entero positivo.")
            


def buscar_productos(productos):
    """muestra un producto buscado por codigo."""
    codigo= validar_numeros("Ingrese el codigo del producto a buscar: ")
    if codigo in productos:
        print("-"*60)
        print("Producto encontrado:")
        print(" ")
        print(f"{codigo:<10} {productos[codigo][0]:<20} {productos[codigo][1]:<10} {productos[codigo][2]:<10}")
        print(" ")
        print("-"*60)
    else:
        print("-"*60)
        print("Producto no encontrado.")
        print("-"*60)

def producto_nuevo(productos):
    """Crea un nuevo producto."""
    codigo= validar_numeros("Ingrese el código del producto: ")
    nombre= input("Ingrese el nombre del producto: ")
    precio= validar_numeros("Ingrese el precio del producto: ")
    cant= validar_numeros("Ingrese la cantidad del producto: ")
    print("Producto agregado exitosamente.")
    productos[codigo] = [nombre, precio, cant]
    return productos

def eliminar_producto(productos):
    codigo = int(input("Ingrese el código del producto a eliminar: "))
    if codigo in productos:
        productos.pop(codigo)
        print("-"*60)
        print(" ")
        print("Producto eliminado exitosamente.")
        print(" ")
        print("-"*60)
    else:
        print("-"*60)
        print(" ")
        print("Producto no encontrado.")
        print(" ")
        print("-"*60)
    return productos

def modificar_producto(productos):
    codigo = int(input("Ingrese el código del producto a modificar: "))
    if codigo in productos:
        nombre= input(" Ingrese el nombre del producto: ")
        precio= validar_numeros("Ingrese el precio del producto: ")
        cant= validar_numeros("Ingrese la cantidad del producto: ")
        productos[codigo] = [nombre, precio, cant]
        print("Producto modificado exitosamente.")
    else:
        print("Producto no encontrado.")
    return productos

def aseguraropcion():
    """Asegurar que el usuario ingrese una opción válida."""
    
    while True:
        try:
            opcion= int(input("Ingrese la opcion que decida realizar: "))
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                raise ValueError
        except ValueError:
            print("Opcion invalida. Por favor, ingrese una opcion valida.")

def mostrar_productos(productos):
    """Muestra todos los productos en la lista."""
    if len(productos) == 0:
        print("-"*60)
        print("No hay productos disponibles.")
        print("-"*60)

    else:
        print("-"*60)
        print("Productos disponibles:")
        print(" ")
        print(f"{'codigo':<10} {'nombre':<20} {'precio':<10} {'cantidad':<10}")
        
        for codigo, (nombre, precio, cantidad) in productos.items():
            print(f"{codigo:<10} {nombre:<20} {precio:<10} {cantidad:<10}")
        print(" ")
        print("-"*60)



def tienda():
    """Función principal del programa."""
    productos =  {}
    print("Bienvenido al sistema de compras")
    print("1. Buscar productos por código")
    print("2. Ingresar nuevo producto: ")
    print("3. Eliminar producto: ")
    print("4. Modificar producto:")
    print("5. Mostrar todos los productos: ")
    print("6. Salir del sistema: ")
    opcion= aseguraropcion()


    while opcion != 6:

        if opcion == 1:
            opcion= buscar_productos(productos)
        elif opcion == 2:
            productos= producto_nuevo(productos)
        elif opcion == 3:
            opcion= eliminar_producto(productos)
        elif opcion == 4:
            opcion= modificar_producto(productos)
        elif opcion == 5:
            opcion= mostrar_productos(productos)

        print("Bienvenido al sistema de compras")
        print("1. Buscar productos por código")
        print("2. Ingresar nuevo producto: ")
        print("3. Eliminar producto: ")
        print("4. Modificar producto:")
        print("5. Mostrar todos los productos: ")
        print("6. Salir del sistema: ")
        opcion= aseguraropcion()
    print("Gracias por utilizar el sistema de compras. ¡Hasta luego!")

tienda()
    

