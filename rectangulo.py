ancho = int (input("Ingresar el ancho del rectangulo"))
altura = int (input("Ingresar la altura del rectangulo"))
c = input("Ingresar el caracter a utilizar")

def dibujar (an,al,ca):
    
    for i in range (an):

        for j in range (al):
            print(ca,end= " ")
        print()


dibujar(ancho,altura,c)