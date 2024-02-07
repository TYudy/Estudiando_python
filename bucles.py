import random

Secreto = random.randint(1,10)
Numero = int(input("Adivine un numero del 1 al 10"))

while Numero != Secreto:
    

    if Numero < Secreto:
        print("El numero es mayor")

    else:
        print("El numero es menor")
    
    Numero = int(input("Adivinar el numero"))


print ("Has adivinado el numero")