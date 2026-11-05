#Pruebas Unitarias Compras

# ==========================================
# PRUEBAS UNITARIAS - TIENDA DE PÁDEL
# ==========================================

def probar_producto_nuevo_logica():
    """Prueba unitaria para verificar la inserción de un nuevo producto en el diccionario."""
    productos = {101: ["Paleta básica", 50000, 10]}
    nuevo_codigo = 102
    nuevo_datos = ["Pelotas", 8000, 25]
    
    # Simulación de lógica de alta
    if nuevo_codigo not in productos:
        productos[nuevo_codigo] = nuevo_datos
        
    if 102 in productos and productos[102] == ["Pelotas", 8000, 25]:
        print("Prueba correcta: Producto agregado exitosamente.")
    else:
        print("Error en la prueba: El producto no se agregó correctamente.")


def probar_eliminar_producto_logica():
    """Prueba unitaria para verificar la eliminación de un producto existente mediante .pop()."""
    productos = {101: ["Paleta básica", 50000, 10], 102: ["Pelotas", 8000, 25]}
    codigo_a_eliminar = 101
    
    # Simulación de lógica de baja
    if codigo_a_eliminar in productos:
        productos.pop(codigo_a_eliminar)
        
    if 101 not in productos and len(productos) == 1:
        print("Prueba correcta: Producto eliminado exitosamente.")
    else:
        print("Error en la prueba: El producto no fue eliminado.")


def probar_modificar_producto_logica():
    """Prueba unitaria para verificar la actualización de los datos de un producto."""
    productos = {101: ["Paleta básica", 50000, 10]}
    codigo = 101
    
    # Simulación de modificación
    if codigo in productos:
        productos[codigo] = ["Paleta pro", 90000, 5]
        
    if productos[codigo] == ["Paleta pro", 90000, 5]:
        print("Prueba correcta: Producto modificado exitosamente.")
    else:
        print("Error en la prueba: El producto no se modificó correctamente.")


def probar_buscar_producto_logica():
    """Prueba unitaria para validar escenarios de búsqueda (positivos y negativos)."""
    productos = {101: ["Paleta básica", 50000, 10]}
    
    # Caso positivo: Código existente
    encontrado_valido = 101 in productos
    datos_encontrados = productos.get(101) if encontrado_valido else None
    
    # Caso negativo: Código inexistente
    encontrado_invalido = 999 in productos
    
    if encontrado_valido and not encontrado_invalido and datos_encontrados == ["Paleta básica", 50000, 10]:
        print("Prueba correcta: Búsqueda de productos validada (Casos positivos y negativos).")
    else:
        print("Error en la prueba: Fallo en la lógica de búsqueda.")


# Ejecución de la suite de pruebas automáticas
print("--- INICIANDO PRUEBAS UNITARIAS ---")
probar_producto_nuevo_logica()
probar_eliminar_producto_logica()
probar_modificar_producto_logica()
probar_buscar_producto_logica()
print("--- FIN DE LAS PRUEBAS ---")