calificación = float(input("¿Cuál es tu calificación de 0 a 10? "))
if calificación >= 9 and calificación <= 10:
    print('Su calificación es tipo A')
elif calificación >= 7 and calificación < 8:
    print('Su calificación es tipo B')
elif calificación >= 5 and calificación < 6:
    print('Su calificación es tipo C')
elif calificación >= 3 and calificación < 4:
    print('Su calificación es tipo D')
elif calificación >= 0 and calificación < 2:
        print('Su calificación es tipo F')
else:
    print('Calificación no válida')
        