
y = int(input("Cuantos numeros quiere promediar: "))
x = 0
suma = 0
while x != y:
    num=int(input("Por favor digite un numero: "))
    suma = num + suma
    prom = suma / y


    x =  x + 1

print("El promedio de los numeros ingresados es: ", prom)
print("La suma de los numeros es: ", suma)