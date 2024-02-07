#for x in range (1,21,2):
 #   print(x)

n = int(input("Ingrese # de empleados: "))
c = 0
c1 =0
Gasto = 0
for ini in range(n):
    sueldo = float(input("Ingresar el sueldo del empleado "))
    Gasto = Gasto + sueldo

    if sueldo >= 1300000 and sueldo <= 3000000:
        c +=1
    elif sueldo > 3000000:
        c1 +=1

print("Los gastos de la empresa total", Gasto )
print("Empleados que ganan más de 1.300.000 y 3.000.000 son: ", c)
print("Empleados que ganan más de 3.000.000 son: ", c1)