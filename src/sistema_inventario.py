import mensajes_usuario as mensajes
import prompts
import constants
from exceptions import NombreNoValido, CantidadNoValida, PrecioNoValido, OpcionNoValida

class Producto:
    nombre: str
    cantidad: int
    precio: float

    def __init__(self, nombre: str, cantidad: int, precio: float):
        if nombre.strip() == "":
            raise ValueError("El nombre del producto no puede estar vacío")

        if cantidad < 0:
            raise CantidadNoValida("La cantidad no puede ser negativa")

        if precio < 0:
            raise PrecioNoValido("El precio no puede ser negativo")

        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio    

    def calcular_valor_total(self):
        return self.cantidad * self.precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        if(nueva_cantidad < 0):
            raise CantidadNoValida("La cantidad no puede ser negativa")
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio: float):
        if(nuevo_precio < 0):
            raise PrecioNoValido("El precio no puede ser negativo")
        try:
            precio = float(nuevo_precio)
        except ValueError:
            raise PrecioNoValido("El precio debe ser un número válido")
        self.precio = precio

    def __str__(self):
        return f"{self.cantidad} {'unidades' if self.cantidad > 1 or self.cantidad == 0 else 'unidad'} de {self.nombre}, con un precio de {self.precio:.2f}, y un valor total de {self.calcular_valor_total():.2f} €"

class Inventario:
    productos: list

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        mensajes.mensaje_producto_agregado(producto.nombre)

    def buscar_producto(self, nombre: str):
        for producto in self.productos:
            if producto.nombre.casefold() == nombre.casefold():
                return producto                
        return None 

    def listar_productos(self):
        if(len(self.productos) == 0):
            mensajes.mensaje_sin_productos()
            return
        for producto in self.productos:
            mensajes.mensaje_detalle_producto(producto)
            
    def calcular_valor_total(self):
        total = 0.0
        for producto in self.productos:
            total += producto.calcular_valor_total()
        return total

    def menu_principal(self):
        mensajes.mensaje_bienvenida()

        while True:
            opciones = [f"{key}. {value.get('descripcion')}" for key, value in constants.OPCIONES_MENU.items()]
            mensajes.mensaje_opciones_disponibles(opciones)        
            
            seleccion_valida = False

            opcion_seleccionada = prompts.pedir_opcion()
            while not seleccion_valida:                
                try:
                    numero = int(opcion_seleccionada)                
                    if(numero not in constants.OPCIONES_MENU.keys()):
                        raise OpcionNoValida
                    seleccion_valida = True
                except (ValueError, OpcionNoValida) as e:
                    mensajes.mensaje_opcion_no_valida(opcion_seleccionada)            
                    opcion_seleccionada = prompts.pedir_opcion()
                
            accion = constants.OPCIONES_MENU[int(opcion_seleccionada)]['accion']        

            if accion == constants.OPCION_ADD:                                
                mensajes.mensaje_bienvenida_agregar_producto()        

                nombre_valido = False
                while not nombre_valido:
                    nombre = prompts.pedir_nombre_producto()                    
                    try:
                        if(nombre.strip() == ""):
                            raise NombreNoValido                    
                        nombre_valido = True
                    except NombreNoValido:
                        mensajes.mensaje_nombre_producto_invalido()

                precio_valido = False
                while not precio_valido:
                    precio_entrada = prompts.pedir_precio_producto()
                    try:
                        precio = float(precio_entrada)
                        if(precio < 0):
                            raise PrecioNoValido
                        precio_valido = True
                    except (ValueError, PrecioNoValido) as e:
                        mensajes.mensaje_precio_producto_invalido(precio_entrada)
                
                cantidad_valida = False
                while not cantidad_valida:
                    cantidad_entrada = prompts.pedir_cantidad_producto()
                    try:
                        cantidad = int(cantidad_entrada)
                        if(cantidad < 0):
                            raise CantidadNoValida
                        cantidad_valida = True
                    except (ValueError, CantidadNoValida) as e:
                        mensajes.mensaje_cantidad_producto_invalida(cantidad_entrada)

                nuevo_producto = Producto(nombre, cantidad, precio)
                self.agregar_producto(nuevo_producto)
            elif accion == constants.OPCION_FIND:
                mensajes.mensaje_bienvenida_buscar_producto()
                nombre_busqueda = prompts.pedir_nombre_producto_buscar()                                                                
                producto = self.buscar_producto(nombre_busqueda)
                if(not producto):                                                
                    mensajes.mensaje_producto_no_encontrado(nombre_busqueda)    
                else:
                    mensajes.mensaje_detalle_producto(producto)                                    
            elif accion == constants.OPCION_LIST:
                mensajes.mensaje_bienvenida_listar_productos()
                self.listar_productos()                
            elif accion == constants.OPCION_TOTAL:
                mensajes.mensaje_bienvenida_total_inventario()
                total_inventario = self. calcular_valor_total()
                mensajes.mensaje_valor_total_inventario(total_inventario)
            elif accion == constants.OPCION_QUIT:
                mensajes.mensaje_despedida()
                break
            else:
                mensajes.mensaje_opcion_no_valida(opcion_seleccionada)                               
              
if __name__ == "__main__":
    try
        inventario = Inventario()    
        inventario.menu_principal();    
    except
        printf("Ha ocurrido un error inesperado. Saliendo del programa. ")