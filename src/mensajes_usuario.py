"""
Funciones para mostrar mensajes al usuario, opcionalmente algunos mensajes reciben parámetros para personalizar el mensaje.
"""
mensaje_bienvenida = lambda: print("""
=========================================
        📦 Sistema de Inventario
=========================================
""")
mensaje_opciones_disponibles = lambda opciones: print("¿Qué deseas hacer? Las opciones disponibles son: \n", *opciones, sep="\n", end="\n\n")
mensaje_opcion_no_valida = lambda opcion: print(f"Opción {opcion} no válida. Por favor, intentalo de nuevo.")
mensaje_bienvenida_agregar_producto = lambda: print("""
--- Agregar Producto ---

Vamos a agregar un nuevo producto.
Por favor, proporciona los siguientes detalles:
""")
mensaje_nombre_producto_invalido = lambda: print("⚠️  El nombre del producto no puede estar vacío. Por favor, ingresa un nombre válido.")
mensaje_cantidad_producto_invalida = lambda cantidad: print(f"⚠️  La cantidad '{cantidad}' no es válida. Debe ser un número entero igual o mayor que 0.")
mensaje_precio_producto_invalido = lambda precio: print(f"⚠️  El precio '{precio}' no es válido. Debe ser un número igual o mayor que 0.")
mensaje_producto_agregado = lambda nombre: print(f"✅  Producto '{nombre}' agregado al inventario.")
mensaje_bienvenida_buscar_producto = lambda: print("""
--- Buscar Producto ---

Vamos a buscar un producto en el inventario.
""")
mensaje_producto_no_encontrado = lambda nombre: print(f"⚠️  El producto '{nombre}' no se encontró en el inventario.")
mensaje_bienvenida_listar_productos = lambda: print("""
--- Listar Productos ---

Aquí están todos los productos en el inventario:
""")
mensaje_sin_productos = lambda: print("El inventario está vacío. No hay productos para mostrar.")
mensaje_detalle_producto = lambda producto: print(f"{producto}")
mensaje_bienvenida_total_inventario = lambda: print("""
--- Valor Total del Inventario ---

El valor total de todos los productos en el inventario es:
""")
mensaje_valor_total_inventario = lambda total: print(f"€ {total:.2f}\n")
mensaje_despedida = lambda: print("""
Gracias por usar el sistema de inventario. ¡Hasta pronto! 👋
""")
mensaje_error_inesperado = lambda: print("⚠️  Ha ocurrido un error inesperado. Saliendo del programa. ")