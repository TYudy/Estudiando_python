print("MENU")
numeros = []


while True :
    print(" ")
    menu = int (input("Acción a realizar: "))
    print(" ")
    if menu == 1 :
        
        nu= int (input("--1-- Numero a añadir: "))
        numeros.append(nu)
        print(numeros)


    elif menu == 2:
        nu= int (input("--2-- Numero a añadir: "))
        po = int(input("--2-- Posicion: "))
        numeros.insert(po,nu)
        print("")


    elif menu == 3:
        print(f"--3-- Hay {len(numeros)} entradas en la lista")


    elif menu == 4:
        print(f"--4-- Ultimo numero : {numeros[-1]}")
        numeros.pop()
        print(f"El numero ha sido eliminado{numeros}")


    elif menu == 5:
        print(numeros)
        po = int(input("--5-- Posicion a eliminar desde el indice 1: "))
        if po >= 1 or po <= len(numeros) :
            temp = numeros[po]
            del numeros[po]
            print(f"El numero {temp} ha sido eliminado")
            print("La lista ha sido actualizada",numeros)
        elif po > len(numeros):
            print("La posicion dada no existe")
        else:
            print("El indice debe iniciar al menos en 1")

        print(" ")


    elif menu == 6:
        con = 0
        nu = int(input("--6-- Numero a contar: "))
        for c in numeros:
            if c == nu:
                con += 1
        print(con)
        print(" ")


    elif menu == 7:
        con = 0
        nu = int(input("--7-- Numero a contar: "))
        for c in numeros:
            con += 1
            if c == nu:
                print(f"Posicion {con}")
        print(" ")


    elif menu == 8:
        print("LISTA")
        for i in numeros:
            print({i}) 
        print(" ")
    elif menu == 9:
        print("Gracias")
        break
    else:
        print("La opción seleccionada no existe")