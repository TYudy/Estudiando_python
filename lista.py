tupla = (2,4,6)
fecha = (9, "Febrero", 2024)

print(tupla)
print(fecha)
cp = int (input("Ingrese la cantidad de palabras que desea agregar"))

if cp < 1:
    print ("No es valido")
else:
    lista = []
    for i in range (cp):
        p = input (f"Escriba la palabra {i+1}: ")
        lista += {p}

    print (f"Las palabras agregadas fueron: {lista}")