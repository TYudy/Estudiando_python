
def inicio():
    print("Menu principal")
    print("Seleccione la opción correcta")
    print("1 SUMA")
    print("2 RESTA")
    print("3 DIVISIÓN")
    print("4 MULTIPLICACIÓN")
    print("0 FINALIZAR")
    
def main():
    while True:
        opcion = int(input("Seleccione la opción"))
        if opcion == 1:
            print("Ha seleccionado la suma")
            num= int(input("Escriba el primer numero"))
            num2 = int(input("Escriba el segundo numero"))
            suma = num + num2
            print(suma)
        elif  opcion == 2:
            print("Ha seleccionado la resta")
            num= int(input("Escriba el primer numero"))
            num2 = int(input("Escriba el segundo numero"))
            resta = num - num2
            print(resta)
        elif  opcion == 3:
            print("Ha seleccionado la división")
            num= int("Escriba el primer numero")
            num2 = int("Escriba el segundo numero")
            div = num / num2
            print(div)
        elif  opcion == 4:
            print("Ha seleccionado la multiplicación")
            num= int(input("Escriba el primer numero"))
            num2 = int(input("Escriba el segundo numero"))
            mul = num * num2
            print(mul)
        elif opcion == 0:
            print("Gracias por su visita")
            break
        else :
            print("SELECCIONE UNA OPCIÓN VALIDA")
            inicio()
    

inicio()
main()