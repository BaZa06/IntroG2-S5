sueldo = float(input("¿Cuál es su sueldo? "))
bono = 0
if sueldo > 3000:
    bono = sueldo * 0.10
    print(f"Su bono es de: , {bono:.2f}")
elif sueldo > 1500 and sueldo <= 3000:
    bono = sueldo * 0.05
    print (f"Su bono es de: , {bono:.2f}")
elif sueldo <= 1500:
    print("No tiene bono")