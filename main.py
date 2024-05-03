import pandas as pd
import matplotlib.pyplot as plt

productos = [
{"nombre": "Camiseta", "precio": 20, "cantidad_disponible": 100},
{"nombre": "Pantalón", "precio": 30, "cantidad_disponible": 80},
{"nombre": "Zapatos", "precio": 50, "cantidad_disponible": 50},
{"nombre": "Reloj", "precio": 100, "cantidad_disponible": 30},
{"nombre": "Gorra", "precio": 15, "cantidad_disponible": 120},
{"nombre": "Bufanda", "precio": 25, "cantidad_disponible": 60},
{"nombre": "Sudadera", "precio": 40, "cantidad_disponible": 70},
{"nombre": "Bolsa", "precio": 35, "cantidad_disponible": 90},
{"nombre": "Chaqueta", "precio": 80, "cantidad_disponible": 40},
{"nombre": "Gafas de sol", "precio": 45, "cantidad_disponible": 25},
{"nombre": "Calcetines", "precio": 10, "cantidad_disponible": 150},
{"nombre": "Sombrero", "precio": 20, "cantidad_disponible": 55},
{"nombre": "Pulsera", "precio": 5, "cantidad_disponible": 200},
{"nombre": "Pendientes", "precio": 15, "cantidad_disponible": 180},
{"nombre": "Cinturón", "precio": 20, "cantidad_disponible": 100},
{"nombre": "Vestido", "precio": 60, "cantidad_disponible": 35},
{"nombre": "Corbata", "precio": 25, "cantidad_disponible": 75},
{"nombre": "Bolso", "precio": 70, "cantidad_disponible": 45},
{"nombre": "Paraguas", "precio": 30, "cantidad_disponible": 65},
{"nombre": "Collar", "precio": 40, "cantidad_disponible": 85},
]

ventas = [
    {"nombre": "Camiseta", "cantidad": 24},
    {"nombre": "Pantalón", "cantidad": 16},
    {"nombre": "Zapatos", "cantidad": 33},
    {"nombre": "Reloj", "cantidad": 11},
    {"nombre": "Gorra", "cantidad": 87},
    {"nombre": "Bufanda", "cantidad": 2},
    {"nombre": "Sudadera", "cantidad": 28},
    {"nombre": "Bolsa", "cantidad": 58},
    {"nombre": "Chaqueta", "cantidad": 4},
    {"nombre": "Gafas de sol", "cantidad": 24},
    {"nombre": "Calcetines", "cantidad": 100},
    {"nombre": "Sombrero", "cantidad": 46},
    {"nombre": "Pulsera", "cantidad": 93},
    {"nombre": "Pendientes", "cantidad": 144},
    {"nombre": "Cinturón", "cantidad": 87},
    {"nombre": "Vestido", "cantidad": 24},
    {"nombre": "Corbata", "cantidad": 17},
    {"nombre": "Bolso", "cantidad": 5},
    {"nombre": "Paraguas", "cantidad": 15},
    {"nombre": "Collar", "cantidad": 49},
]

def valor_inventario(productos):

    # Crea un DataFrame con los datos del arreglo de productos
    tabla = pd.DataFrame(productos)

    # Realiza la multiplicación para calcular el inventario
    tabla['Inventario'] = tabla['precio'] * tabla['cantidad_disponible']

    # Suma todos los valores de la tabla inventario
    valor_total = tabla['Inventario'].sum()

    print(f"El valor total del inventario es de: ${valor_total}")

    # Crea la tabla del DataFrame
    df = tabla[['nombre','precio', 'cantidad_disponible', 'Inventario']]
    
    return df.to_string(index=False) # Retorna el DataFrame borrandole el índice

print(valor_inventario(productos))

print('---------------------------------------------------------')


def resultado_ventas(productos, ventas):
    # Crea un DataFrame con los datos del arreglo de productos
    tabla = pd.DataFrame(productos)
    # Crea un DataFrame con los datos del arreglo de ventas
    tabla_ventas = pd.DataFrame(ventas)

    # Resta la tabla de cantidad a la tabla de cantidad_disponible
    tabla['cantidad_restante'] = tabla['cantidad_disponible'] - tabla_ventas['cantidad']

    # Crea la tabla resultante
    dataframe = tabla[['nombre', 'cantidad_restante']]

    # Metodo basico para graficar X vs Y
    plt.plot(tabla['nombre'], tabla['cantidad_restante']) # se grafica una linea de color azul
    plt.xticks(tabla['nombre'],  rotation='vertical')

    # data = tabla['nombre'], tabla['cantidad_restante']
    # plt.hist(data, bins=10)

    plt.title('Cantidad disponible de productos')

    plt.grid(True) # Para visualizar en forma de grilla

    plt.show() # Mostrar la gráfica luego de que ya se definió todos los elementos

    return dataframe.to_string(index=False) # Retorna el DataFrame borrandole el índice

print(resultado_ventas(productos, ventas))