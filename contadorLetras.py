Frase = input("Por favor ingrese una frase ")
letra = input("Por favor ingrese la letra que quiere buscar ")
Cl= 0
for i in Frase:
    if i == letra:
        Cl += 1

print ("La letra '%s' aparece %2i en la frase '%s', "%(letra,Cl,Frase))