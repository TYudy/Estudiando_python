
y = int(input("Cuantas alturas quiere promediar: "))
x = 0
suma = 0
while x != y:
    num=float(input("Por favor digite un numero: "))
    suma = num + suma
    prom = suma / y


    x =  x + 1

print("El promedio de las alturas es: ", prom)
print("La suma de las alturas es: ", suma)
