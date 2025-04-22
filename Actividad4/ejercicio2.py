import datetime as dt
fechaIngreso  = input("Ingrese la fecha de ingreso (día/mes/año): ")
fechaIngreso = dt.datetime.strptime (fechaIngreso, "%d/%m/%Y")
fechaActual = dt.datetime.now ()

dias = (fechaActual - fechaIngreso).days

print (fechaActual)
print (fechaIngreso)
print ("dias ", dias)

if dias > 30:
    print ("Cuenta inactiva")