#Cálculo consumo de combustible
distancia_recorridaKM = float(input("Ingrese la distancia recorrida en KM: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
rendimiento = distancia_recorridaKM / litros_consumidos
precio_combustible = 48.97
gasto_total_combustible = litros_consumidos * precio_combustible
print(f"""Distancia recorrida fue de: {distancia_recorridaKM:>3}
Los litros consumidos fueron de: {litros_consumidos:>3}
{"El rendimiento fue de: ":>0}: {rendimiento:.2f} km/litro
{"El precio definido del combustible es de: ":<10}: {precio_combustible:>3.2f}
{"Gasto total de combustible fue de: ":<10}: {gasto_total_combustible:>3.2f}""")