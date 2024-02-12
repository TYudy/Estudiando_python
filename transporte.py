conductores = []
totalk=0
tkd = []
sumak=0

cant = int(input("Por favor ingrese la cantidad de conductores a registrar"))
for c in range (cant):
    conductor=input(f"Por favor ingrese el nombre del conductor {c+1}: ")
    conductores.append (conductor)
    totalk = 0
    for i in range (1,8):
        print("Dia", i)
        kms= int(input("Por favor ingrese los kilometros recorridos: "))
        totalk += kms
    tkd.append (totalk)

for d in range (len(tkd)):
    sumak += tkd[d]


for l in range (cant):
   print (f"Conductor: {conductores[l]} Km: {tkd[l]}")

  
    




print(conductores)
print(tkd)
print(sumak)

    
