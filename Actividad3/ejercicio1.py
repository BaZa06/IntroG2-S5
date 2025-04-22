calificacion1 = int(input("Ingrese la calificación del primer examen: "))
calificacion2 = int(input("Ingrese la calificación del segundo examen: "))
calificacion3 = int(input("Ingrese la calificación del tercer examen: "))
suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3
print(f"""calificacion 1: {calificacion1:>3}
calificacion 2: {calificacion2:>3}
calificacion 3: {calificacion3:>3}
{"Promedio":<10}: {promedio:>3.0f}""")