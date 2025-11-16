import pytest
import constants
import sistema_inventario as si

@pytest.fixture
def test_data():
    """Fixture con datos de prueba comunes"""
    return {
        "Ratón Logitech MX Vertical": {
            "cantidad": 10,
            "precio": 99.99            
        }, 
        "Teclado Mecánico Keychron K2": {
            "cantidad": 5,
            "precio": 79.99
        },
        "Monitor Dell UltraSharp U2723QE": {
            "cantidad": 3,
            "precio": 499.99
        },
        "Teclado Mecánico Keychron K3": {      
            "cantidad": 7,
            "precio": 89.99
        }
    }


PRODUCTOS = [
    "Ratón Logitech MX Vertical",
    "Teclado Mecánico Keychron K2",
    "Monitor Dell UltraSharp U2723QE",
    "Teclado Mecánico Keychron K3"
]
def test_agregar_productos(mocker, test_data):
    mock_prompts = mocker.MagicMock()

    # Opción de agregar producto
    opcion_agregar = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_ADD
    ][0]

    # Opción de salir
    opcion_salir = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_QUIT
    ][0]

    # side_effect con dos llamadas: primero agregar, luego salir
    mock_prompts.pedir_opcion.side_effect = [opcion_agregar, opcion_salir]

    # Datos del producto a agregar
    producto = PRODUCTOS[0]
    mock_prompts.pedir_nombre_producto.return_value = producto
    mock_prompts.pedir_cantidad_producto.return_value = test_data[producto]["cantidad"]
    mock_prompts.pedir_precio_producto.return_value = test_data[producto]["precio"]

    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(si, "prompts", mock_prompts)
    mocker.patch.object(si, "mensajes", mock_mensajes)

    inventario = si.Inventario()
    inventario.menu_principal()

    # Validaciones
    assert any(p.nombre == producto for p in inventario.productos)

    # Buscar el producto en la lista
    p = next(p for p in inventario.productos if p.nombre == producto)

    # Comparar cantidad y precio
    assert p.cantidad == test_data[producto]["cantidad"]
    assert p.precio == test_data[producto]["precio"]

def test_buscar_producto(mocker, test_data):
    mock_prompts = mocker.MagicMock()

    # Opción de agregar producto
    opcion_agregar = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_ADD
    ][0]

    # Opción de buscar producto
    opcion_buscar = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_LIST
    ][0]

    # Opción de salir
    opcion_salir = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_QUIT
    ][0]

    # side_effect con llamadas: agregar, buscar, salir
    mock_prompts.pedir_opcion.side_effect = [opcion_agregar, opcion_buscar, opcion_salir]

    # Datos del producto a agregar
    producto = PRODUCTOS[1]
    mock_prompts.pedir_nombre_producto.return_value = producto
    mock_prompts.pedir_cantidad_producto.return_value = test_data[producto]["cantidad"]
    mock_prompts.pedir_precio_producto.return_value = test_data[producto]["precio"]

    # Nombre del producto a buscar
    mock_prompts.pedir_nombre_producto.side_effect = [producto]

    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(si, "prompts", mock_prompts)
    mocker.patch.object(si, "mensajes", mock_mensajes)

    inventario = si.Inventario()
    inventario.menu_principal()

    # Validaciones
    assert mock_mensajes.mensaje_detalle_producto.called

def test_calcular_valor_inventario(mocker, test_data):
    mock_prompts = mocker.MagicMock()

    # Opción de agregar producto
    opcion_agregar = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_ADD
    ][0]

    # Opción de calcular total
    opcion_total = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_TOTAL
    ][0]

    # Opción de salir
    opcion_salir = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_QUIT
    ][0]

    # side_effect con llamadas: agregar x2, total, salir
    mock_prompts.pedir_opcion.side_effect = [
        opcion_agregar,
        opcion_agregar,
        opcion_total,
        opcion_salir
    ]

    productos_a_agregar = PRODUCTOS[:2]
    side_effect_nombre = []
    side_effect_cantidad = []
    side_effect_precio = []

    for producto in productos_a_agregar:
        side_effect_nombre.append(producto)
        side_effect_cantidad.append(test_data[producto]["cantidad"])
        side_effect_precio.append(test_data[producto]["precio"])

    mock_prompts.pedir_nombre_producto.side_effect = side_effect_nombre
    mock_prompts.pedir_cantidad_producto.side_effect = side_effect_cantidad
    mock_prompts.pedir_precio_producto.side_effect = side_effect_precio

    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(si, "prompts", mock_prompts)
    mocker.patch.object(si, "mensajes", mock_mensajes)

    inventario = si.Inventario()
    inventario.menu_principal()

    # Cálculo esperado del valor total
    valor_esperado = sum(
        test_data[producto]["cantidad"] * test_data[producto]["precio"]
        for producto in productos_a_agregar
    )

    # Validaciones
    mock_mensajes.mensaje_valor_total_inventario.assert_called_with(valor_esperado)

def test_listar_productos(mocker, test_data):
    mock_prompts = mocker.MagicMock()

    # Opción de agregar producto
    opcion_agregar = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_ADD
    ][0]

    # Opción de listar productos
    opcion_listar = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_LIST
    ][0]

    # Opción de salir
    opcion_salir = [
        key for key, value in constants.OPCIONES_MENU.items()
        if value["accion"] == constants.OPCION_QUIT
    ][0]

    # side_effect con llamadas: agregar x2, listar, salir
    mock_prompts.pedir_opcion.side_effect = [
        opcion_agregar,
        opcion_agregar,
        opcion_listar,
        opcion_salir
    ]

    productos_a_agregar = PRODUCTOS[:2]
    side_effect_nombre = []
    side_effect_cantidad = []
    side_effect_precio = []

    for producto in productos_a_agregar:
        side_effect_nombre.append(producto)
        side_effect_cantidad.append(test_data[producto]["cantidad"])
        side_effect_precio.append(test_data[producto]["precio"])

    mock_prompts.pedir_nombre_producto.side_effect = side_effect_nombre
    mock_prompts.pedir_cantidad_producto.side_effect = side_effect_cantidad
    mock_prompts.pedir_precio_producto.side_effect = side_effect_precio

    mock_mensajes = mocker.MagicMock()
    mocker.patch.object(si, "prompts", mock_prompts)
    mocker.patch.object(si, "mensajes", mock_mensajes)

    inventario = si.Inventario()
    inventario.menu_principal()

    # Validaciones
    assert mock_mensajes.mensaje_detalle_producto.call_count == len(productos_a_agregar)