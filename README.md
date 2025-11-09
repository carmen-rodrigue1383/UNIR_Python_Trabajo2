# Título

## Descripción

Descripción

- [Enunciado](./enunciado.md) 
- [Solución](./solucion.md)

## Estructura
```
src/
├── main.py  # Módulo principal
├── ...
└── constantes.py            # Constantes 
```

## Uso
```cmd
python src/main.py
```

## Test
```cmd
pytest tests/
```
**Test con report de cobertura**
```cmd
pytest --cov=src --cov-report=html tests/
```