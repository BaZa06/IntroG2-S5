#Función
def es_triangulo(lado1, lado2, lado3):
    suma = lado1 + lado2
    if (suma > lado3):
        return "Es un triángulo"
    else: 
        return "No es un triángulo"
def main():
        lado1 = float(input("Ingrese el lado 1: "))
        lado2 = float(input("Ingrese el lado 2: "))
        lado3 = float(input("Ingrese el lado 3: "))
        resultado = es_triangulo(lado1, lado2, lado3)
        print(resultado)    
main()