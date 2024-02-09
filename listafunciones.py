def ingresar ():   
    enteros = []

    for x in range (5):
        numero = int(input("Ingresar el numero"))
        enteros.append (numero)

    imprimir(enteros)
    sumar(enteros)

def imprimir(enteros):
    print("Los numeros son: ")
    for x in (enteros):
        print(x)

def sumar(enteros):
    acum = 0
    for x in (enteros):
        acum = acum + x 

    print(f"La suma es: {acum}")


ingresar()