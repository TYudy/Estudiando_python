



def rango():

    a1 = int(input("Por favor ingrese el primer año"))
    a2 = int(input("Por favor ingrese el segundo año"))
    contador(a1,a2)

def contador(an1,an2):
    b = 0
    b1 = 0
    for i in range (an1,an2+1):
      
        if i % 4  == 0 and i % 100 != 0:
            b += 1
            print(f"{i} es bisiesto")

        else:
            b1 += 1
            print(f"{i} no es bisiesto")

    print(f"Hay {b} bisiestos" )
    print(f"Hay {b1} que no son bisiestos" )


rango()