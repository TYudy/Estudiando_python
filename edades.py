sumam = 0
sumat = 0
suman = 0

print("TURNO MAÑANA")
for i in range (1,7):
    print("Estudiante" , i)
    mañana = int(input("Ingrese la edad: "))
    sumam = sumam + mañana
    promm = sumam / 6
print("TURNO TARDE")
for i1 in range (1,8):
    print("Estudiante" , i1)
    tarde = int(input("Ingrese la edad: "))
    sumat = sumat + tarde
    promt = sumat / 7

print("TURNO NOCHE")
for i2 in range (1,13):
    print("Estudiante" , i2)
    noche = int(input("Ingrese la edad: "))
    suman = suman + noche
    promn = suman / 12

print(" ")
print("--PROMEDIOS-- ")
print("MAÑANA : ",promm)
print("TARDE : ", promt)
print("NOCHE : ", promn)
if promm > promt and promm > promn:
    print("El promedio de las edades de la mañana es mayor")
elif promt > promm and promt > promn:
    print("El promedio de las edades de la tarde es mayor")
else:
    print("El promedio de las edades de la noche es mayor")