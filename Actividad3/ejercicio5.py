#Cálculo del consumo de agua por persona
litros_consumidos_mes_vivienda =  float(input("Ingrese la cantidad de litros consumidos al mes en una vivienda: "))
personas_casa = int(input("Ingrese la cantidad de personas que viven en la casa: "))
consumo_mesual_persona = litros_consumidos_mes_vivienda / personas_casa
consumo_diario_persona = consumo_mesual_persona / 30
print(f"""El consumo total mensual es de: {litros_consumidos_mes_vivienda:>3}
El número de personas que viven en la casa es de: {personas_casa:>3}
{"El consumo mensual por persona es de: ":<10}: {consumo_mesual_persona:>3.2f} litros
{"El consumo diario por persona es de: ":<10}: {consumo_diario_persona:>3.2f} litros""")