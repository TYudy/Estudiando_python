
def año () :
    año= int(input("Por favor ingrese el año"))
    bisiesto(año)



def bisiesto (año):
   
    
    
    if año % 4  == 0 and año % 100 != 0:

        print(f"{año} es bisiesto")

    else:
        print(f"{año} no es bisiesto")


año()