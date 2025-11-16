class NombreNoValido(Exception):
    """Excepción personalizada para nombre de producto no válido (no puede estar vacío)"""
    pass

class CantidadNoValida(Exception):
    """Excepción personalizada para cantidad de producto no válida (debe ser numérico entero mayor que 0)"""
    pass

class PrecioNoValido(Exception):
    """Excepción personalizada para precio de producto no válido (debe ser numérico mayor que 0)"""
    pass

class OpcionNoValida(Exception):
    """Excepción personalizada para opción de menú no válida"""
    pass

