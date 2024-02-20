
Compra = {}


cont = 0
print("!BIENVENIDO¡")
print("Si desea terminar el programa ingrese x:")
Total=0
while True:
        
        Articulo = input("Articulo: ")
        if Articulo != "x":
            Precio = float(input("Precio: ") )
            Compra[Articulo] = Precio
            Total +=  Compra[Articulo]
        else:
            break
                
print(" ")
print("LISTA DE COMPRA")

print("_"*45)
o=0
for Articulo in Compra: 
    o += 1
    print("{:^5}{:<20} {:<10}".format(o,Articulo,Compra[Articulo]))
    print("-"*40)
print("-"*40)
print ("{:5}{:<20} {:<20}".format(" ","Total",Total))
print("_"*45)

