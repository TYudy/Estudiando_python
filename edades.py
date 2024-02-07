sumam = 0
sumat = 0
suman = 0
 
print("TURNO MAÑANA")
for i in range (1,7):
    mañana = int(input(f"Ingrese la edad del estudiante {i}"))
    sumam = sumam + mañana
    promm = sumam / 6
print("TURNO TARDE")
for i in range (1,8):
    tarde = int(input(f"Ingrese la edad del estudiante {i}"))
    sumat = sumat + tarde
    promt = sumat / 7

print("TURNO NOCHE")
for i in range (1,13):
    noche = int(input(f"Ingrese la edad del estudiante {i}"))
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