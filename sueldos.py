
print("Para finalizar el ingreso de sueldos digite 0")
C1 = 0
C2 = 0
C3 = 0
importe = 0
while True:
    
    sueldo = float(input("Por favor, digite el sueldo de su empleado: "))
    if sueldo >= 1300000 and sueldo < 3000000:
        C1 += 1
        importe = importe + sueldo
    elif sueldo > 3000000 and sueldo <= 10000000:
        C2 += 1
        importe = importe + sueldo
    elif sueldo == 0:
        break
    else:
        C3 += 1

print("El importe que la empresa gasta es: ", importe)

if C1 == 1:
    print(C1," empleado cobra entre $1.300.000 y $10.000.000")
else:
    print(C1," empleados cobran entre $1.3000.000 y $10.000.000")

if C2 == 1:
    print(C2," empleado cobra más de $3.000.000")
else:
    print(C2," empleados cobran más de $3.000.000")

if C3 == 1:
    print(C2," empleado cobra menos de $1.300.000")
else:
    print(C2," empleados cobran menos de $1.300.000")

