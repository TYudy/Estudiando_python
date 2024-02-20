alumnos = {}
promedios = {}



canta = int(input("Por favor ingrese la cantidad de alumnos: "))
for c in range (canta):
    nombre = input("Por favor ingrese el nombre del alumno: ")
    nota = 0
    notas = []
    suma = 0
    contn=0
    if nombre in alumnos:
        "Ese nombre ya existe dentro del sistema"
    else:
        while True:
            nota = int(input("NOTA: "))
            if nota >= 0:
                contn  += 1
                suma = suma + nota
                prom = suma / contn
                notas.append (nota)
            else:
                break
    promedios [nombre] = prom
    alumnos [nombre] = notas

print (" ")
print ("")
for nombre in alumnos:
    print(nombre)
    for nota in alumnos[nombre]:
        print(nota)
    for x in promedios:
        print("Promedio: ", prom)