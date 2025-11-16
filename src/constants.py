"""Constantes utilizadas en el sistema de inventarios
"""
OPCION_ADD = "ADD"
OPCION_FIND = "FIND"
OPCION_LIST = "LIST"
OPCION_TOTAL = "TOTAL"
OPCION_QUIT = "QUIT"

OPCIONES_MENU = {
    1: { "descripcion": "Agregar producto", "accion": OPCION_ADD},
    2: { "descripcion": "Buscar producto", "accion": OPCION_FIND},
    3: { "descripcion": "Listar productos", "accion": OPCION_LIST},
    4: { "descripcion": "Calcular valor total del inventario", "accion": OPCION_TOTAL},
    5: { "descripcion": "Salir", "accion": OPCION_QUIT }
}