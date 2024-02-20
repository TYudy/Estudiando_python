

import random

print("MENU")
print("Para el ejercicio de Los jugadores: 1 ")
print("Para el ejercicio de Los alumnos: 2 ")
print("Para el ejercicio de las salas de juego: 3 ")
print("Para el ejercicio de la contraseña: 4 ")
print("Para el ejercicio de aplicar el iva: 5 ")
print("Para finalizar el programa ingrese: 0")

while True :
    ejercicio=int(input("Por favor ingrese el ejercicio el cual desea visualizar: "))
  
    
    if ejercicio == 1:
        print("EJERCICIO 1")
        J1= input("Por favor digite el nombre del primer jugador: ")
        J2= input("Por favor digite el nombre del segundo jugador: ")

        J1n = random.randint(1,6)
        J2n = random.randint(1,6)

        if J1n >J2n :
            print(f"{J1} ha ganado, su numero fue : {J1n} y el numero de {J2} fue : {J2n}")
        elif J2n > J1n:
             print(f"{J2} ha ganado, su numero fue : {J2n} y el numero de {J1} fue : {J1n}")
        else :
             print(f"Ha sido un empate , el numero de {J1} fue : {J1n} y el numero de {J2} fue : {J2n}")


    elif ejercicio == 2:
            print("EJERCICIO 2")
            sexo= input("Por favor indique su sexo")
            nombre=input("Por favor ingrese su nombre")


    elif ejercicio == 3:
        print("EJERCICIO 3")
        nombre= input("Digite su nombre")
        edad= int (input("Digite su edad"))
        if edad < 4:
            print("Puede entrar gratis a la sala")
            
        elif edad >= 4 and edad<= 18:
            print("Debe pagar 30000")
        else:
            print("Debe pagar 50000")

    elif ejercicio == 4:
        print("EJERCICIO 4")
        cont= "contraseña"
        while True:
         cont2 = input("Por favor digite la contraseña: ")
         if cont == cont2:
              print("La contraseña es correcta")
              break
         else:
              print("Contraseña incoreccta, siga intentando")
             


    elif ejercicio == 5:

        print("EJERCICIO 5")
        def iva():
            cantidad = float (input("Por favor digite la cantidad: "))
            iva =  input("Por favor digite el IVA a aplicar: ")
            iva = float(iva)
            porcentaje =  (cantidad * iva)/100
            total = cantidad + porcentaje
            print("El total de la factura sin el Iva es: " , " $", cantidad)
            if iva == 0:
                
                porcentaje =  (total * 21)/100
                total = total + porcentaje
                print("El total con el iva del 21% es: " ,"$", total)

            else:
                print("El total con el iva del % es: ", "$", total)
                

        iva()

    elif ejercicio == 0:
        print("¡Gracias!")
        break