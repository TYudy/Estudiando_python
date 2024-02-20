



def consultarprecio():
    Frutas = {"Manzana": 2.00, "Uva":5.00, "Banano":8.00, "Pera":10.0}
    respuesta2 = input("¿Desea ingresar o eliminar una fruta a la lista? s/n")
    if respuesta2 == "s": 
        res ="s"
        while res == "s":
            
            respuesta3 = input(" Agregar o Eliminar a/e")
            if respuesta3 == "a":
                 agregar(Frutas)
            elif respuesta3 == "e":
                 eliminar(Frutas)
            else:
                 print("No existe")
            res = input("¿Desea continuar? s/n")
    else:
        print(Frutas)
        print("Frutas a consultar")
        respuesta = "s"
        while respuesta == "s":
            Total=0
            fruta = input("Fruta: ")
            cantidad = int(input("Cantidad: ") )
            if fruta in Frutas:
                    Total +=  Frutas[fruta] * cantidad
                    print("EL total de las frutas es: " , Total)
            else:
                print("La fruta ingresada no existe")

            respuesta = input("Desea ingresar otra fruta s/n:")


def agregar(Frutas):
     f= input("Fruta a agregar: ")
     p = input("Precio: ")
     Frutas[f] = p
     print(Frutas)
     
def eliminar(Frutas):
    f= input("Fruta a eliminar: ")
    if f in Frutas:
        del Frutas[f]
        print(Frutas)
    else:
        print("La fruta ingresada no existe en la lista")
     
     


consultarprecio()