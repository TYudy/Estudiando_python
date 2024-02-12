
nombres = []
notas=[]
listm=[]
listb = []
mb = 0
b=0
ins=0
for i in range (1,5):
    nom= input(f"Alumno {i} : ")
    nombres.append (nom)
    no = int(input("Nota: "))
    notas.append (no)
    
for y in range(len(nombres)):
    print(nombres[y])
    print(notas[y])
    if notas [y] >= 8:
        print("Muy bueno")
        mb += 1
        listm.append (nombres[y])
    else:
        if notas [y]>=4:
            print("Bueno")
            b +=1
            listb.append (nombres[y])
        else:
            print("Insuficiente, No aprobo")
            ins += 1
print("Lista incial",nombres)
'''print(nombres, notas)
print(" ")
print("Cantidad de alumnos muy buenos:" , mb)
print("Cantidad de alumnos buenos:" , b)
print("Cantidad de alumnos reprobados:" , ins)
print(" ")
print(f"Los mejores alumnos son: {listm}")
print(f"Los mejores alumnos son: {listb}")'''

eliminar = []
for z in range (len(notas)):
    if notas[z]>=4 and notas[z]<=7 :
        #notas.pop(z)
        #nombres.pop(z)
        eliminar.append(z)
for  d in sorted(eliminar, reverse = True):
    notas.pop(d)
    nombres.pop(d)
print ("Listado de alumnos entre" , nombres)