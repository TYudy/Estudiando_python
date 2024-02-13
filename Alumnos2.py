'''Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.

al final nos debe mostrar la lista de los alumnos con el promedio de cada uno , si al ingresar un nombre que ya existe debe salir debe salir un mensaje de que ya existe'''

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
    