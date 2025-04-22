#control de inventario de un producto
inventario_inicial = int(input("Ingrese el inventario inicial: "))
productos_recividos = int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))
suma = inventario_inicial + productos_recividos
inventario_actual = suma - productos_vendidos
print(f"""Inventario inicial era de: {inventario_inicial:>3}
Los productos recibidos fueron de: {productos_recividos:>3}
Los productos vendidos fueron de: {productos_vendidos:>3}
{"Inventario actual disponible de: ":<10}: {inventario_actual:>3}""")