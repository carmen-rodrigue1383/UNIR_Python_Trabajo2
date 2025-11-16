"""
Funciones para realizar preguntas al usuario, algunas de las cuales requieren parámetros para personalizar la pregunta.
"""
pedir_opcion = lambda: input("Selecciona una opción: ")
pedir_nombre_producto = lambda: input("Nombre del producto: ")
pedir_cantidad_producto = lambda: input("Cantidad del producto (mayor que 0, sin decimales): ")
pedir_precio_producto = lambda: input("Precio del producto en € (mayor que 0): ")
pedir_nombre_producto_buscar = lambda: input("Introduce el nombre del producto que deseas buscar: ")