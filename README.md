# NumberSorter

Un programa educativo en Python que ordena una lista de números enteros **usando el método de inserción** (insertion sort simplificado).

Recibe una lista de números desordenados, los inserta uno por uno en una nueva lista manteniendo el orden ascendente, y muestra el resultado.

Ideal para practicar:
- Bucles `for` y `while`
- Uso de `list.insert()`
- Comparaciones y lógica de ordenamiento manual
- Manejo básico de entrada/salida

## Características

- Ordena números insertándolos en la posición correcta (sin usar `sorted()` ni `sort()`)
- Muestra tanto el resultado propio como la versión de Python (`sorted`) para comparación
- Maneja entrada por consola (números separados por coma)
- Valida entrada básica (solo enteros)
- Opción para salir del programa

## Requisitos

- Python 3.x  
- No requiere librerías externas

## Instalación

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/NumberSorter.git
2. Entra al directorio: cd NumberSorter

## Uso

Ejecuta el programa: python NumberSorter.py
Ejemplo de interacción:
=== NumberSorter - Ordenador por inserción ===

Ingresa números separados por coma (o 'salir'): 7, 3, 9, -2, 5, 1

Números ingresados (desordenados):
[7, 3, 9, -2, 5, 1]

Lista ordenada (por inserción):
[-2, 1, 3, 5, 7, 9]

(Para comparación - sorted de Python):
[-2, 1, 3, 5, 7, 9]

Ingresa números separados por coma (o 'salir'): salir
¡Hasta luego!

## Ejemplos adicionales

Entrada negativa y repetidos:
Ingresa números separados por coma (o 'salir'): 4, -1, 4, 0, -5, 2
Salida esperada:
Lista ordenada (por inserción): [-5, -1, 0, 2, 4, 4]
Lista vacía o solo Enter:
Ingresa números separados por coma (o 'salir'): 
→ Mensaje: "Entrada vacía. Intenta de nuevo."
Entrada inválida:
Ingresa números separados por coma (o 'salir'): 1,2,a,4
→ Mensaje: "Error: Ingresa solo números enteros separados por comas."

## ¿Por qué este método?

- Ayuda a entender cómo funciona el ordenamiento por inserción
- Muestra la diferencia entre algoritmos manuales y funciones nativas (sorted)
- Es excelente para entrevistas o exámenes donde piden implementar ordenamiento sin librerías

## Ideas para extender el proyecto

- Permitir orden descendente
- Medir tiempo de ejecución y compararlo con sorted()
- Generar listas aleatorias grandes para comparar rendimiento
- Agregar opción de leer números desde un archivo
- Interfaz gráfica simple con tkinter

## Autor
Camilo Baeza
