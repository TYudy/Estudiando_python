persona = {
    "Nombre":"Julio" ,
    "Apellido":"Bermudez",
    "Estatura": 1.70,
    "Edad":"40", 
    "Email":"Julio03@gmail.com",
    "CiudadNac":"Barcelona",
    "Genero" : ["Femenino","Masculino","otro"]
    }

print(persona["Nombre"],"La edad de{}",persona["Edad"])
#Agregar clave/valor
persona["Telefono"]= 315851935
print (persona)
#Modificar clave
persona["Celular"] = persona.pop("Telefono")
print(persona)
#Eliminar elemento
del (persona["Celular"])
print(persona)

#Iterar los items de las claves y valores
for clave,valor in persona.items():
    print(clave , ":" , valor)

print(persona["Genero"])