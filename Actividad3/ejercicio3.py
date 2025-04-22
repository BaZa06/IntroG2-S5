#Cáculo de interes comupesto
capital_inicial = float(input("Ingrese el capital inicial: "))
interes_anual = int(input("Ingrese la tasa de interez anual en porcentaje: "))
años = int(input("Ingrese el número de años: "))
decimal = interes_anual / 100
valor = (1 + decimal) **años
monto_final = capital_inicial * valor
interes_ganado = monto_final - capital_inicial
print(f"""Capital inicial fue de: {capital_inicial:>3}
Interes anual fue de: {interes_anual:>3}
Años fue de: {años:>3}
{"Monto final de: ":<10}: {monto_final:>3.2f}
{"Interes ganado de: ":<10}: {interes_ganado:>3.2f}""")
