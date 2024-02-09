texto = "Bunos dias, definiendo un parametro de una función"



def mensaje ():

    N1 = int(input("Ingresar el  primer numero"))
    N2 = int(input("Ingresar el  segundo numero"))
    calcularmayor(N1,N2)
    positivo(N1,N2)
    
    
def calcularmayor(num1,num2):
    if num1 > num2: 
        print("El primer numero es mayor")
    elif num1 == num2:
        print ("Los numeros son iguales")

    else :
        print("El segundo numero es el mayor")


def positivo(p1,p2):
    if p1 >0  and p2 >0:
        print("Numero positivo")
    elif p1 >0 and p2 <0:
        print(f"El  {p1} es positivo y el {p2} es negativo")
    elif p1 <0 and p2 >0:
        print(f"El {p2} es positivo y el {p1} es negativo")
    else:
        print("Son negativos")
mensaje() 