# Primer Parcial de TLP 3 - Python para Ciencia de datos

En este repositorio se desarrollo el primer parcial del espacio curricular TLP 3 - Python para Ciencia de datos, el mismo cuenta con dos archivos `app.py` y `main.py`, más adelante se explica la funcionalidad de cada archivo, pero primero hay tener las herramientas necesarias para la ejecución del proyecto.

## Requisitos 
- Python 3.x: Si no lo tienes instalado, puedes descargarlo desde [python.org](https://www.python.org/downloads/).
- pip: El gestor de paquetes de Python. Generalmente se instala automáticamente con Python 3.

## Configuración del Entorno Virtual

Se recomienda usar entornos virtuales para evitar conflictos entre las dependencias de diferentes proyectos. Sigue estos pasos para crear y activar un entorno virtual:

```bash
# Instalar la herramienta virtualenv si no está instalada
pip install virtualenv

# Crear un nuevo entorno virtual
virtualenv venv

# Activar el entorno virtual (Windows)
venv\Scripts\activate
# o (Linux/macOS)
source venv/bin/activate
```

## Instalación de Dependencias
Para instalar las librerías necesarias, ejecuta el siguiente comando después de activar tu entorno virtual:

```bash
pip install pandas
```

```bash
pip install matplotlib
```

## Archivos y Uso

### app.py

Este archivo contiene una función `capitalizar_palabra(palabra)` que recibe una cadena de texto y su función convertir la primera letra a mayúscula y que las demás se mantengan en minúsculas. Para ejecutarlo, simplemente llama a la función con la cadena de texto que desees como argumento. Ejemplo:

```bash
from app import capitalizar_palabra
print(capitalizar_palabra('python')) # Salida: Python
```

### main.py

El siguiente archivo tiene un arreglo de productos y sobre el mismo se calcula de cuanto es el inventario multiplicando el precio del producto y la cantidad disponible del mismo, eso se imprime en un dataframe con los atributos nombre, precio, cantidad_disponible e inventario. También, tiene otro arreglo de ventas y que simula unas ventas por cada producto disponible, lo que hace es restar a la cantidades disponibles del principio, luego imprime un dataframe con el nombre del producto y las cantidades restantes.

Para ejecutarlo, simplemente corre el script:

```bash
python main.py
```

Y por último se genera un gráfico donde el eje x representa los nombres de los productos y el eje y representa la cantidad disponible de cada producto.